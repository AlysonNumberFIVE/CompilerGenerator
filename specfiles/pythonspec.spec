# Classifier
# A list of all regexes used in the language to identify valid patterns

alphabet		[_a-zA-Z]
digit			[0-9]
word			{alphabet}({alphabet}|{digit})*
number			{digit}+
float			[0-9]+((\.[0-9]*)|e((\+|-)?[0-9]+))
indet 			%TAB
symbols			[+-/=*!&\|\^@]
equ				([+-/=*!&\|]|((>)?>)|((<)?<))?=
left			(<)?<
right			(>)?>
brackets		[\[\]\(\)]
misc 			[:]
newline 		%NEWLINE
str 			".*"
str2 			'.*'
mcomm 			'''.*'''
mcomm2 			""".*"""
fstring 		[fouri]".*"
hex 			0[xX][a-fA-Z0-9]+

# float			{digit}+((\.{digit}*)|e((\+|-)?{digit}+))
# equ			({symbols}|({left}|{right}))?=

%%

# Delim
# first column has token  description, followed by first token regex, and then its regex pattern
''' 		{mcomm}
""" 		{mcomm2}
# 			#.*{newline}
' 			{str2}
" 			{str}
0[xX]		{hex}
f"		 	{fstring}

%%

# TokenType
# A list of all the tokens used in the language and their identifying type names.

{fstring}						FSTRING
{str2}							STRING
{str}							STRING
def								FUNC_DECL
{word}							ID
True							TRUE
False							FALSE
{number}   						INTEGER
:								COLON
{float}							FLOAT
( 								O PENBRACE
) 								CLOSEBRACE
[								OPENBRACKET
]								CLOSEBRACKET
,								COMMA
+								PLUS
-								MINUS
* 								MULTIPLY
/ 								DIVIDE
= 								ASSIGN
== 								EQUAL
+=								ADD_ASSIGN
-=								SUB_ASSIGN
*=								MUL_ASSIGN
/=								DIV_ASSIGN
>								GREATER
<								LESS
<=								GREATER_EQU
>=								LESS_EQU
|								OR
&								AND
^								XOR
in  							IN
and 							AND
or 								OR
not								NOT
else 							ELSE
<< 								BIT_LEFT
>> 								BIT_RIGHT
>>= 							BITRIGHT_EQU
<<=								BITLEFT_EQU
{indent}						INDENT
None							KEYWORD
as 								KEYWORD
import 							KEYWORD
break							KEYWORD
continue 						KEYWORD
del 							KEYWORD
from 							KEYWORD
return 							KEYWORD
class 							KEYWORD
do								KEYWORD
elif							KEYWORD
for								KEYWORD
while							KEYWORD
global 							KEYWORD
@ 								AT






