from tkinter import *
import cmath
import math

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 100     #miliseconds
        self.wraplength = 180   #pixels
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
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
#TRANSLATE
def trans_0():
    window.title('Square root of a number')
    btn['text'] = 'Calculate'
    btn_del_all['text'] = 'Clear'
    main_menu.entryconfig(1, label = 'Language')
    main_menu.entryconfig(2, label = 'Help')
    about_m.entryconfig(1, label = 'About us')
    INPT_TIP = CreateToolTip(txt, \
    'Enter in this field the number whose square root you want to calculate. '
    'Then click on the "Calculate" button. '
    'To work with complex numbers, use j, not i. ')
    button1_ttp = CreateToolTip(tipBtn, \
    'If you want to calculate the square root with the specified precision,'
    'check the checkbox. After that, enter the precision with which '
    'you want to perform the calculations. ')
    lang_now.set(0)
    
def trans_1():
    window.title('Raíz cuadrada de un número')
    btn['text'] = 'Calcular'
    btn_del_all['text'] = 'Claro'
    main_menu.entryconfig(1, label = 'Idioma')
    main_menu.entryconfig(2, label = 'Asistencia')
    about_m.entryconfig(1, label = 'Sobre nosotros')
    INPT_TIP = CreateToolTip(txt, \
    'Introduzca en este campo el número cuya raíz cuadrada desea calcular. '
    'A continuación, haga clic en el botón "Calcular". '
    'Para trabajar con números complejos, use j, no i. ')
    button1_ttp = CreateToolTip(tipBtn, \
    'Si desea calcular la raíz cuadrada con la precisión especificada,'
    'marca la casilla de verificación. Después de eso, introduzca la precisión con la que '
    'quieres hacer los cálculos. ')
    lang_now.set(1)
    
def trans_2():
    window.title('数的平方根')
    btn['text'] = '计算'
    btn_del_all['text'] = '清除'
    main_menu.entryconfig(1, label = '语言')
    main_menu.entryconfig(2, label = '救命')
    about_m.entryconfig(1, label = '关于我们')
    INPT_TIP = CreateToolTip(txt, \
    '在此字段中输入要计算其平方根的数字。 '
    '然后点击"计算"按钮。 '
    '要处理复数，请使用j，而不是i。')
    button1_ttp = CreateToolTip(tipBtn, \
    '如果你想以指定的精度计算平方根，'
    '勾选复选框。 之后，输入精度与'
    '你想执行计算。 ')
    lang_now.set(2)
    
def trans_3():
    window.title('Вычисление квдратного корня числа')
    btn['text'] = 'Вычислить'
    btn_del_all['text'] = 'Очистить'
    main_menu.entryconfig(1, label = 'Язык')
    main_menu.entryconfig(2, label = 'Помощь')
    about_m.entryconfig(1, label = 'О нас')
    INPT_TIP = CreateToolTip(txt, \
    'Введите в это поле число, корень квадратный которого надо '
    'вычислить. Затем нажмите на кнопку "Вычислить". Чтобы '
    'работать с комплексными числами, используйте j вместо i. ')
    button1_ttp = CreateToolTip(tipBtn, \
    'Если вы хотите выполнить вычисление квадратного корня с '
    'заданной точностью, поставьте галочку в клеточку. После '
    'этого введите точность, с который вы хотите произвести вычисления. ')
    lang_now.set(3)

#Check state
def check_state():
    if(state_.get() == True):
        set_prec.config(state = 'normal')
    else:
        set_prec.config(state = 'readonly')

#CLEAR
def clear():
    txt.delete(0, 'end')

