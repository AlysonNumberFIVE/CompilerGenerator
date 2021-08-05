# CompilerGenerator
The purpose of this repo is to store all the code for my current Medium project.<br><br>

This project, currently entitled Compiler Generator, is a series of project/articles covering my attempt at making a metacompiler from scratch in Golang, following along with the book <a href="">Engineering a Compiler</a>.<br><br>

## Compiler Structure

This project is divided into three parts;

-<b>The Frontend</b>    - The part of the compiler responsible for injesting a raw source code and extracting valid tokens and verifying accurate semantics of the language.<br>
-<b>The middleware</b>  - Intermediate code generation that converts source code into an intermediate pseudocode-like form. Optimization happens here.<br>
-<b>The Backend</b>      - The part of the compiler responsible for converting the intermediate representation into the target system's assmebly architecture.<br>

The aim is to create a metacompiler that, once a language's specification is ingested alongside valid source file(s) of the language to be compiled, the language is successfully compiled into the target architecture of a specified system.<br>

## Progress so Far 

### The Scanner

Currently, an automated scanner generator is implemented. Similar to the `lex/flex` utilities, this one runs on a spec file mainly based on the usage of regex pattern matching.<br>

A C language spec file (see the full file in `specfiles/c.spec`):
```

# Classifier

alphabet    [_a-zA-Z]
digit       [0-9]
number      {digit}+
newline     %NEWLINE
word        {alphabet}({alphabet}|{digit})*
symbols     [-+/\*&!\|\{\}=><:^;,]
equ         ([+-/=*!&\|]|((>)?>)|((<)?<))?=
left        (<)?<
right       (>)?>
brackets    [\[\]\(\)]
comment     //.*{newline}
mcomment    /\*.*\*/
float       [0-9]+((\.[0-9]*)|e((\+|-)?[0-9]+))
hex         0[xX][a-fA-Z0-9]+
string      ".*"
char        '[(\')(\t)(\n)]|(.*)'
arrow			  ->

%%

# Delim
'     {char}
"     {string}
//    {comment}
/\*   {mcomment}

%%

# TokenType

{string}    STRING
{number}    INTEGER
{word}      ID
{char}      CH
char        CHAR
int         INT
long        LONG
void        VOID
unsigned    UNSIGNED
*           STAR
...
```
### Spec file format
The spec file is akin to modified version of the `.l` format used to compile `lex` parsers. Unlike `lex` which generates `.c` source files that compile into the parser themselves, `spec` is the first part of the metacompiler and directly outputs a `Go` list of structs that contain each token. With a `spec` file set, it reads input files and tokenizes the input file going ooff the rules in the spec file. 

##### Structure
Similar to the `lex` file format, the `spec` format has 3 sections, each divided by a pair of `%%`. The spec design is based on 
table driven scanner design.<br>
- Note: a table driven scanner makes use of 3 tables, one with a collection of acceptable DFAs used by the language, a second for classifying input types and a third that holds the valid tokens generated by accepting DFA states. The spec file format is designed to mimick this behaviour with a few modifications to simplify the programming process.<br>

Each section of the spec file's data is laid out as follows:<br>
- <b>Classifier list</b> - This has a list of all the language's regexes. These, alongside helper functions inside the scanner, simulate the concept of DFA state traversal, the saving of accepting states and rollbacks in case of failed states.
- <b>Delim list</b>      - This table is for all language constructs that rely on delimiting tokens to end their parsing. Tokens that go here are those for strings and comments.
- <b>TokenType list</b>  - These are all the valid tokens that are accepted by the specified language.

A slight drawback with this format's design is the heavy reliance on regex knowledge to simulate the DFAs needed for the target language. An optional add-on will be an init file that auto-generates common regexes for common language constructs to speed up spec file development.











