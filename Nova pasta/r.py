import tkinter as tk


def mostrar():
    dado=  nome.get()
    dado1 = idade.get()
    dado2 = email.get()
    dado3 = endereço.get()
    dado4 = cep.get()
    dado5 = cidade.get()
    dado6 = cursos.get()


    print(dado,dado1,dado2,dado3,dado4,dado5,dado6)



janela = tk.Tk()


janela.geometry('800x600')
janela.configure(bg = 'white')
janela.iconbitmap()

texto = tk.Label(janela, text = 'cadastre - se', font=('arial', 25), bg = 'white')
texto.pack(pady=90)


nome = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
nome.pack()


idade= tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
idade.pack()

email = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
email.pack()

endereço = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
endereço.pack()

cep = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
cep.pack()

cidade = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
cidade.pack()

cursos= tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
cursos.pack()

btn  =  tk.Button(janela, text= 'MOSTRAR', font=('arial', 15), bg = '#e5e5e5', command=mostrar)
btn.pack()

texto2 = tk.Label(janela, text = 'VAI APARECER AQUI', font=('arial', 25), bg = 'white')
texto2.pack(pady=20)


janela.mainloop()