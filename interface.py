from tkinter import *
from calculation import calculate


# реализация пользовательского интерфейса
def load_inter():
    global ans, txt


    # Creating window
    window = Tk()
    window.geometry('500x130')
    window.resizable(width=False, height=False)
    window.title('Square root of a number')
    '''
    Creating elements
    '''

    ans = StringVar()
    ans.set('')

    # MENU
    main_menu = Menu()

    lang_m = Menu()
    lang_m.add_command(label="English")
    lang_m.add_command(label="Spanish")
    lang_m.add_command(label="Chinese")
    lang_m.add_command(label="Russian")

    main_menu.add_cascade(label='Language', menu=lang_m)
    # OUTPUT area
    out = Entry(window, textvariable=ans, width=50, font=('Helvetica', 20), justify='left',
                relief='sunken', state='readonly')
    out.place(x=0, y=0)
    # INPUT area
    txt = Entry(window, width=30)
    txt.place(x=20, y=60)
    # Creating a SPINBOX that allows you to change the PRECISION
    spb = Spinbox(window, from_=0, to=20, state='readonly')
    spb.place(x=250, y=60)
    # Creating BUTTON
    btn = Button(window, text='Calculate', command=get_and_set_number)
    btn.place(x=20, y=85)

    window.config(menu=main_menu)
    window.mainloop()


# функция считывает введённое пользователем значение из диалога ввода, и выводит вычесленное
def get_and_set_number():
    num = txt.get()
    ans.set(calculate(num))