#Validating input values and calculating result value
def clicked():
    if(lang_now.get() == 0):
        if(state_.get() == True):
            try:
                INPT = txt.get()
                INPT = float(INPT)
                def x(n, INPT):
                    return (1/2)*(n+INPT/n)
                sqrt = 0
                n = 1
                e = set_prec.get()
                e = float(e)
                if(e < 0):
                    ans.set('Incorrect input')
                elif INPT < 0 :
                    ans.set('Incorrect input')
                else :
                    while abs(x(n, INPT)-n) > e:
                        sqrt = x(n, INPT)
                        n = sqrt
                    if(sqrt == 0):
                        ans.set(str(0))
                    else:
                        ans.set('±' + str(sqrt))
            except ValueError:
                ans.set('Please, enter a number')
        else:
            try:
                res = math.sqrt(float(txt.get()))
                if(int(res) == float(res)):
                    res = str(int(res))
                else:
                    res = str(float(res))
                if(res == '0'):
                    ans.set(res)
                else:
                    ans.set('±' + str(res))
            except ValueError:
                try:
                    tmp = txt.get()
                    tmp = tmp.replace(' ', '')
                    res = cmath.sqrt(complex(tmp))
                    if(res.real == 0):
                        ans.set('±' + str(res.imag) + 'j')
                    else:
                        re = str(res.real)
                        im = str(res.imag)
                        ans.set(re + '±' + im + 'j')
                except ValueError:
                    ans.set('Please, enter a number')
                    
    elif(lang_now.get() == 1):
        if(state_.get() == True):
            try:
                INPT = txt.get()
                INPT = float(INPT)
                def x(n, INPT):
                    return (1/2)*(n+INPT/n)
                sqrt = 0
                n = 1
                e = set_prec.get()
                e = float(e)
                if(e < 0):
                    ans.set('Entrada incorrecta')
                elif INPT < 0 :
                    ans.set('Entrada incorrecta')
                else :
                    while abs(x(n, INPT)-n) > e:
                        sqrt = x(n, INPT)
                        n = sqrt
                    if(sqrt == 0):
                        ans.set(str(0))
                    else:
                        ans.set('±' + str(sqrt))
            except ValueError:
                ans.set('Por favor, introduzca un número')
        else:
            try:
                res = math.sqrt(float(txt.get()))
                if(int(res) == float(res)):
                    res = str(int(res))
                else:
                    res = str(float(res))
                if(res == '0'):
                    ans.set(res)
                else:
                    ans.set('±' + str(res))
            except ValueError:
                try:
                    tmp = txt.get()
                    tmp = tmp.replace(' ', '')
                    res = cmath.sqrt(complex(tmp))
                    if(res.real == 0):
                        ans.set('±' + str(res.imag) + 'j')
                    else:
                        re = str(res.real)
                        im = str(res.imag)
                        ans.set(re + '±' + im + 'j')
                except ValueError:
                    ans.set('Por favor, introduzca un número')
                    
    elif(lang_now.get() == 2):
        if(state_.get() == True):
            try:
                INPT = txt.get()
                INPT = float(INPT)
                def x(n, INPT):
                    return (1/2)*(n+INPT/n)
                sqrt = 0
                n = 1
                e = set_prec.get()
                e = float(e)
                if(e < 0):
                    ans.set('输入不正确')
                elif INPT < 0 :
                    ans.set('输入不正确')
                else :
                    while abs(x(n, INPT)-n) > e:
                        sqrt = x(n, INPT)
                        n = sqrt
                    if(sqrt == 0):
                        ans.set(str(0))
                    else:
                        ans.set('±' + str(sqrt))
            except ValueError:
                ans.set('请输入数字')
        else:
            try:
                res = math.sqrt(float(txt.get()))
                if(int(res) == float(res)):
                    res = str(int(res))
                else:
                    res = str(float(res))
                if(res == '0'):
                    ans.set(res)
                else:
                    ans.set('±' + str(res))
            except ValueError:
                try:
                    tmp = txt.get()
                    tmp = tmp.replace(' ', '')
                    res = cmath.sqrt(complex(tmp))
                    if(res.real == 0):
                        ans.set('±' + str(res.imag) + 'j')
                    else:
                        re = str(res.real)
                        im = str(res.imag)
                        ans.set(re + '±' + im + 'j')
                except ValueError:
                    ans.set('请输入数字')
                    
    elif(lang_now.get() == 3):
        if(state_.get() == True):
            try:
                INPT = txt.get()
                INPT = float(INPT)
                def x(n, INPT):
                    return (1/2)*(n+INPT/n)
                sqrt = 0
                n = 1
                e = set_prec.get()
                e = float(e)
                if(e < 0):
                    ans.set('Неверный ввод')
                elif INPT < 0 :
                    ans.set('Неверный ввод')
                else :
                    while abs(x(n, INPT)-n) > e:
                        sqrt = x(n, INPT)
                        n = sqrt
                    if(sqrt == 0):
                        ans.set(str(0))
                    else:
                        ans.set('±' + str(sqrt))
            except ValueError:
                ans.set('Пожалуйста, введите число')
        else:
            try:
                res = math.sqrt(float(txt.get()))
                if(int(res) == float(res)):
                    res = str(int(res))
                else:
                    res = str(float(res))
                if(res == '0'):
                    ans.set(res)
                else:
                    ans.set('±' + str(res))
            except ValueError:
                try:
                    tmp = txt.get()
                    tmp = tmp.replace(' ', '')
                    res = cmath.sqrt(complex(tmp))
                    if(res.real == 0):
                        ans.set('±' + str(res.imag) + 'j')
                    else:
                        re = str(res.real)
                        im = str(res.imag)
                        ans.set(re + '±' + im + 'j')
                except ValueError:
                    ans.set('Пожалуйста, введите число')

