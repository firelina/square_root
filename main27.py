#coding=utf-8
from Tkinter import *
import cmath
import math




# Validating input values and calculating result value
def calculate(num, prec):


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
                return trans[lang_now.get()]["input"]
            elif INPT < 0:
                return trans[lang_now.get()]["input"]
            else:
                while abs(x(n, INPT) - n) > e:
                    sqrt = x(n, INPT)
                    n = sqrt
                if (sqrt == 0):
                    return str(0)
                else:
                    return '±' + str(sqrt)
        except ValueError:
            print(lang_now.get())
            return trans[lang_now.get().strip()]["ent_num"]
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
keys_trans = ["title", "text", 'del_num', 'del_per', 'lang', 'help', 'aboutus', 'enter_num_tip', 'enter_per_tip', 'input', 'ent_num']

# trans = {'English': {"title": 'Square root of a number', "text": 'Calculate', 'del_num': 'Remove number',
#           'del_per': 'Remove precision', 'lang': 'Language', 'help': 'Help', 'aboutus': 'About us'}}
trans = {}

# TRANSLATE
def lang_change(*args):
    print(lang_now.get())
    window.title(trans[lang_now.get()]["title"])
    btn['text'] = trans[lang_now.get()]["text"]
    btn_del_all['text'] = trans[lang_now.get()]["del_num"]
    btn_del_all_per['text'] = trans[lang_now.get()]["del_per"]
    main_menu.entryconfig(1, label=trans[lang_now.get()]["lang"])
    main_menu.entryconfig(2, label=trans[lang_now.get()]["help"])
    about_m.entryconfig(1, label=trans[lang_now.get()]["aboutus"])
    INPT_TIP = CreateToolTip(txt, trans[lang_now.get()]["enter_num_tip"])
    button1_ttp = CreateToolTip(tipBtn, trans[lang_now.get()]["enter_per_tip"])


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
            value=set_prec.get() + event.char
            if len(value) > 1 and value[-1] == value[-2]:
                value=value[:-1]
            set_prec_symbol(value)


# Creating window
window = Tk()
window.geometry('500x130')
window.resizable(width=False, height=False)
window.title('Square root of a number')
# photo = PhotoImage(file='logo.png')
# window.iconphoto(False, photo)
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

    f = open("all_languages")
    data = f.read()
    data = data.split('***\n')
    # keys_lang.clear()
    # print(len(data))
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
##Entry for PREC
set_prec = Entry(window, width=22, relief='sunken', state='readonly', justify='right')
set_prec.place(x=320, y=60)
###TIP for USER
# loadimage = PhotoImage(file='yes4.png')
defaultbg = window.cget('bg')
# tipBtn = Button(window, image=loadimage, bg=defaultbg, state='disabled')
tipBtn = Button(window, bg=defaultbg, state='disabled')
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
