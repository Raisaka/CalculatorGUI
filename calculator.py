

Double = []
Char = []





def Infix():
    post = ''
    InFx = Enter()
    popped = ''

    for i in range(len(InFx)):
        ch = InFx[i]
        if(isOperand(ch)):
            post += ch
        elif(ch == '('):
            Char.append(ch)
        elif(ch == ')'):
            while str(Char[-1]) != '(':
                post += str(Char[-1])
                Char.pop()
            Char.pop()
        elif(isOperator(InFx[i])):
            #print(Prescedence(InFx[i]))
            #print(str(Char[-1]))
            #print(Prescedence(Char[len - 1]))
            while isEmpty(Char) is not True and (Prescedence(InFx[i]) <= Prescedence(str(Char[-1]))):
                print('hello')
                if str(Char[-1]) == '(':
                    print('hello')
                    break
                print('hello')
                post += str(Char[-1])
                Char.pop()
            Char.append(ch)
        else:
            raise 'The expression is the wrong format'

    while isEmpty(Char) is not True:
        post += str(Char[-1])
        Char.pop()

    return post



def Enter():
    expression = input('Enter infix expression:')
    return expression
def isEmpty(list):
    if list == []:
        return True
    else:
        return False
def Prescedence(ch):
    if ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    else:
        return 0
def isOperator(ch):
    if ch == '+' or ch == '-' or ch == '*' or ch == '/':
        return True
    else:
        return False

def isOperand(character):
    if character >= '0' and character <= '9':
        return True
    else:
        return False


def doMath(opr1, opt, opr2):
    if opt == '+':
        return opr1 + opr2
    elif opt == '-':
        return opr1 - opr2
    elif opt == '*':
        return opr1 * opr2
    elif opt == '/':
        return opr1 / opr2
    else:
        print('Invalid operator')

def main():
    print("Hello World!")
    print()
    shee = Infix()
    print(shee)
if __name__ == "__main__":
    main()


