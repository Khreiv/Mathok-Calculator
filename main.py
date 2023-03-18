from tkinter import *
from math import *


def key_handler(event):
    if event.keysym.isdigit():
        click(event.keysym)
    elif event.keysym in ('plus', 'minus', 'asterisk', 'slash'):
        click(event.keysym.replace('plus', '+').replace('minus', '-').replace('asterisk', '*').replace('slash', '/'))
    elif event.keysym == 'period':
        click('.')
    elif event.keysym == 'Return':
        operation()
    elif event.keysym == 'Escape':
        clean()
    elif event.keysym == 'BackSpace':
        delete_last()


def delete_last():
    global OPERATOR
    OPERATOR = OPERATOR[:-1]
    input_text.set(OPERATOR)


def disable_arrow_keys(_):
    return "break"


root = Tk()
root.title('mathok')
root.geometry('392x600')
root.iconbitmap('images/mathok.ico')
root.bind('<Key>', key_handler)

input_text = StringVar()
OPERATOR = ''

input_entry = Entry(root, font=('arial', 20), width=22, textvariable=input_text,
                    bd=20, insertbackground='powder blue', bg='powder blue', justify='right')

input_entry.place(x=10, y=60)

input_entry.focus_set()
input_entry.bind('<Left>', disable_arrow_keys)
input_entry.bind('<Right>', disable_arrow_keys)


# NUMBERS
def click(num):
    global OPERATOR
    OPERATOR = OPERATOR + str(num)
    input_text.set(OPERATOR)


# OPERATORS
def operation():
    global OPERATOR
    try:
        # Reemplaza las funciones con sus equivalentes en Python
        OPERATOR = OPERATOR.replace('sqrt', 'sqrt(').replace('log', 'log(').replace('pi', 'pi(')
        # Encuentra todos los paréntesis abiertos y les agrega un paréntesis de cierre
        count_open = OPERATOR.count('(')
        count_close = OPERATOR.count(')')
        OPERATOR += ')' * (count_open - count_close)

        # Convierte la cadena en una lista de términos y operadores
        terms = re.split(r'([+\-*/()])', OPERATOR)

        # Evalúa las funciones matemáticas en la lista
        for i, term in enumerate(terms):
            if term == 'sqrt(':
                terms[i+1] = sqrt(float(terms[i+1]))
            if term == 'log(':
                terms[i+1] = log(float(terms[i+1]))
            if term == 'pi(':
                terms[i+1] = pi

        # Reconstruye la cadena a partir de la lista modificada
        OPERATOR = ''.join([str(term) for term in terms])

        # Ahora evalúa la cadena con las funciones matemáticas ya aplicadas
        op = str(eval(OPERATOR))
        input_text.set(op)
    except:
        input_text.set('3RR0R')
        OPERATOR = ''


# CLEAR
def clean():
    global OPERATOR
    OPERATOR = ''
    input_text.set('0')


# BUTTON SIZE
btn_width = 11
btn_height = 3

# X 0 BUTTONS
Button(root, text='+', width=btn_width, height=btn_height, command=lambda: click('+')).place(x=17, y=180)
Button(root, text='-', width=btn_width, height=btn_height, command=lambda: click('-')).place(x=17, y=240)
Button(root, text='*', width=btn_width, height=btn_height, command=lambda: click('*')).place(x=17, y=300)
Button(root, text='/', width=btn_width, height=btn_height, command=lambda: click('/')).place(x=17, y=360)
Button(root, text='\u221a', width=btn_width, height=btn_height, command=lambda: click('sqrt')).place(x=17, y=420)
Button(root, text='%', width=btn_width, height=btn_height, command=lambda: click('%')).place(x=17, y=480)

# X 1 BUTTONS
Button(root, text='7', width=btn_width, height=btn_height, command=lambda: click(7)).place(x=105, y=180)
Button(root, text='4', width=btn_width, height=btn_height, command=lambda: click(4)).place(x=105, y=240)
Button(root, text='1', width=btn_width, height=btn_height, command=lambda: click(1)).place(x=105, y=300)
Button(root, text='0', width=btn_width, height=btn_height, command=lambda: click(0)).place(x=105, y=360)
Button(root, text='EXP', width=btn_width, height=btn_height, command=lambda: click('**')).place(x=105, y=420)
Button(root, text='In', width=btn_width, height=btn_height, command=lambda: click('log')).place(x=105, y=480)

# X 2 BUTTONS
Button(root, text='8', width=btn_width, height=btn_height, command=lambda: click(8)).place(x=193, y=180)
Button(root, text='5', width=btn_width, height=btn_height, command=lambda: click(5)).place(x=193, y=240)
Button(root, text='2', width=btn_width, height=btn_height, command=lambda: click(2)).place(x=193, y=300)
Button(root, text=',', width=btn_width, height=btn_height, command=lambda: click('.')).place(x=193, y=360)
Button(root, text='(', width=btn_width, height=btn_height, command=lambda: click('(')).place(x=193, y=420)
Button(root, text='\u03C0', width=btn_width, height=btn_height, command=lambda: click('pi')).place(x=193, y=480)

# X 3 BUTTONS
Button(root, text='9', width=btn_width, height=btn_height, command=lambda: click(9)).place(x=282, y=180)
Button(root, text='6', width=btn_width, height=btn_height, command=lambda: click(6)).place(x=282, y=240)
Button(root, text='3', width=btn_width, height=btn_height, command=lambda: click(3)).place(x=282, y=300)
Button(root, text='C', width=btn_width, height=btn_height, command=clean).place(x=282, y=360)
Button(root, text=')', width=btn_width, height=btn_height, command=lambda: click(')')).place(x=282, y=420)
Button(root, text='=', width=btn_width, height=btn_height, command=operation).place(x=282, y=480)

# TK LOOP
root.mainloop()
