# O QUE FALTA:
# - Conversão de binário para decimal
# - Botão para poder alternar dos dois modos (decimal/binário, binário/decimal)
# - Não permitir mais do que 3 caracteres em cada entry
# - Não permitir mais do que 255 em valor decimal
# - Alterações na interface só para não ficar tão feio :(

from tkinter import * # Importa a biblioteca Tkinter, que é preciso para criar a interface gráfica

def calculation():

    result1 = bin(int(entry1.get()))[2:].zfill(8)
    result2 = bin(int(entry2.get()))[2:].zfill(8)
    result3 = bin(int(entry3.get()))[2:].zfill(8)
    result4 = bin(int(entry4.get()))[2:].zfill(8)
   
    ip_binary = f"{result1}.{result2}.{result3}.{result4}"
    result_label.config(text=ip_binary)

def only_numbers(char):
    return char.isdigit()

window = Tk() # cria a raiz Tk

w = 350 # largura para a raiz Tk
h = 470 # altura para a raiz Tk

# aqui, recebemos a altura e a largura do nosso ecrã
ws = window.winfo_screenwidth() # largura do ecrã
hs = window.winfo_screenheight() # altura do ecrã

# calcula a posição x e y do centro do nosso ecrã
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# define a posição da janela para o centro do ecrã 
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.title("Conversor de IP") # título da janela

vcmd = (window.register(only_numbers), '%S')

# Entradas de texto para efetuar a conversão

entry1 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry1.grid(row=0, column=1)

dot1 = Label(window, font=('Arial', 20), text='.')
dot1.grid(row=0, column=2)

entry2 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry2.grid(row=0, column=3)

dot2 = Label(window, font=('Arial', 20), text='.')
dot2.grid(row=0, column=4)

entry3 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry3.grid(row=0, column=5)

dot3 = Label(window, font=('Arial', 20), text='.')
dot3.grid(row=0, column=6)

entry4 = Entry(window, font=('Arial', 20), bg='lightgray', width=10, justify='center', validate='key', validatecommand=vcmd)
entry4.grid(row=0, column=7)

convertbtn = Button(window, text='Converter', font=('Arial', 20), width=10, command=calculation)
convertbtn.grid(row=1, column=3, columnspan=3, pady=(10, 0))

result_label = Label(window, text='', font=('Arial', 20))
result_label.grid(row=2, column=3, columnspan=8, pady=(10,0))

window.mainloop()
