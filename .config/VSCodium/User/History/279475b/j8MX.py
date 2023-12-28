"""
Програма, що знаходить похідну для даної функції
"""
import tkinter as tk
import sympy as sp

def calculate_derivative():
    """
    Підрахунок похідної функції
    """
    try:
        derr = derrivative_input.get()
        x = sp.symbols(variable_input.get()) if variable_input.get() != "" else sp.symbols('x')
        derr_sp = sp.diff(sp.sympify(derr), x)
        var=variable_input.get() if variable_input.get() != "" else 'x'
        if value_input.get() == "":
            result_text.config(text=f"f'({var}) = {derr_sp}")
        else:
            value=float(value_input.get())
            result=derr_sp.subs(x, value)
            result_text.config(text=f"f'({var}) = {derr_sp}\n\nf'({value}) = {round(result,3)}")
        input_text.config(text=f"f({var}) = {derr}")
    except Exception as e:
        input_text.config(text="")
        result_text.config(text=f"Неправильні вхідні дані!\n({e})")

def clear():
    """
    Очищення всіх полів
    """
    derrivative_input.delete(0,tk.END)
    variable_input.delete(0,tk.END)
    value_input.delete(0,tk.END)
    result_text.config(text="")
    input_text.config(text="")

def init_window():
    """
    Ініціалізація вікна
    """
    window=tk.Tk()
    window.title("Калькулятор похідних")
    window.geometry("750x500")
    window.resizable(True, True)
    return window

def init_buttons(window: tk.Tk):
    """
    Ініціалізація кнопок
    """
    calculateb=tk.Button(window,text="Обчислити похідну",padx=10,\
                           pady=10,font=('Arial', 14),command=calculate_derivative)
    clearb=tk.Button(window,text="Очистити",padx=70,pady=10,font=('Arial', 14), command=clear)
    calculateb.grid(row=3,column=0,columnspan=2)
    clearb.grid(row=3,column=2,columnspan=2)
    return calculateb, clearb
def init_text():
    """
    Ініціалізація тексту
    """
    inputt=tk.Label(calculator_window,text="",font=('Arial', 14),\
                        bd=10,width=45,anchor='w',wraplength=700)
    inputt.grid(row=4,column=0,columnspan=4)
    result=tk.Label(calculator_window,text="",font=('Arial', 14),\
                        bd=10,width=45,anchor='w',wraplength=700)
    result.grid(row=5,column=0,columnspan=4)
    variable_label=tk.Label(calculator_window,text="Змінна:",\
                              font=('Arial',14),bd=10, anchor='e')
    variable_label.grid(row=1,column=0,sticky='e')
    value_label=tk.Label(calculator_window,text="Значення:",\
                           font=('Arial', 14),bd=10,anchor='e')
    value_label.grid(row=2,column=0,sticky='e')
    return inputt,result

def init_entries():
    """
    Ініціалізація полів для вводу даних
    """
    derrivative=tk.Entry(calculator_window,font=('Arial',14),bd=10,\
                            insertwidth=4,width=45,justify='center')
    derrivative.grid(row=0,column=0,columnspan=5)
    variable=tk.Entry(calculator_window,font=('Arial',14),bd=10,\
                              insertwidth=5,width=10,justify='center')
    variable.grid(row=1,column=1,sticky='w')
    value=tk.Entry(calculator_window,font=('Arial',14),bd=10, \
                           insertwidth=5,width=10,justify='center')
    value.grid(row=2,column=1,sticky='w')
    return derrivative,variable,value

calculator_window=init_window()
input_text,result_text=init_text()
calculate_button,clear_button=init_buttons(calculator_window)
derrivative_input,variable_input,value_input=init_entries()

calculator_window.mainloop()