
# Classifier

alphabet		[_a-zA-Z]
digit			[0-9]
number			{digit}+
newline			%NEWLINE
word			{alphabet}({alphabet}|{digit})*
symbols			[-+/\*&!\|\{\}=><:^;]
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

# Delim
'       {char}
"		{string}
//		{comment}
/\*		{mcomment}

%%

# TokenType

{string}		STRING
{number}		INTEGER
{word}			ID
{char}			CH
char			CHAR
int				INT
long			LONG
void			VOID
unsigned		UNSIGNED
*				STAR
struct			STRUCT
union			UNION
<< 				BITLEFT
=				EQU
<				LESSTHAN
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
{				OPENCURLY
}				CLOSECURLY
[				OPENBRACKET
]				CLOSEBRACKET
,				COMMA
;				SEMICOLON
sizeof			SIZEOF
register		REGISTER
short			SHORT
{float}			FLOAT
else			ELSE
case 			CASE
:				COLON
->				DEREF_PTR
...				ELIPSE
?				QMARK
.				DOT
~				TILDE
^				XOR
^=				XOR_EQU
return			RETURN
NULL			NULLTOKEN


