
# Classifier

alphabet		[_a-zA-Z]
digit			[0-9]
number			{digit}+
newline			%NEWLINE
word			{alphabet}({alphabet}|{digit})*
symbols			[-+/\*&!\|=><:^;,@]
lbrace 			%LBRC
rbrace 			%RBRC
equ             ([+-/=*!&\|]|((>)?>)|((<)?<))?=
left            (<)?<
right           (>)?>
brackets        [\[\]\(\)]
comment 		//.*{newline}
mcomment		/\*.*\*/
float           [0-9]+((\.[0-9]*)|e((\+|-)?[0-9]+))
hex             0[xX][a-fA-Z0-9]+
string			".*"
char 			'[(\')(\t)(\n)]|(.*)'	

%%

# Delim tokens come here

' 		{char}
"		{string}
//		{comment}
/*		{mcomment}

%%

# And token types here
# Below is a list of generic token types. Feel free to edit out whatever isn't needed.

{string} 	LITERAL
{number}	NUMBER 
{word}		IDENTIFIER
+ 			PLUS
-			MINUS
/			DIVIDE
(			OPENBRACKET
)			CLOSEBRACKET
{lbrace}	OPENBRACE 
{rbrace} 	CLOSEBRACE
>> 			LSHIFT
<< 			RSHIFT
<<= 		LSHIFT_ASSIGN
>>=			RSHIFT_ASSIGN
[			OPENBLOCK
]			CLOSEBLOCK
int 		DATATYPE
string 		DATATYPE
char 		DATATYPE
float 		FLOAT
* 			STAR
if 			IF
while 		WHILE
else		ELSE
@			DEREF
;			SEMICOLON
.			DOT
,			COMMA