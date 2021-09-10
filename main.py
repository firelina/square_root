# coding=utf-8
from tkinter import *
import cmath
import math


# Validating input values and calculating result value
def calculate(num, prec):
    if (state_.get() == True):
        try:
            INPT = num
            INPT = float(INPT)
            e = int(prec)
            if INPT < 0:
                return trans[lang_now.get()]["input"]
            tmp = math.sqrt(INPT)
            res = round(tmp, e)
            if (res == 0):
                return str(0)
            else:
                if (int(res) == float(res)):
                    return '±' + str(int(res))
                else:
                    return '±' + str(res)
        except ValueError:
            return trans[lang_now.get()]["ent_num"]
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
                try:
                    Ims = ''
                    Rez = ''
                    jfind = False
                    for i in range(0, len(tmp)):
                        if not (jfind) and tmp[i] != 'j':
                            Ims += tmp[i]
                        elif tmp[i] == 'j':
                            jfind = True
                        else:
                            Rez += tmp[i]
                    imsint = int(Ims)
                    if Rez[0] == '-':
                        rezint = -int(Rez[1:])
                    else:
                        rezint = int(Rez)
                    com = cmath.sqrt(complex(rezint, imsint))
                    return '±' + str(com.real) + '∓' + str(com.imag) + 'j'
                except ValueError:
                    return trans[lang_now.get()]["ent_num"]


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


keys_lang = []
# keys_trans = ["title", "text", 'del_num', 'del_per', 'lang', 'help', 'aboutus', 'enter_num_tip', 'enter_per_tip', 'input', 'ent_num']

# trans = {'English': {"title": 'Square root of a number', "text": 'Calculate', 'del_num': 'Remove number',
#           'del_per': 'Remove precision', 'lang': 'Language', 'help': 'Help', 'aboutus': 'About us'}}
trans = {}


# TRANSLATE
def lang_change(*args):
    # print(lang_now.get())
    window.title(trans[lang_now.get()]["title"])
    btn['text'] = trans[lang_now.get()]["text"]
    btn_del_all['text'] = trans[lang_now.get()]["del_num"]
    btn_del_all_per['text'] = trans[lang_now.get()]["del_per"]
    main_menu.entryconfig(1, label=trans[lang_now.get()]["lang"])
    main_menu.entryconfig(2, label=trans[lang_now.get()]["help"])
    about_m.entryconfig(1, label=trans[lang_now.get()]["aboutus"])
    INPT_TIP = CreateToolTip(txt, \
                             trans[lang_now.get()]["enter_num_tip"])
    button1_ttp = CreateToolTip(tipBtn, \
                                trans[lang_now.get()]["enter_per_tip"])


# CLEAR
def clear():
    txt['state'] = 'normal'
    txt.delete(0, 'end')
    txt['state'] = 'readonly'


def clearper():
    set_prec['state'] = 'normal'
    set_prec.delete(0, 'end')
    set_prec['state'] = 'readonly'


# start_calc
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
            elif len(value) > 1 and value[-1] == value[-2]:
                value = value[:-1]
            elif len(value) > 1 and value[-2] == '-' and value[-1] == '+':
                value = value[:-2] + '+'
            elif len(value) > 1 and value[-2] == '+' and value[-1] == '-':
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
            value = set_prec.get() + event.char
            if len(value) > 1 and value[-1] == value[-2]:
                value = value[:-1]
            set_prec_symbol(value)


