from tkinter import *
from tkinter import ttk
import parser

class Calculator:

    def __init__(self):
        self.root = Tk()
        self.root.title( "Calculator")
        self.root.config( background="white")

        self.display = ttk.Entry( self.root)
        self.display.grid( column=0, row=0, columnspan=4, padx=10, pady=10, sticky="we")
        self.display.config( font="Nunito 16 normal", foreground="black")

        #NUMERIC BUTTONS
        ttk.Button( self.root, text="7", command=lambda: self.get_numbers(7)).grid( column=0, row=2, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="8", command=lambda: self.get_numbers(8)).grid( column=1, row=2, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="9", command=lambda: self.get_numbers(9)).grid( column=2, row=2, padx=5, pady=5, sticky="nsew")

        ttk.Button( self.root, text="4", command=lambda: self.get_numbers(4)).grid( column=0, row=3, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="5", command=lambda: self.get_numbers(5)).grid( column=1, row=3, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="6", command=lambda: self.get_numbers(6)).grid( column=2, row=3, padx=5, pady=5, sticky="nsew")

        ttk.Button( self.root, text="1", command=lambda: self.get_numbers(1)).grid( column=0, row=4, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="2", command=lambda: self.get_numbers(2)).grid( column=1, row=4, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="3", command=lambda: self.get_numbers(3)).grid( column=2, row=4, padx=5, pady=5, sticky="nsew")

        #MID BUTTONS
        ttk.Button( self.root, text="0", command=lambda: self.get_numbers(0)).grid( column=0, row=5, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="(", command=lambda: self.get_operation("(")).grid( column=1, row=5, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text=")", command=lambda: self.get_operation(")")).grid( column=2, row=5, padx=5, pady=5, sticky="nsew")

        #MATH OPERATORS BUTTONS
        ttk.Button( self.root, text="÷", command=lambda: self.get_operation("/")).grid( column=3, row=2, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="×", command=lambda: self.get_operation("*")).grid( column=3, row=3, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="-", command=lambda: self.get_operation("-")).grid( column=3, row=4, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="+", command=lambda: self.get_operation("+")).grid( column=3, row=5, padx=5, pady=5, sticky="nsew")

        #BOTTOM BUTTONS
        ttk.Button( self.root, text="AC", command=lambda: self.clear_display()).grid( column=0, row=6, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="⟵", command=lambda: self.undo()).grid( column=1, row=6, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text=".", command=lambda: self.get_numbers(".")).grid( column=2, row=6, padx=5, pady=5, sticky="nsew")
        ttk.Button( self.root, text="=", command=lambda: self.calculate()).grid( column=3, row=6, padx=6, pady=5, sticky="nsew")
        self.root.mainloop()

    #ENGINE
    i = 0

    def get_numbers(self, n):
        self.display.insert(Calculator.i, n)
        Calculator.i+= 1

    def get_operation(self, operator):
        opertor_length = len(operator)
        self.display.insert( Calculator.i, operator)
        Calculator.i+= opertor_length

    def calculate(self):
        display_state = self.display.get()
        try:
            math_expression = parser.expr( display_state).compile()
            result = eval(math_expression)
            self.clear_display()
            self.display.insert( 0, result)
        except Exception:
            self.clear_display()
            self.display.insert( 0, 'SyntaxError')

    def clear_display(self):
        self.display.delete(0, END)

    def undo(self):
        display_state = self.display.get()
        if len(display_state):
            display_new_state = display_state[:-1]
            self.clear_display()
            self.display.insert( 0, display_new_state)
        else:
            self.clear_display()
            self.display.insert( 0, 'SyntaxError')

#MAIN BLOCK
calculator1= Calculator()