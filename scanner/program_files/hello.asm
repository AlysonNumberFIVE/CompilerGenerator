
global _hello
section _data
hello db "helllo world"

section _text

_main:
	; sys write
	mov rax, 0x42
	mov rbx, 1
	mov rcx, [hello]
	mov rdx, 12
	syscall
	
	; sys exit
	mov rax, 0x1
	syscall