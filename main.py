from tkinter import *
import cmath
from math import sqrt


# Validating input values and calculating result value
def clicked():
    try:
        res = sqrt(float(txt.get()))
        if (int(res) == float(res)):
            res = str(int(res))
        else:
            res = str(float(res))
        ans.set(res)
    except ValueError:
        try:
            tmp = txt.get()
            tmp = tmp.replace(' ', '')
            res = str(cmath.sqrt(complex(tmp)))
            ans.set(res)
        except ValueError:
            ans.set('Please, enter a number')

# Delete functions
def clear():
    txt.delete(0, 'end')

def delete_last():
    txt.delete(len(txt.get())-1,len(txt.get()))

# Creating window
window = Tk()
window.geometry('500x130')
window.resizable(width=False, height=False)
window.title('Square root of a number')
window.configure(bg='#555')

photo = PhotoImage(file='logo.png')
window.iconphoto(False,photo)
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
out = Entry(window, textvariable=ans, width=33, font=('Helvetica', 20), justify='right', relief='sunken', state = 'readonly', bg="#a6a6a6")
out.place(x = 0, y = 0)
#INPUT area
txt = Entry(window, width = 30,bg="#a6a6a6",justify='right')
txt.place(x=20, y=60)
# Creating a SPINBOX that allows you to change the PRECISION
#spb = Spinbox(window, from_=0, to=20, state='readonly',bg="#a6a6a6")
#spb.place(x=250, y=60)
# Creating BUTTON
btn = Button(window, text='Calculate',  bg="#555", fg="#fafafa",  activebackground="#555", activeforeground="#fafafa",command=clicked)
btn.place(x=20, y=83)

btn_del_all = Button(window, text='Clear', bg="#555", fg="#fafafa", activebackground="#555", activeforeground="#fafafa", command=clear)
btn_del_all.place(x=80, y=83)

btn_del_last = Button(window, text='Delete', bg="#555", fg="#fafafa",  activebackground="#555", activeforeground="#fafafa", command=delete_last)
btn_del_last.place(x=120, y=83)

window.config(menu=main_menu)
window.mainloop()
