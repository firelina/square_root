# coding=utf-8
from tkinter import *
import cmath
import math
from decimal import Decimal



# Validating input values and calculating result value
def calculate(num, prec, state):
    num = str(simple_actions(num)).strip('()')
    try:
        prec = int(prec)
    except ValueError:
        return trans[lang_now.get()]["input"]
    # if (state_.get() == True):
    #     try:
    #         INPT = num
    #         INPT = float(INPT)
    #         e = int(prec)
    #         if INPT < 0:
    #             return trans[lang_now.get()]["input"]
    #         tmp = math.sqrt(INPT)
    #         res = round(tmp, e)
    #         if (res == 0):
    #             return str(0)
    #         else:
    #             if (int(res) == float(res)):
    #                 return '±' + str(int(res))
    #             else:
    #                 return '±' + str(res)
    #     except ValueError:
    #         return trans[lang_now.get()]["ent_num"]

    try:
        res = math.sqrt(float(num))
        if (int(res) == float(res)):
            res = str(int(res))
        else:
            res = float(res)
        if (res == '0'):
            return res
        else:
            if state:
                res = round(res, prec)
            else:
                res = int(res)
            return '±' + str(res)
    except OverflowError:
        return '±' + str(int(calculate_big_numbers(int(num))))

    except ValueError:
        try:
            tmp = num
                # if tmp
                # tmp = tmp.replace(' ', '')

            res = cmath.sqrt(complex(tmp))
            if (res.real == 0):
                if state:
                    res = '±' + str(round(res.imag, prec)) + 'j'
                else:
                    res = '±' + str(int(res.imag)) + 'j'

                return res
            else:
                if state:
                    re = str(round(res.real, prec))
                    im = str(round(res.imag, prec))
                else:
                    re = str(res.real)
                    im = str(res.imag)
                if res.imag < 0:
                    res = '±' + re + '∓' + im + 'j'
                else:
                    res = '±' + re + '±' + im + 'j'
                return res
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
                if state:
                    res = '±' + str(round(com.real, prec)) + '∓' + str(round(com.imag, prec)) + 'j'
                else:
                    res = '±' + str(com.real) + '∓' + str(com.imag) + 'j'
                if com.imag > 0:
                    res = '±' + str(com.real) + '±' + str(com.imag) + 'j'
                return res
            except ValueError:
                return trans[lang_now.get()]["ent_num"]


# вычисление корня из очень больших чисел
def calculate_big_numbers(number):
    degree = 2
    nd = Decimal(number)
    exponent = Decimal("1.0") / Decimal(degree)
    return nd ** exponent

