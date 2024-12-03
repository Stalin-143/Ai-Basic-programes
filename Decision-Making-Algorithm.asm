section .data
    prompt db "Enter your password: ", 0
    weak_msg db "Weak password", 0
    strong_msg db "Strong password", 0
    buffer db 32
    length equ $ - buffer

section .bss
    password resb 32

section .text
    global _start

_start:
    ; Prompt user for password
    mov eax, 4          ; syscall: sys_write
    mov ebx, 1          ; file descriptor: stdout
    mov ecx, prompt     ; message
    mov edx, length     ; message length
    int 0x80            ; syscall interrupt

    ; Read input password
    mov eax, 3          ; syscall: sys_read
    mov ebx, 0          ; file descriptor: stdin
    mov ecx, password   ; buffer
    mov edx, 32         ; buffer size
    int 0x80            ; syscall interrupt

    ; Initialize counters
    xor ebx, ebx        ; has_upper
    xor ecx, ecx        ; has_lower
    xor edx, edx        ; has_digit
    xor esi, esi        ; has_special
    xor edi, edi        ; length

    mov esi, password   ; point to password buffer

check_char:
    mov al, [esi]       ; load character
    cmp al, 0           ; end of string?
    je evaluate         ; if yes, jump to evaluation

    inc edi             ; increase length counter

    ; Check uppercase
    cmp al, 'A'
    jl check_lower
    cmp al, 'Z'
    jg check_lower
    mov bl, 1           ; set has_upper = 1
    jmp next_char

check_lower:
    cmp al, 'a'
    jl check_digit
    cmp al, 'z'
    jg check_digit
    mov cl, 1           ; set has_lower = 1
    jmp next_char

check_digit:
    cmp al, '0'
    jl check_special
    cmp al, '9'
    jg check_special
    mov dl, 1           ; set has_digit = 1
    jmp next_char

check_special:
    ; Check if character is a special symbol
    cmp al, '!'
    je set_special
    cmp al, '@'
    je set_special
    cmp al, '#'
    je set_special
    cmp al, '$'
    je set_special
    cmp al, '%'
    je set_special
    cmp al, '^'
    je set_special
    cmp al, '&'
    je set_special
    cmp al, '*'
    je set_special
    jmp next_char

set_special:
    mov esi, 1          ; set has_special = 1

next_char:
    inc esi             ; next character
    jmp check_char

evaluate:
    cmp edi, 8          ; length >= 8?
    jl weak_password

    ; Check if all flags are set
    test bl, bl         ; has_upper?
    jz weak_password
    test cl, cl         ; has_lower?
    jz weak_password
    test dl, dl         ; has_digit?
    jz weak_password
    test esi, esi       ; has_special?
    jz weak_password

strong_password:
    ; Print "Strong password"
    mov eax, 4
    mov ebx, 1
    mov ecx, strong_msg
    mov edx, 14
    int 0x80
    jmp exit

weak_password:
    ; Print "Weak password"
    mov eax, 4
    mov ebx, 1
    mov ecx, weak_msg
    mov edx, 12
    int 0x80

exit:
    mov eax, 1          ; syscall: sys_exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; syscall interrupt
