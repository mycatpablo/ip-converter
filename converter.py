from tkinter import * # Importa a biblioteca Tkinter, que é preciso para criar a interface gráfica

class Converter: # Class Converter, que faz a conversão de decimal para binário e vice-versa
    def __init__(self): # Inicializa a class Converter
        self.is_decimal = True
    
    def conversion(self): # Função que faz a conversão
        self.is_decimal = not self.is_decimal

converter = Converter() # Instancia a classe

def calculation(): # Função que faz o cálculo

    try:
        # Converte os valores em inteiros
        val1 = int(entry1.get())
        val2 = int(entry2.get())
        val3 = int(entry3.get())
        val4 = int(entry4.get())

        # Se algum dos valores não cumprir os requisitos, o resultado será uma mensagem de erro
        if any((entry > 255 or entry < 0) if converter.is_decimal else (entry > 11111111 or entry < 0) for entry in [val1, val2, val3, val4]):
            ip_binary = "Erro: Valor acima de 255" if converter.is_decimal else "Erro: Valor acima de 11111111"
        else:
            # Converte os valores para binário
            if converter.is_decimal: # Se for decimal
                result1 = bin(int(entry1.get()))[2:].zfill(8) # Preenche com zeros à esquerda, e tira os primeiros 2 bits
                result2 = bin(int(entry2.get()))[2:].zfill(8)
                result3 = bin(int(entry3.get()))[2:].zfill(8)
                result4 = bin(int(entry4.get()))[2:].zfill(8)
                ip_binary = f"{result1}.{result2}.{result3}.{result4}"
            else: # Se for binário
                ip_binary = f"{int(entry1.get(), 2)}.{int(entry2.get(), 2)}.{int(entry3.get(), 2)}.{int(entry4.get(), 2)}"

    # Se for um erro, o resultado é uma mensagem de erro
    except ValueError:
        ip_binary = "Erro: Não foi introduzido nenhum valor!"

    result_label.config(text=ip_binary)

def only_numbers(char): # Verifica se o caracter introduzido é um número
    return char.isdigit()

def jump_cursor(event): # Move o cursor para o próximo entry
    next_entry = event.tk_focusNext()
    next_entry.focus_set()

def max_numbers(value): # Limita o tamanho dos entries
    for entry in [entry1, entry2, entry3, entry4]:
        value = entry.get() # Recebe o valor do entry
        if converter.is_decimal: # Se o conversor estiver em decimal, limita o tamanho para 3 caracteres
            if value and len(value) > 2:
                jump_cursor(entry)
        else: # Se o conversor estiver em binário, limita o tamanho para 8 caracteres
            if value and len(value) > 7: 
                jump_cursor(entry)

def clear_button_click(): # Limpa os entries
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    result_label.config(text='')
    entry1.focus_set()

def copy_result(): # Copia o resultado para o teclado
    result_text = result_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(result_text)
    copybtn.config(text='Copiado!')
    window.after(1000, lambda: copybtn.config(text='Copiar para o teclado'))

def toggle_button_click(): # Troca o modo de conversão
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    result_label.config(text='')
    entry1.focus_set()
    converter.conversion()
    if converter.is_decimal:
        togglebtn.config(text='Trocar para binário')
    else:
        togglebtn.config(text='Trocar para decimal')

# Interface gráfica

window = Tk() # cria a raiz Tk

w = 675 # largura para a raiz Tk
h = 300 # altura para a raiz Tk

# aqui, recebemos a altura e a largura do nosso ecrã
ws = window.winfo_screenwidth() # largura do ecrã
hs = window.winfo_screenheight() # altura do ecrã

# calcula a posição x e y do centro do nosso ecrã
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# define a posição da janela para o centro do ecrã 
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.title("Conversor de IP") # título da janela

window.resizable(False, False) # Impede que a janela seja redimensionada

# Binds
window.bind("<Escape>", lambda event: clear_button_click())
window.bind("<Return>", lambda event: calculation())
window.bind("<c>", lambda event: copy_result())
window.bind("<t>", lambda event: toggle_button_click())

vcmd = (window.register(only_numbers), '%S') # Regista a função que verifica se o caracter introduzido é um número

initial_text = Label(window, font=('Arial', 20), bg='lightgray', width=10, justify='center')
initial_text.grid(row=0, column=1)

# Entradas de texto para efetuar a conversão

entry1 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry1.grid(row=0, column=1)
entry1.bind("<KeyRelease>", max_numbers)
entry1.focus_set()

dot1 = Label(window, font=('Arial', 20), text='.')
dot1.grid(row=0, column=2)

entry2 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry2.grid(row=0, column=3)
entry2.bind("<KeyRelease>", max_numbers)

dot2 = Label(window, font=('Arial', 20), text='.')
dot2.grid(row=0, column=4)

entry3 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry3.grid(row=0, column=5)
entry3.bind("<KeyRelease>", max_numbers)

dot3 = Label(window, font=('Arial', 20), text='.')
dot3.grid(row=0, column=6)

entry4 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry4.grid(row=0, column=7)
entry4.bind("<KeyRelease>", max_numbers)

convertbtn = Button(window, text='Converter', font=('Arial', 20), width=10, command=calculation)
convertbtn.grid(row=1, column=2, columnspan=2)

clearbtn = Button(window, text='Limpar', font=('Arial', 20), width=10, command=lambda: clear_button_click())
clearbtn.grid(row=1, column=3, columnspan=11)

copybtn = Button(window, text='Copiar para o teclado', font=('Arial', 20), width=17, command = copy_result)
copybtn.grid(row=2, column=2, columnspan=4)

togglebtn = Button(window, text='Trocar para binário', font=('Arial', 20), width=15, command= lambda: toggle_button_click())
togglebtn.grid(row=3, column=2, columnspan=4)

result_label = Label(window, text='', font=('Arial', 20))
result_label.grid(row=4, column=1, columnspan=8)

window.mainloop()