def simple_actions(string):
    try:
        # if '+j' in string:
        #     string = string.split('+j')
        #     string = ('+1j').join(string)

        while 'j' in string:
            ind = string.index('j')
            if string[ind - 1] not in '1234567890' or ind == 0:
                string = string[:ind] + '1f' + string[ind + 1:]
            elif string[ind - 1] in '1234567890':
                string = string[:ind] + 'f' + string[ind + 1:]
        string = ('j').join(string.split('f'))


        # print(string)


        if ',' in string:
            string = string.split(',')
            string = ('.').join(string)

        if 'π' in string:
            string = string.split('π')
            string = ('math.pi').join(string)
        if '|' in string:
            while'|' in string:
                ind = string.index('|')
                string = string[:ind] + 'abs(' + string[ind + 1:]
                ind += 4
                while True:

                    if ind >= len(string) or string[ind] not in '-1234567890.':
                        break
                    ind += 1

                string = string[:ind] + ')' + string[ind + 1:]

        if '^' in string:
            string = string.split('^')
            string = ('**').join(string)
        if 'log' in string:
            while 'log(' in string:
                ind = string.index('log(')
                ind1 = string.index('log(') + 4

                comp = False
                while string[ind1] != ')':
                    comp = True if string[ind1] == 'j' else False

                    # if ind1 >= len(string) or string[ind1] not in '-1234567890.':
                    #     break
                    ind1 += 1

                if not comp:
                    string = string[:ind] + 'math.log_(' + string[ind + 4:]
                if comp:
                    string = string[:ind] + 'cmath.log_(' + string[ind + 4:]


            # ind = string.index(')')
            string = ('').join(string.split('_'))
        if 'ln' in string:
            while 'ln(' in string:

                ind = string.index('ln(')
                string = string[:ind] + 'math.log1p_(' + string[ind + 3:]

            # ind = string.index(')')
            string = ('').join(string.split('_'))

        if 'cos' in string:

            while 'cos(' in string:
                ind = string.index('cos(')
                ind1 = string.index('cos(') + 4
                comp = False
                while string[ind1] != ')':
                    comp = True if string[ind1] == 'j' else False

                    # if ind1 >= len(string) or string[ind1] not in '-1234567890.':
                    #     break
                    ind1 += 1

                string = string[:ind1] + ')' + string[ind1:] if not comp else string
                if not comp:
                    string = string[:ind] + 'math.cos_(' + 'math.radians(' + string[ind + 4:]
                if comp:
                    string = string[:ind] + 'cmath.cos_(' + string[ind + 4:]

            string = ('').join(string.split('_'))
        if 'sin' in string:

            while 'sin(' in string:
                ind = string.index('sin(')
                ind1 = string.index('sin(') + 4
                comp = False
                while string[ind1] != ')':
                    comp = True if string[ind1] == 'j' else False

                    # if ind1 >= len(string) or string[ind1] not in '-1234567890.':
                    #     break
                    ind1 += 1

                string = string[:ind1] + ')' + string[ind1:] if not comp else string
                if not comp:
                    string = string[:ind] + 'math.sin_(' + 'math.radians(' + string[ind + 4:]
                if comp:
                    string = string[:ind] + 'cmath.sin_(' + string[ind + 4:]

            string = ('').join(string.split('_'))
        if 'tan' in string:
            while 'tan(' in string:
                ind = string.index('tan(')
                ind1 = string.index('tan(') + 4
                comp = False
                while string[ind1] != ')':
                    comp = True if string[ind1] == 'j' else False

                    # if ind1 >= len(string) or string[ind1] not in '-1234567890.':
                    #     break
                    ind1 += 1

                string = string[:ind1] + ')' + string[ind1:] if not comp else string
                if not comp:
                    string = string[:ind] + 'math.tan_(' + 'math.radians(' + string[ind + 4:]
                if comp:
                    string = string[:ind] + 'cmath.tan_('  + string[ind + 4:]

                # ind = string.index('tan(math.radians(') + len('tan(math.radians(')
            string = ('').join(string.split('_'))

        # if 'cot' in string:
        #     while 'cot(' in string:
        #         ind = string.index('cot(')
        #         ind1 = string.index('cot(') + 4
        #         while True:
        #
        #             if ind1 >= len(string) or string[ind1] not in '-1234567890.':
        #                 break
        #             ind1 += 1
        #
        #         string = string[:ind1] + ')' + string[ind1:]
        #         string = string[:ind] + '1/math.tan(' + 'math.radians(' + string[ind + 4:]
        #
        #         # ind = string.index('tan(math.radians(') + len('tan(math.radians(')
        #     string = ('').join(string.split('_'))

        if '!' in string:
            while '!' in string:
                ind = string.index('!') - 1
                ind1 = string.index('!')
                # string = string.split('!')
                num = ''
                while True:
                    if ind < 0 or string[ind] not in '-1234567890.':
                        break
                    num += string[ind]
                    ind -= 1

                num = num[::-1]
                string = string[:ind + 1] + 'math.factorial(' + num + ')' + string[ind1 + 1:]


        # string = ('))').join(string.split('#'))
        # print(string)
        res = eval(string)
        return res
    except Exception:
        # print(string)
        return trans[lang_now.get()]["ent_num"]

