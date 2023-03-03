import math
import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Cool Calculator")

        self.total_expression = "" #total will start off blank
        self.current_expression = "" #current will start of blank as well

        self.display_frame = self.create_display_frame() # call create frame

        self.total_label, self.label = self.create_display_labels() ## makes labels

        #used for the calculator buttons and where they are placed on the frame top to bottom
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.':(4, 1)
        }
        #these are for the operation button symbols and what they will do division, multi, add, sub
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()#create the buttons frames

        #will make each button spaced nicely rows and columns
        self.buttons_frame.rowconfigure(0, weight = 1)
        for x in range (1,5):
            self.buttons_frame.rowconfigure(x, weight = 1)
            self.buttons_frame.columnconfigure(x, weight = 1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.keyboard()
    def keyboard(self):
        self.window.bind("<Return>", lambda event: self.equals())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(str(key), lambda event, operator = key: self.append_operator(operator))
    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_squareroot_button()
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, anchor = tk.E, bg = LIGHT_GRAY, fg = LABEL_COLOR, padx = 24, font = SMALL_FONT_STYLE)
        total_label.pack(expand = True, fill = "both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label
    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221, bg = LIGHT_GRAY)
        frame.pack(expand = True, fill = "both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg = WHITE, fg = LABEL_COLOR, font = DIGIT_FONT_STYLE,
                               borderwidth = 0, command = lambda x = digit: self.add_to_expression(x))
            button.grid(row = grid_value[0], column = grid_value[1], sticky = tk.NSEW)
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = OFF_WHITE, fg = LABEL_COLOR, font = DEFAULT_FONT_STYLE,
                               borderwidth = 0, command = lambda x = operator: self.append_operator(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i += 1


    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_total_label()
        self.update_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_squareroot_button(self):
        button = tk.Button(self.buttons_frame, text='√', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.squareroot)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    def squareroot(self):
        self.total_expression = '√(' + self.current_expression + ')'
        self.update_total_label()

        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text='x\u00b2', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW)
    def square(self):
        #self.total_expression = '√(' + self.current_expression + ')'
        #self.update_total_label()

        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def equals(self):
        self.total_expression += self.current_expression #take the whole expression at once "89+42"
        self.update_total_label()#update total label
        try:
            # eval takes an expression string and evaluates it, then make the answer the current expression
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""  # update total to a blank string
        except Exception as e:#if theres an error like div by 0 then exception
           self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command = self.equals)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame

    #updates the total label on the calc, anytime the total should change
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text = expression)

    #updates the current label on the calc, should be called any time a button is pressed
    def update_label(self):
        self.label.config(text = self.current_expression[:11])#stops after 11 places

    def run(self):
        self.window.mainloop()

#########################
#IGNORE, REEEEEE
# Double = [] #stores floating numbers for calculating
# Char = [] #stores characters
#
#
#
# def Post(exp):
#     #variables we will use in the function
#     num = 0.0
#     left = 0.0
#     right = 0.0
#     ans = 0.0
#     full = False
#
#     for i in range(len(exp)):
#         #full = False
#         if(isOperator(exp[i])):
#             right = float(Double[-1])
#             if(len(Double) != 0):
#                 Double.pop()
#             else:
#                 print("Can't pop")
#             if(len(Double) != 0):
#                 left = float(Double[-1])
#                 Double.pop()
#                 ans = doMath(left, exp[i], right)
#                 Double.append(ans)
#             else:
#                 raise TypeError('The expression is in the wrong format!', left, 'Not enough operands')
#                 #full = True
#                 break
#         elif(isOperand(exp[i])):
#             num = float(exp[i])
#             # print('this is before going into the stack ')
#             # print(num)
#             Double.append(num)
#     answer = 0
#     while full is False:
#         answer = float(Double[-1])
#         if(len(Double) != 0):
#             Double.pop()
#         else:
#             print('Cant pop')
#         if(len(Double) != 0):
#             raise OverflowError('The expression is too long', answer)
#             full = True
#         else:
#             full = True
#     # print('This is the answer')
#     # print(answer)
#     return answer
#
#
#
# def Infix():
#     post = ''
#     InFx = Enter()
#     popped = ''
#
#     for i in range(len(InFx)):
#         ch = InFx[i]
#         if(isOperand(ch)):
#             post += ch
#         elif(ch == '('):
#             Char.append(ch)
#         elif(ch == ')'):
#             while str(Char[-1]) != '(':
#                 post += str(Char[-1])
#                 Char.pop()
#             Char.pop()
#         elif(isOperator(InFx[i])):
#             #print(Prescedence(InFx[i]))
#             #print(str(Char[-1]))
#             #print(Prescedence(Char[len - 1]))
#             while isEmpty(Char) is not True and (Prescedence(InFx[i]) <= Prescedence(str(Char[-1]))):
#                 #print('hello')
#                 if str(Char[-1]) == '(':
#                     #print('hello')
#                     break
#                 #print('hello')
#                 post += str(Char[-1])
#                 Char.pop()
#             Char.append(ch)
#         else:
#             raise TypeError("The expression is in the wrong format", ch)
#
#     while isEmpty(Char) is not True:
#         post += str(Char[-1])
#         Char.pop()
#
#     return post
#
#
#
# def Enter():
#     expression = input('Enter infix expression:')
#     return expression
# def isEmpty(list):
#     if list == []:
#         return True
#     else:
#         return False
# def Prescedence(ch):
#     if ch == '*' or ch == '/':
#         return 2
#     elif ch == '+' or ch == '-':
#         return 1
#     else:
#         return 0
# def isOperator(ch):
#     if ch == '+' or ch == '-' or ch == '*' or ch == '/':
#         return True
#     else:
#         return False
#
# def isOperand(character):
#     if character >= '0' and character <= '9':
#         return True
#     else:
#         return False
#
#
# def doMath(opr1, opt, opr2):
#     # print("This is opr1")
#     # print(opr1)
#     # print('This is opr2')
#     # print(opr2)
#     ans = 0
#     if opt == '+':
#         ans = opr1 + opr2
#         return ans
#     elif opt == '-':
#         ans = opr1 - opr2
#         return ans
#     elif opt == '*':
#         ans = opr1 * opr2
#         return ans
#     elif opt == '/':
#         ans = opr1 / opr2
#         return ans
#     else:
#         print('Invalid operator')
#
# def main():
#     # print("Hello World!")
#     # print()
#     try:
#         shee = Infix()
#         print(shee)
#         result = Post(shee)
#         print('This is the result')
#         print(result)
#     except TypeError as UF:
#         print(UF.args)
#     except OverflowError as OF:
#         print(OF.args)
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    #main()


