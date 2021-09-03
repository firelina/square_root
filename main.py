from tkinter import *
import cmath
from math import sqrt
import googletrans

#Validating input values and calculating result value
def clicked():
    try:
        res = sqrt(float(txt.get()))
        if(int(res) == float(res)):
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



#Creating window
window = Tk()
window.geometry('500x130')
window.resizable(width=False, height=False)
window.title('Square root of a number')
'''
Creating elements
'''

ans = StringVar()
ans.set('')

#MENU
main_menu = Menu()

lang_m = Menu()
lang_m.add_command(label="English")
lang_m.add_command(label="Spanish")
lang_m.add_command(label="Chinese")
lang_m.add_command(label="Russian")

main_menu.add_cascade(label = 'Language', menu = lang_m)
#OUTPUT area
out = Entry(window, textvariable = ans, width = 33, font=('Helvetica', 20), justify='right', relief = 'sunken', state = 'readonly')
out.place(x = 0, y = 0)
#INPUT area
txt = Entry(window, width = 30)
txt.place(x = 20, y = 60)
#Creating a SPINBOX that allows you to change the PRECISION
spb = Spinbox(window, from_= 0, to = 20, state = 'readonly')
spb.place(x = 250, y = 60)
#Creating BUTTON
btn = Button(window, text = 'Calculate', command = clicked)
btn.place(x = 20, y = 85)

window.config(menu=main_menu)
window.mainloop()
