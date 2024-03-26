"""
NAME: calculator-basic.py
DESC: Tkinter-GUI based python program that will operate
as a calculator. Basic operations (+, -, *, /).
"""

# Import tkinter
from tkinter import *

# Root Window
root = Tk()
root.geometry("350x350")
root.resizable(0,0)
root.title("Bailey Arick - Calculator Project")

############ ALL FUNCTIONS ############
'''
NAME: btn_click()
ARGS: item (any)
DESC: Function will serve as an event action for all the buttons.
      It will update the current expression and display it to the
      screen.
'''
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


'''
NAME: btn_clear()
ARGS: none
DESC: Function will only serve for the "clear" button. It will empty out
      the current expression and set the display accordingly.
'''
def btn_clear():
    global expression
    expression = ""
    input_text.set("")


'''
NAME: btn_equal()
ARGS: none
DESC: Function will only serve for the "equals" button. It will evaluate
      the current expression and update it with the result and display
      it to the screen.
'''
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result


expression = ""
input_text = StringVar()  # input_screen entry

############ ALL WIDGETS BELOW ############
# Frames
display_frame = Frame(root, highlightbackground="black")  # frame for display screen
display_frame.pack(side=TOP)
btn_frame = Frame(root, width=320, height=275)  # frame for buttons
btn_frame.pack()

# Display "Screen"
input_screen = Entry(display_frame, font="consolas 20 bold", textvariable=input_text, width=50, justify=RIGHT)
input_screen.grid(row=0, column=0)
input_screen.pack(ipady=10)

# first row
clear_btn = Button(btn_frame, text="C", width=34, height=3, cursor="hand2", command=lambda: btn_clear())
clear_btn.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide_btn = Button(btn_frame, text="/", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: btn_click("/"))
divide_btn.grid(row=0, column=3, padx=1, pady=1)

# second row
seven_btn = Button(btn_frame, font="consolas 10", text="7", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(7))
seven_btn.grid(row=1, column=0)
eight_btn = Button(btn_frame, font="consolas 10", text="8", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(8))
eight_btn.grid(row=1, column=1)
nine_btn = Button(btn_frame, font="consolas 10", text="9", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(9))
nine_btn.grid(row=1, column=2, padx=1, pady=1)
multiply_btn = Button(btn_frame, font="consolas 10", text="*", fg="black", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: btn_click("*"))
multiply_btn.grid(row=1, column=3, padx=1, pady=1)

# third row
four_btn = Button(btn_frame, font="consolas 10", text="4", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(4))
four_btn.grid(row=2, column=0, padx=1, pady=1)
five_btn = Button(btn_frame, font="consolas 10", text="5", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(5))
five_btn.grid(row=2, column=1, padx=1, pady=1)
six_btn = Button(btn_frame, font="consolas 10", text="6", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(6))
six_btn.grid(row=2, column=2, padx=1, pady=1)
subtract_btn = Button(btn_frame, font="consolas 10", text="-", fg="black", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: btn_click("-"))
subtract_btn.grid(row=2, column=3, padx=1, pady=1)

# fourth row
one_btn = Button(btn_frame, font="consolas 10", text="1", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(1))
one_btn.grid(row=3, column=0, padx=1, pady=1)
two_btn = Button(btn_frame, font="consolas 10", text="2", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(2))
two_btn.grid(row=3, column=1, padx=1, pady=1)
three_btn = Button(btn_frame, font="consolas 10", text="3", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(3))
three_btn.grid(row=3, column=2, padx=1, pady=1)
addition_btn = Button(btn_frame, font="consolas 10", text="+", fg="black", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: btn_click("+"))
addition_btn.grid(row=3, column=3, padx=1, pady=1)

# fifth row
zero_btn = Button(btn_frame, font="consolas 10", text="0", fg="black", width=22, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
zero_btn.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point_btn = Button(btn_frame, font="consolas 10", text=".", fg="black", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click("."))
point_btn.grid(row=4, column=2, padx=1, pady=1)
equals_btn = Button(btn_frame, font="consolas 10", text="=", fg="black", width=10, height=3, bg="#eee", cursor="hand2", command=lambda: btn_equal())
equals_btn.grid(row=4, column=3, padx=1, pady=1)
############ ALL WIDGETS ABOVE ############

# Display loop
root.mainloop()