#Creating window
window = Tk()
window.geometry('500x130')
window.resizable(width=False, height=False)
window.title('Square root of a number')

'''
Creating elements
'''

lang_now = IntVar()
lang_now.set(0)

ans = StringVar()
ans.set('')

#MENU
main_menu = Menu()

lang_m = Menu()
lang_m.add_command(label="English", command = trans_0)
lang_m.add_command(label="Español", command = trans_1)
lang_m.add_command(label="中文", command = trans_2)
lang_m.add_command(label="Русский", command = trans_3)

about_m = Menu()
about_m.add_command(label = "About us")

main_menu.add_cascade(label = 'Language', menu = lang_m)
main_menu.add_cascade(label = 'Help', menu = about_m)
#OUTPUT area
out = Entry(window, textvariable = ans, width = 83, justify='right', relief = 'sunken', state = 'readonly')
out.place(x = 0, y = 0)
#INPUT area
txt = Entry(window, width = 30)
txt.place(x = 20, y = 60)
INPT_TIP = CreateToolTip(txt, \
    'Enter in this field the number whose square root you want to calculate. '
    'Then click on the "Calculate" button. '
    'To work with complex numbers, use j, not i. ')

#Calculate with given PRECISION
state_ = BooleanVar()
state_.set(0)
chk = Checkbutton(window, variable = state_, onvalue = 1, offvalue = 0, command = check_state)
chk.place(x = 300, y = 60)
##Entry for PREC
set_prec = Entry(window, width = 11, relief = 'sunken', state = 'readonly')
set_prec.place(x = 305, y = 85)
###TIP for USER
loadimage = PhotoImage(file = 'yes4.png')
defaultbg = window.cget('bg')
tipBtn = Button(window, image = loadimage, bg = defaultbg, state = 'disabled')
tipBtn['border'] = '0'
tipBtn.place(x = 378, y = 60)
button1_ttp = CreateToolTip(tipBtn, \
   'If you want to calculate the square root with the specified precision,'
   'check the checkbox. After that, enter the precision with which '
   'you want to perform the calculations. ')

#CLEAR BUTTON
btn_del_all = Button(window, text='Clear', command=clear)
btn_del_all.place(x = 95, y = 85)

#Creating BUTTON 
btn = Button(window, text = 'Calculate', command = clicked)
btn.place(x = 20, y = 85)

window.config(menu=main_menu)
window.mainloop()
