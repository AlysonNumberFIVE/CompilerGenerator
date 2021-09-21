
# Classifiers

alphabet 		[_a-zA-Z]
digit 			[0-9]
number 			{digit}+
hex				{digit}+h
word 			{alphabet}({alphabet}|{digit})*
label 			_{alphabet}({alphabet}|{digit})*:
colon 			:
newline 		%NEWLINE
comma			,
brackets 		[\[\]]
space 			%SPACE
gen_regs		[er][abcd]x
small_regs		[abcd][lhx]
push 			push(a)?
pop 			pop(a)?
hex 			0[xX][a-fA-F0-9]+
comment 		;.*{newline}
string			".*"
char			'.*'

%%
# delim

; 		{comment}
" 		{string}
' 		{char}
0[xX]	{hex}


%%
# tokenType

{label}		LABEL
{number}	INTEGER
{hex}		INTEGER
syscall 	SYSCALL
{string}	STRING
{word}		ID
section 	SECTION
extern 		EXTERN
include 	INCLUDE
_data		DATA
_text		TEXT
_bss		BSS
db			DB
dq			DQ
dw			DW
mov			MOV
cmp			CMP
rax			GREG64
rbx			GREG64
rcx			GREG64
rdx			GREG64
eax			GREG32
ebx			GREG32
ecx			GREG32
edx			GREG32
ax			GREG16
bx			GREG16
cx			GREG16
dx			GREG16
al 			GREG8
ah 			GREG8
bl 			GREG8
bh 			GREG8
cl 			GREG8
ch 			GREG8
dl 			GREG8
dh 			GREG8
push 		PUSH
pop 		POP
pusha 		PUSHA
,			COLON
popa 		POPA
int 		INT
[			OPENBRACKET
]			CLOSEBRACKET




