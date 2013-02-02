	.section	__TEXT,__text,regular,pure_instructions
	.globl	_foo_stupid
	.align	4, 0x90
_foo_stupid:
	pushl	%ebp
	movl	%esp, %ebp
	movl	$1, %eax
	popl	%ebp
	ret

	.globl	_main
	.align	4, 0x90
_main:
	pushl	%ebp
	movl	%esp, %ebp
	popl	%ebp
	ret


.subsections_via_symbols
