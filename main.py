import tkinter
from tkinter import *
import cmath
import math


# Validating input values and calculating result value
def calculate(num, prec):
    dictt = {'input': ['Incorrect input', 'Entrada incorrecta', '输入不正确', 'Неверный ввод'],
             'ent_num': ['Please, enter a number', 'Por favor, introduzca un número', '请输入数字',
                         'Пожалуйста, введите число']}

    if (state_.get() == True):
        try:
            INPT = num
            INPT = float(INPT)

            def x(n, INPT):
                return (1 / 2) * (n + INPT / n)

            sqrt = 0
            n = 1
            e = prec
            e = float(e)
            if (e < 0):
                return dictt['input'][lang_now.get()]
            elif INPT < 0:
                return dictt['input'][lang_now.get()]
            else:
                while abs(x(n, INPT) - n) > e:
                    sqrt = x(n, INPT)
                    n = sqrt
                if (sqrt == 0):
                    return str(0)
                else:
                    return '±' + str(sqrt)
        except ValueError:
            return dictt['ent_num'][lang_now.get()]
    else:
        try:
            res = math.sqrt(float(num))
            if (int(res) == float(res)):
                res = str(int(res))
            else:
                res = str(float(res))
            if (res == '0'):
                return res
            else:
                return '±' + str(res)
        except ValueError:
            try:
                tmp = num
                # if tmp
                tmp = tmp.replace(' ', '')

                res = cmath.sqrt(complex(tmp))
                if (res.real == 0):
                    return '±' + str(res.imag) + 'j'
                else:
                    re = str(res.real)
                    im = str(res.imag)
                    return '±' + re + '∓' + im + 'j'
            except ValueError:
                return dictt['ent_num'][lang_now.get()]


class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 100  # miliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                      background="#ffffff", relief='solid', borderwidth=1,
                      wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


# TRANSLATE
def trans_0():
    window.title('Square root of a number')
    btn['text'] = 'Calculate'
    btn_del_all['text'] = 'Remove number'
    btn_del_all_per['text'] = 'Remove precision'
    main_menu.entryconfig(1, label='Language')
    main_menu.entryconfig(2, label='Help')
    about_m.entryconfig(1, label='About us')
    INPT_TIP = CreateToolTip(txt, \
                             'Enter in this field the number whose square root you want to calculate. '
                             'Then click on the "Calculate" button. '
                             'To work with complex numbers, use j, not i. '
                             'To work with real numbers, use ".", not ","')
    button1_ttp = CreateToolTip(tipBtn, \
                                'If you want to calculate the square root with the specified precision,'
                                'check the checkbox. After that, enter the precision with which '
                                'you want to perform the calculations. ')
    lang_now.set(0)


def trans_1():
    window.title('Raíz cuadrada de un número')
    btn['text'] = 'Calcular'
    btn_del_all['text'] = 'Eliminar número'
    btn_del_all_per['text'] = 'Eliminar precisión'
    main_menu.entryconfig(1, label='Idioma')
    main_menu.entryconfig(2, label='Asistencia')
    about_m.entryconfig(1, label='Sobre nosotros')
    INPT_TIP = CreateToolTip(txt, \
                             'Introduzca en este campo el número cuya raíz cuadrada desea calcular. '
                             'A continuación, haga clic en el botón "Calcular". '
                             'Para trabajar con números complejos, use j, no i. '
                             'Para trabajar con números reales, use ".", No ","')
    button1_ttp = CreateToolTip(tipBtn, \
                                'Si desea calcular la raíz cuadrada con la precisión especificada,'
                                'marca la casilla de verificación. Después de eso, introduzca la precisión con la que '
                                'quieres hacer los cálculos. ')
    lang_now.set(1)


def trans_2():
    window.title('数的平方根')
    btn['text'] = '计算'
    btn_del_all['text'] = '删除编号'
    btn_del_all_per['text'] = '删除精度'
    main_menu.entryconfig(1, label='语言')
    main_menu.entryconfig(2, label='救命')
    about_m.entryconfig(1, label='关于我们')
    INPT_TIP = CreateToolTip(txt, \
                             '在此字段中输入要计算其平方根的数字。 '
                             '然后点击"计算"按钮。 '
                             '要处理复数，请使用j，而不是i。'
                             '要处理实数，请使用“.”，而不是“,”')
    button1_ttp = CreateToolTip(tipBtn, \
                                '如果你想以指定的精度计算平方根，'
                                '勾选复选框。 之后，输入精度与'
                                '你想执行计算。 ')
    lang_now.set(2)


def trans_3():
    window.title('Вычисление квдратного корня числа')
    btn['text'] = 'Вычислить'
    btn_del_all['text'] = 'Удалить число'
    btn_del_all_per['text'] = 'Очистить точность'
    main_menu.entryconfig(1, label='Язык')
    main_menu.entryconfig(2, label='Помощь')
    about_m.entryconfig(1, label='О нас')
    INPT_TIP = CreateToolTip(txt, \
                             'Введите в это поле число, корень квадратный которого надо '
                             'вычислить. Затем нажмите на кнопку "Вычислить". Чтобы '
                             'работать с комплексными числами, используйте j вместо i. '
                             'Чтобы работать с вещественными числами, используйте ".", а не ","')
    button1_ttp = CreateToolTip(tipBtn, \
                                'Если вы хотите выполнить вычисление квадратного корня с '
                                'заданной точностью, поставьте галочку в клеточку. После '
                                'этого введите точность, с который вы хотите произвести вычисления. ')
    lang_now.set(3)