# create_buttons_calculate
def create_buttons():
    
    btn_sin = Button(width=3, text='sin')
    btn_cos = Button(width=3, text='cos')
    btn_tan = Button(width=3, text='tan')
    btn_cot = Button(width=3, text='cot')
    btn_pi = Button(width=3, text='π')
    btn_imaginary_unit = Button(width=3, text='j')
    btn_ln = Button(width=3, text='ln')
    btn_log = Button(width=3, text='log')
    btn_left_parenthesis = Button(width=3, text='(')
    btn_right_parenthesis = Button(width=3, text=')')
    btn_exponentiation = Button(width=3, text='^')
    btn_module = Button(width=3, text='|x|')
    btn_factorial = Button(width=3, text='n!')
    btn_dot = Button(width=3, text='.')
    btn_plus = Button(width=3, text='+')
    btn_minus = Button(width=3, text='-')
    btn_multiplication = Button(width=3, text='*')
    btn_division = Button(width=3, text='/')
    btn_clean_entry = Button(width=3,text='CE')
    btn_delete_last_symbol = Button(width=3, text='⇐')


    btn_digit_1 = Button(width=3, text='1')
    btn_digit_2 = Button(width=3, text='2')
    btn_digit_3 = Button(width=3, text='3')
    btn_digit_4 = Button(width=3, text='4')
    btn_digit_5 = Button(width=3, text='5')
    btn_digit_6 = Button(width=3, text='6')
    btn_digit_7 = Button(width=3, text='7')
    btn_digit_8 = Button(width=3, text='8')
    btn_digit_9 = Button(width=3, text='9')
    btn_digit_0 = Button(width=3, text='0')

    # first_floor_digits

    btn_digit_1.place(x=195, y=120)
    btn_digit_2.place(x=230, y=120)
    btn_digit_3.place(x=265, y=120)

    # second_floor_digits

    btn_digit_4.place(x=195, y=150)
    btn_digit_5.place(x=230, y=150)
    btn_digit_6.place(x=265, y=150)

    # third_floor_digits

    btn_digit_7.place(x=195, y=180)
    btn_digit_8.place(x=230, y=180)
    btn_digit_9.place(x=265, y=180)

    # first_floor_operations

    btn_sin.place(x=20, y=120)
    btn_cos.place(x=55, y=120)
    btn_tan.place(x=90, y=120)
    btn_cot.place(x=125, y=120)
    btn_digit_0.place(x=160, y=120)
    btn_clean_entry.place(x=300,y=120)
    btn_delete_last_symbol.place(x=335,y=120)

    # second_floor_operations

    btn_pi.place(x=20, y=150)
    btn_imaginary_unit.place(x=55, y=150)
    btn_ln.place(x=90, y=150)
    btn_log.place(x=125, y=150)
    btn_module.place(x=160, y=150)
    btn_multiplication.place(x=300, y=150)
    btn_division.place(x=335,y=150)

    # third_floor_operations

    btn_left_parenthesis.place(x=20, y=180)
    btn_right_parenthesis.place(x=55, y=180)
    btn_dot.place(x=90, y=180)
    btn_exponentiation.place(x=125, y=180)
    btn_factorial.place(x=160,y=180)
    btn_plus.place(x=300,y=180)
    btn_minus.place(x=335,y=180)

# Creating window

window = Tk()
window.geometry('500x300')
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
lang_now.trace("w", lang_change)

ans = StringVar()
ans.set('')

# MENU
main_menu = Menu()


def add_butts():
    lang_m = Menu()
    if not keys_lang:
        main_menu.add_cascade(label='Language', menu=lang_m)
    trans.clear()

    f = open("all_languages", encoding="utf-8")
    data = f.read()
    data = data.split('***\n')
    keys_lang.clear()
    count = -1
    for lang in data:
        count += 1
        phrases = lang.split('...\n')
        lang_title = phrases.pop(0).split(':')[1].strip()
        keys_lang.append(lang_title)
        trans[count] = {}
        for i in range(len(phrases)):
            key, val = phrases[i].split(':')
            trans[count][key] = val.strip()
        lang_m.add_radiobutton(label=lang_title, variable=lang_now, value=count)
    f.close()


add_butts()

about_m = Menu()
about_m.add_command(label="About us")

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
# Entry for PREC
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

# create_clear_button
btn_del_all = Button(window, text='Remove number', command=clear)
btn_del_all.place(x=95, y=83)

btn_del_all_per = Button(window, text='Remove precision', command=clearper)
btn_del_all_per.place(x=320, y=83)

# create_calculate_button
btn = Button(window, text='√', command=clicked)
btn.place(x=20, y=83)

# create_buttons
create_buttons()

window.config(menu=main_menu)
window.mainloop()
