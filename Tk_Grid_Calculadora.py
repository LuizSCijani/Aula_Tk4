from tkinter import *

#criar a janela/window
janela = Tk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)
janela.bind('7', lambda event: entrada('7'))
janela.bind('8', lambda event: entrada('8'))
janela.bind('9', lambda event: entrada('9'))
janela.bind('*', lambda event: entrada('*'))
janela.bind('4', lambda event: entrada('4'))
janela.bind('5', lambda event: entrada('5'))
janela.bind('6', lambda event: entrada('6'))
janela.bind('/', lambda event: entrada('/'))
janela.bind('1', lambda event: entrada('1'))
janela.bind('2', lambda event: entrada('2'))
janela.bind('3', lambda event: entrada('3'))
janela.bind('+', lambda event: entrada('+'))
janela.bind('0', lambda event: entrada('0'))
janela.bind('=', lambda event: saida())
janela.bind('.', lambda event: entrada('.'))
janela.bind('-', lambda event: entrada('-'))
janela.bind('<BackSpace>', lambda event: deletar())
janela.bind('C', lambda event: entrada('C'))
janela.bind('(', lambda event: entrada('('))
janela.bind(')', lambda event: entrada(')'))

#criar a função
def entrada(valor):
    label['text'] += valor

def saida():
    resultado = eval(label['text'])
    label['text'] = str(resultado)

def deletar():
    label['text'] = label['text'][:-1]

#criar os widgets
label = Label(janela, text='', font='Arial 20')
bt1 = Button(janela, text='7', font='Arial 22', command=lambda: entrada('7'))
bt2 = Button(janela, text='8', font='Arial 22', command=lambda: entrada('8'))
bt3 = Button(janela, text='9', font='Arial 22', command=lambda: entrada('9'))
bt4 = Button(janela, text='*', font='Arial 22', command=lambda: entrada('*'))
bt5 = Button(janela, text='4', font='Arial 22', command=lambda: entrada('4'))
bt6 = Button(janela, text='5', font='Arial 22', command=lambda: entrada('5'))
bt7 = Button(janela, text='6', font='Arial 22', command=lambda: entrada('6'))
bt8 = Button(janela, text='/', font='Arial 22', command=lambda: entrada('/'))
bt9 = Button(janela, text='1', font='Arial 22', command=lambda: entrada('1'))
bt10 = Button(janela, text='2', font='Arial 22', command=lambda: entrada('2'))
bt11 = Button(janela, text='3', font='Arial 22', command=lambda: entrada('3'))
bt12 = Button(janela, text='+', font='Arial 22', command=lambda: entrada('+'))
bt13 = Button(janela, text='0', font='Arial 22', command=lambda: entrada('0'))
bt14 = Button(janela, text='=', font='Arial 22', command=lambda: saida())
bt15 = Button(janela, text='.', font='Arial 22', command=lambda: entrada('.'))
bt16 = Button(janela, text='-', font='Arial 22', command=lambda: entrada('-'))
bt17 = Button(janela, text='Del', font='Arial 22', command=lambda: deletar())
bt18 = Button(janela, text='C', font='Arial 22')
bt19 = Button(janela, text='(', font='Arial 22', command=lambda: entrada('('))
bt20 = Button(janela, text=')', font='Arial 22', command=lambda: entrada(')'))

#organizar os widgets/layout
label.grid(row=0)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=1, column=1, sticky=NSEW)
bt3.grid(row=1, column=2, sticky=NSEW)
bt4.grid(row=1, column=3, sticky=NSEW)
bt5.grid(row=2, column=0, sticky=NSEW)
bt6.grid(row=2, column=1, sticky=NSEW)
bt7.grid(row=2, column=2, sticky=NSEW)
bt8.grid(row=2, column=3, sticky=NSEW)
bt9.grid(row=3, column=0, sticky=NSEW)
bt10.grid(row=3, column=1, sticky=NSEW)
bt11.grid(row=3, column=2, sticky=NSEW)
bt12.grid(row=3, column=3, sticky=NSEW)
bt13.grid(row=4, column=0, sticky=NSEW)
bt14.grid(row=4, column=1, sticky=NSEW)
bt15.grid(row=4, column=2, sticky=NSEW)
bt16.grid(row=4, column=3, sticky=NSEW)
bt17.grid(row=5, column=0, sticky=NSEW)
bt18.grid(row=5, column=1, sticky=NSEW)
bt19.grid(row=5, column=2, sticky=NSEW)
bt20.grid(row=5, column=3, sticky=NSEW)

#executar a janela
janela.mainloop()