; ---------------------------------------------------------------------------------
; Предназначение: Парс десятичного числа в стринг
; Ввод:
; SI <- Ссылка на начало стринга для записи
; AX <- Число для парса
; Вывод: ---
; ---------------------------------------------------------------------------------
proc dec2string
    push bx
    push cx

    mov bx, 10d     ; 0 для проверки на последний разряд
    mov cx, 0
    Splitter:
        inc cx
        cmp ax, bx
        xor dx, dx  ; Сбрасываем регистр DX, потому что иначе div начинает выкобениваться
        div bx      ; Делим АХ на 10
        push dx     ; Остаток (последняя цифра числа) записывается в стек. Так мы сможем получать их в правильном порядке потом
        xor dx, dx  ; Сбрасываем регистр DX, потому что иначе div начинает выкобениваться
        cmp ax, 0
        jne Splitter
   
    Writer:
        pop dx          ; Достаем последний доступный десяток
        add dx, 30h     ; Делаем из числа символ цифры
        mov [si], dx    ; Заносим цифру в стринг
        inc si
        dec cx
        jnz Writer
   
    mov [si], "$"
    pop cx
    pop bx
    ret
endp dec2string