# def simple_actions_complex(string):
#     try:
#         res = eval(string)
#     except ValueError:
#         return trans[lang_now.get()]["ent_num"]



class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 100  # miliseconds
        self.wraplength = 300  # pixels
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
    btn_del_per['text'] = trans[lang_now.get()]["del_per"]
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
    txt.insert(0, 0)
    txt['state'] = 'readonly'


def clear_per():
    set_prec['state'] = 'normal'
    set_prec.delete(0, 'end')
    set_prec.insert(0,0)
    set_prec['state'] = 'readonly'


def clear_last_symbol():
    if state_.get():
        set_prec['state'] = 'normal'
        set_prec.delete(len(set_prec.get()) - 1, len(set_prec.get()))
        if len(set_prec.get()) == 0:
            set_prec.insert(0,0)
        set_prec['state'] = 'readonly'
    else:
        txt['state'] = 'normal'
        txt.delete(len(txt.get()) - 1, len(txt.get()))
        if len(txt.get()) == 0:
            txt.insert(0, 0)
        txt['state'] = 'readonly'


# start_calc
def clicked():
    num = txt.get()
    prec = set_prec.get()
    state = state_.get()
    set_result(calculate(num, prec, state))

def set_result(result):
    ans.set(result)



#   set_symbol_functions
def set_number_symbol(value):
    txt['state'] = 'normal'
    txt.delete(0, 'end')
    txt.insert(0, value)
    txt['state'] = 'readonly'


def set_prec_symbol(value):
    if len(value) == 0:
        set_prec['state'] = 'normal'
        set_prec.delete(0, 'end')
        set_prec.insert(0, value)
        set_prec['state'] = 'readonly'
    elif getint(value) < 16 :
         set_prec['state'] = 'normal'
         if value[0] == '0':
             value=value[1:]
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
            if len(value)== 0:
                value = '0'
            set_number_symbol(value)
        elif event.char.isdigit() or event.char in '+-..j*^,/()':
            value = txt.get() + event.char
            if value[0] == '0':
                value = value[1:]
            if not event.char.isdigit():
                if len(value) > 1 and value[-1] == value[-2]:
                    value = value[:-1]
                elif len(value) > 1 and value[-2] == '.' and value[-1] == ',':
                    value = value[:-2] + ','
                elif len(value) > 1 and value[-2] == ',' and value[-1] == '.':
                    value = value[:-2] + '.'
                elif len(value) > 1 and value[-2] == '(' and value[-1] == ')':
                    value = value[:-2] + ')'
                elif len(value) > 1 and value[-2] == ')' and value[-1] == '(':
                    value = value[:-2] + '('
                elif len(value)> 1 and value[-2] in '-+*/^' and event.char in '-+*/^':
                    value=value[:-2] + event.char
            set_number_symbol(value)
    else:
        if event.char == '\x08':
            value = set_prec.get()
            value = value[:-1]
            if len(value) > 0:
                set_prec_symbol(value)
            else:
                set_prec['state'] = 'normal'
                set_prec.delete(0, 'end')
                set_prec.insert(0, 0)
                set_prec['state'] = 'readonly'
        elif event.char == '\r':
            clicked()
        elif event.char.isdigit():
            set_prec_symbol(set_prec.get() + event.char)

# Work with on-screen buttons