# Check state
'''
def check_state():
    if (state_.get() == True):
        set_prec.config(state='normal')
    else:
        set_prec.config(state='readonly')
'''


# CLEAR
def clear():
    txt['state'] = 'normal'
    txt.delete(0, 'end')
    txt['state'] = 'readonly'


def clearper():
    set_prec['state'] = 'normal'
    set_prec.delete(0, 'end')
    set_prec['state'] = 'readonly'


# clicked_calculate
def clicked():
    num = txt.get()
    prec = set_prec.get()
    ans.set(calculate(num, prec))


#   set_symbol_functions
def set_number_symbol(value):
    txt['state'] = 'normal'
    txt.delete(0, 'end')
    txt.insert(0, value)
    txt['state'] = 'readonly'


def set_prec_symbol(value):
    set_prec['state'] = 'normal'
    set_prec.delete(0, 'end')
    set_prec.insert(0, value)
    set_prec['state'] = 'readonly'


# key_events
def press_key(event):
    if not state_.get():
        if event.char == '\r':
            clicked()
        elif event.char == '\x08':
            value = txt.get()
            value = value[:-1]
            set_number_symbol(value)
        elif event.char.isdigit() or event.char in '+-..j':
            value = txt.get() + event.char
            if event.char.isdigit():
                set_number_symbol(value)
            elif value[-1] == value[-2]:
                value = value[:-1]
            elif value[-2] == '-' and value[-1] == '+':
                value = value[:-2] + '+'
            elif value[-2] == '+' and value[-1] == '-':
                value = value[:-2] + '-'
            set_number_symbol(value)
    else:
        if event.char == '\x08':
            value = set_prec.get()
            value = value[:-1]
            set_prec_symbol(value)
        elif event.char == '\r':
            clicked()
        elif event.char.isdigit():
            set_prec_symbol(set_prec.get() + event.char)
        elif event.char in '..':
            value=set_prec.get() + event.char
            if value[-1] == value[-2]:
                value=value[:-1]
            set_prec_symbol(value)
# Creating window
window = Tk()
window.geometry('500x130')
window.resizable(width=False, height=False)
window.title('Square root of a number')
photo = PhotoImage(file='logo.png')
window.iconphoto(False, photo)
window.bind('<Key>', press_key)
'''
Creating elements
'''

lang_now = IntVar()
lang_now.set(0)

ans = StringVar()
ans.set('')

# MENU
main_menu = Menu()

lang_m = Menu()
lang_m.add_command(label="English", command=trans_0)
lang_m.add_command(label="Español", command=trans_1)
lang_m.add_command(label="中文", command=trans_2)
lang_m.add_command(label="Русский", command=trans_3)

about_m = Menu()
about_m.add_command(label="About us")

main_menu.add_cascade(label='Language', menu=lang_m)
main_menu.add_cascade(label='Help', menu=about_m)
# OUTPUT area
out = Entry(window, textvariable=ans, width=83, justify='right', relief='sunken', state='readonly')
out.place(x=0, y=0)
# INPUT area
txt = Entry(window, width=30, justify='right', state='readonly')
txt.place(x=20, y=60)
INPT_TIP = CreateToolTip(txt, \
                         'Enter in this field the number whose square root you want to calculate. '
                         'Then click on the "Calculate" button. '
                         'To work with complex numbers, use j, not i. ')

# Calculate with given PRECISION
state_ = BooleanVar()
state_.set(0)
chk = Checkbutton(window, variable=state_, onvalue=1, offvalue=0)
chk.place(x=300, y=60)
##Entry for PREC
set_prec = Entry(window, width=22, relief='sunken', state='readonly', justify='right')
set_prec.place(x=320, y=60)
###TIP for USER
loadimage = PhotoImage(file='yes4.png')
defaultbg = window.cget('bg')
tipBtn = Button(window, image=loadimage, bg=defaultbg, state='disabled')
tipBtn['border'] = '0'
tipBtn.place(x=460, y=73)
button1_ttp = CreateToolTip(tipBtn, \
                            'If you want to calculate the square root with the specified precision,'
                            'check the checkbox. After that, enter the precision with which '
                            'you want to perform the calculations. ')

# CLEAR BUTTON
btn_del_all = Button(window, text='Remove number', command=clear)
btn_del_all.place(x=95, y=83)

btn_del_all_per = Button(window, text='Remove precision', command=clearper)
btn_del_all_per.place(x=320, y=83)

# Creating BUTTON
btn = Button(window, text='Calculate', command=clicked)
btn.place(x=20, y=83)

window.config(menu=main_menu)
window.mainloop()
