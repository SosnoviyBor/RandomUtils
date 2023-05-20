IDEAL
MODEL small
STACK 256

; ==================================== Макроси ====================================
; ---------------------------------------------------------------------------------
; Призначення: ініціалізація програми
; ---------------------------------------------------------------------------------
MACRO M_init        ; Макрос для ініціалізації. Його початок
    mov ax, @data   ; @data ідентифікатор, що створюються директивою MODEL
    mov ds, ax      ; Завантаження початку сегменту даних в регістр DS
    mov es, ax      ; Завантаження початку сегменту даних в регістр ES
    ENDM M_init     ; Кінець макросу

; ---------------------------------------------------------------------------------
; Призначення: вихід із програми (із кодом 0)
; ---------------------------------------------------------------------------------
MACRO M_exit
    mov ah, 4ch
    mov al, 0
    int 21h
    ENDM M_exit

; ---------------------------------------------------------------------------------
; Призначення: вихід із програми (із кодом FF)
; ---------------------------------------------------------------------------------
MACRO M_error_exit
    mov ah, 4ch
    mov al, 0FFh
    int 21h
    ENDM M_error_exit

; ---------------------------------------------------------------------------------
; Призначення: перевод строки
; ---------------------------------------------------------------------------------
MACRO M_crlf
    push ax
    push dx

    mov ah, 09h
    mov dx, offset crlf
    int 21h

    pop dx
    pop ax
    ENDM M_crlf

; ---------------------------------------------------------------------------------
; Призначення: сокращение количества кода
; DX <- сообщение для вывода
; ---------------------------------------------------------------------------------
MACRO M_print
    push ax
    mov ah, 09h
    int 21h
    pop ax
    ENDM M_print

; ---------------------------------------------------------------------------------
; Призначення: простая очистка экрана
; ---------------------------------------------------------------------------------
MACRO M_clearscreen
    push ax
    mov al, 2
    mov ah, 0
    int 10h
    pop ax
    ENDM M_clearscreen

; ---------------------------------------------------------------------------------
; Призначення: запам'ятовування значень регістрів
; ---------------------------------------------------------------------------------
MACRO M_push_all
    push ax
    push bx
    push cx
    push dx
    push bp
    push si
    push di
    ENDM M_push_all

; ---------------------------------------------------------------------------------
; Призначення: повернення значень регістрів
; ---------------------------------------------------------------------------------
MACRO M_pop_all
    pop di
    pop si
    pop bp
    pop dx
    pop cx
    pop bx
    pop ax
    ENDM M_pop_all

DATASEG

crlf db 10, 13, "$"

CODESEG
Start:
    M_init



    M_exit

    ; =================================== Процедури ===================================
    ; ---------------------------------------------------------------------------------
    ; Предназначение: выбрасывание разных ошибок
    ; Ввод:
    ; BX <- код ошибки менеджера
    ; Вывод: ---
    ; ---------------------------------------------------------------------------------
    proc error_manager
        mov ah, 09h
        cmp bx, 1h      ; too long input error
        je too_long_error
        cmp bx, 2h      ; wrong input error
        je wrong_input_error
        cmp bx, 0ffffh  ; overflow error
        je overflow_error
        jmp halt

        too_long_error:     ; BX <- 1
            mov dx, offset too_long_err
            int 21h
            jmp halt
        wrong_input_error:  ; BX <- 2
            mov dx, offset wrong_input_err
            int 21h
            jmp halt
        overflow_error:     ; BX <- FFFFh
            mov dx, offset overflow_err
            int 21h
            jmp halt

        halt:
        M_error_exit
        ret
    endp error_manager


    end Start