def disable_button():
    if state_.get():
        btn_sin['state'] = 'disable'
        btn_cos['state'] = 'disable'
        btn_tan['state'] = 'disable'
        btn_comma['state'] = 'disable'
        btn_pi['state'] = 'disable'
        btn_imaginary_unit['state'] = 'disable'
        btn_ln['state'] = 'disable'
        btn_log['state'] = 'disable'
        btn_left_parenthesis['state'] = 'disable'
        btn_right_parenthesis['state'] = 'disable'
        btn_exponentiation['state'] = 'disable'
        btn_module['state'] = 'disable'
        btn_factorial['state'] = 'disable'
        btn_dot['state'] = 'disable'
        btn_plus['state'] = 'disable'
        btn_minus['state'] = 'disable'
        btn_multiplication['state'] = 'disable'
        btn_division['state'] = 'disable'
        btn_clean_entry['state'] = 'disable'
    else:
        btn_sin['state'] = 'active'
        btn_cos['state'] = 'active'
        btn_tan['state'] = 'active'
        btn_comma['state'] = 'active'
        btn_pi['state'] = 'active'
        btn_imaginary_unit['state'] = 'active'
        btn_ln['state'] = 'active'
        btn_log['state'] = 'active'
        btn_left_parenthesis['state'] = 'active'
        btn_right_parenthesis['state'] = 'active'
        btn_exponentiation['state'] = 'active'
        btn_module['state'] = 'active'
        btn_factorial['state'] = 'active'
        btn_dot['state'] = 'active'
        btn_plus['state'] = 'active'
        btn_minus['state'] = 'active'
        btn_multiplication['state'] = 'active'
        btn_division['state'] = 'active'
        btn_clean_entry['state'] = 'active'
        btn_delete_last_symbol['state'] = 'active'


def add_symbol(symbol):
    if state_.get():
        value = set_prec.get() + str(symbol)
        set_prec_symbol(value)
    else:
        value = txt.get() + str(symbol)
        if value[0]=='0':
            value=value[1:]
        set_number_symbol(value)

# create_buttons_calculate
# def create_buttons():


# Creating window

window = Tk()
window.geometry('500x190')
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


# files = ['eng', 'spn', 'rus', 'cha']

def add_butts():
    lang_m = Menu()
    if not keys_lang:
        main_menu.add_cascade(label='Language', menu=lang_m)
    trans.clear()
    # if keys_lang:
    #     empty_menu = Menu()
    #     window.config(menu=empty_menu)
    #     empty_menu.add_cascade(label='Language', menu=lang_m)
    #     empty_menu.add_cascade(label='Help', menu=about_m)


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
txt = Entry(window, width=78,justify='right')
txt.insert(0,0)
txt['state'] = 'readonly'
txt.place(x=15, y=45)
INPT_TIP = CreateToolTip(txt, \
                         'Enter in this field the number/expression whose square root you want to calculate. '
                         'Then click on the "Calculate" button. '
                         'To work with complex numbers, use j, not i. ')

# Calculate with given PRECISION
state_ = BooleanVar()
state_.set(0)
chk = Checkbutton(window, variable=state_, onvalue=1, offvalue=0, command=disable_button)
chk.place(x=375, y=111)
# Entry for PREC
set_prec = Entry(window, width=5,  relief='sunken', justify='right')
set_prec.insert(0,0)
set_prec['state'] = 'readonly',
set_prec.place(x=400, y=111)
###TIP for USER
loadimage = PhotoImage(file='yes4.png')
defaultbg = window.cget('bg')
tipBtn = Button(window, image=loadimage, bg=defaultbg, state='disabled')
tipBtn['border'] = '0'
tipBtn.place(x=450, y=102)
button1_ttp = CreateToolTip(tipBtn, \
                            'If you want to calculate the square root with the specified precision,'
                            'check the checkbox. After that, enter the precision with which '
                            'you want to perform the calculations. ')

