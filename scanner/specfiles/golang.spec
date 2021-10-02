
# Classifier

alphabet		[_a-zA-Z]
digit			[0-9]
number			{digit}+
newline			%NEWLINE
word			{alphabet}({alphabet}|{digit})*
symbols			[-+/\*&!\|=><:^;,]
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
rune 			'[(\')(\t)(\n)]|(.*)'
equ_assign 		:=

%%

# Delim
'       {rune}
"		{string}
//		{comment}
/\*		{mcomment}

%%

# TokenType

{string}		LITERAL
{number}		LITERAL
{word}			ID
{rune}			LITERAL
var				VAR
*				STAR
struct			STRUCT
<< 				BITLEFT
=				EQU
<				LESSTHAN
{equ_assign}	equ_assign
>				GREATER
>> 				BITRIGHT
>>=				BITRIGHT_EQU
<<=				BITLEFT_EQU
&&				AND
||				OR
!=				NOT
&				BIT_AND
|				BIT_OR
!				MPT
do				DO
for				FOR
continue		CONTINUE
while			WHILE
if 				IF
(				OPENBRACE
)				CLOSEBRACE
{lbrace}		OPENCURLY
{rbrace}		CLOSECURLY
[				OPENBRACKET
]				CLOSEBRACKET
,				COMMA
;				SEMICOLON
case 			CASE
:				COLON
...				ELIPSE
.				DOT
~				TILDE
^				XOR
^=				XOR_EQU
return			RETURN
nil 			NIL