btn_sin = Button(width=3, text='sin', command=lambda: add_symbol('sin'))
btn_cos = Button(width=3, text='cos', command=lambda: add_symbol('cos'))
btn_tan = Button(width=3, text='tan', command=lambda: add_symbol('tan'))
btn_comma = Button(width=3, text=',', command=lambda: add_symbol(','))
btn_pi = Button(width=3, text='π', command=lambda: add_symbol('π'))
btn_imaginary_unit = Button(width=3, text='j', command=lambda: add_symbol('j'))
btn_ln = Button(width=3, text='ln', command=lambda: add_symbol('ln'))
btn_log = Button(width=3, text='log', command=lambda: add_symbol('log'))
btn_left_parenthesis = Button(width=3, text='(', command=lambda: add_symbol('('))
btn_right_parenthesis = Button(width=3, text=')', command=lambda: add_symbol(')'))
btn_exponentiation = Button(width=3, text='^', command=lambda: add_symbol('^'))
btn_module = Button(width=3, text='|x|', command=lambda: add_symbol('|'))
btn_factorial = Button(width=3, text='n!', command=lambda: add_symbol('!'))
btn_dot = Button(width=3, text='.', command=lambda: add_symbol('.'))
btn_plus = Button(width=3, text='+', command=lambda: add_symbol('+'))
btn_minus = Button(width=3, text='-', command=lambda: add_symbol('-'))
btn_multiplication = Button(width=3, text='*', command=lambda: add_symbol('*'))
btn_division = Button(width=3, text='/', command=lambda: add_symbol('/'))
btn_clean_entry = Button(width=3, text='CE', command= clear)
btn_delete_last_symbol = Button(width=3, text='⇐', command=clear_last_symbol)

btn_digit_1 = Button(width=3, text='1', command=lambda: add_symbol('1'))
btn_digit_2 = Button(width=3, text='2', command=lambda: add_symbol('2'))
btn_digit_3 = Button(width=3, text='3', command=lambda: add_symbol('3'))
btn_digit_4 = Button(width=3, text='4', command=lambda: add_symbol('4'))
btn_digit_5 = Button(width=3, text='5', command=lambda: add_symbol('5'))
btn_digit_6 = Button(width=3, text='6', command=lambda: add_symbol('6'))
btn_digit_7 = Button(width=3, text='7', command=lambda: add_symbol('7'))
btn_digit_8 = Button(width=3, text='8', command=lambda: add_symbol('8'))
btn_digit_9 = Button(width=3, text='9', command=lambda: add_symbol('9'))
btn_digit_0 = Button(width=3, text='0', command=lambda: add_symbol('0'))

# first_floor_digits

btn_digit_1.place(x=195, y=75)
btn_digit_2.place(x=230, y=75)
btn_digit_3.place(x=265, y=75)

# second_floor_digits

btn_digit_4.place(x=195, y=105)
btn_digit_5.place(x=230, y=105)
btn_digit_6.place(x=265, y=105)

# third_floor_digits

btn_digit_7.place(x=195, y=135)
btn_digit_8.place(x=230, y=135)
btn_digit_9.place(x=265, y=135)

# first_floor_operations

btn_sin.place(x=20, y=75)
btn_cos.place(x=55, y=75)
btn_tan.place(x=90, y=75)
btn_exponentiation.place(x=125, y=75)
btn_digit_0.place(x=160, y=75)
btn_clean_entry.place(x=300, y=75)
btn_delete_last_symbol.place(x=335, y=75)

# second_floor_operations

btn_pi.place(x=20, y=105)
btn_imaginary_unit.place(x=55, y=105)
btn_ln.place(x=90, y=105)
btn_factorial.place(x=125, y=105)
btn_comma.place(x=160, y=105)
btn_multiplication.place(x=300, y=105)
btn_division.place(x=335, y=105)

# third_floor_operations

btn_left_parenthesis.place(x=20, y=135)
btn_right_parenthesis.place(x=55, y=135)
btn_log.place(x=90, y=135)
btn_module.place(x=125, y=135)
btn_dot.place(x=160, y=135)
btn_plus.place(x=300, y=135)
btn_minus.place(x=335, y=135)

# create_clear_button

btn_del_per = Button(window, text='Remove precision', width=15, command=clear_per)
btn_del_per.place(x=370, y=135)

# create_calculate_button
btn = Button(window, text='Calculate ', width=15, command=clicked)
btn.place(x=370, y=75)

window.config(menu=main_menu)
window.mainloop()
