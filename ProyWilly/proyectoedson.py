from Stack import Stack
def coincide(last, simbolo):
    simbolos_apertura = '([{'
    simbolos_cierre = ')]}'

    return simbolos_apertura.index(last) == simbolos_cierre.index(simbolo)

def check(simbolo):
    stack = Stack()
    valid = True
    print(f'Operacion dada: {simbolo}')
    for i in simbolo:
        if i in '({[':
            stack.push(i)
        elif i in ')}]':
            if stack.is_empty():
                valid = False
            else:
                top = stack.pop()
                if not coincide(top, i):
                    valid = False
                else:
                    valid = True
    if not stack.is_empty():
        valid  = False
    if valid == False:

        print('Sintaxis inválida')
        return valid
    else:
        print('Sintáxis correcta')
        return valid

def notacion(infix):

    if check(infix):
        values = {}
        values['('] = 0
        values['<'] = 1
        values['>'] = 1
        values['='] = 1
        values['+'] = 2
        values['-'] = 2
        values['*'] = 3
        values['/'] = 3
        values['%'] = 3
        values['^'] = 4
        stack = Stack()
        output = []
        list = []
        for i in infix:
            if i == ' ':
                continue
            elif i not in '(+-*/)%^<>=':
                if len(output) > 0:
                    if output[-1] not in '(+-*/)%^<>=' and list[-1] not in '(+-*/)%^<>=':
                        output.pop()
                        i = list[-1] + i
                        list.pop()
                output.append(i)
                list.append(i)
            elif i == '(':
                stack.push(i)
                list.append(i)
            elif i == ')':
                top = stack.pop()
                while top != '(':
                    output.append(top)
                    top = stack.pop()
            else:
                while not stack.is_empty() and values[stack.top()] >= values[i]:
                    list.append(stack.top())
                    output.append(stack.pop())
                stack.push(i)
                list.append(i)
        while not stack.is_empty():
            list.append(stack.top())
            output.append(stack.pop())
        print('Notación Postfija: ', end='')
        return ' '.join(output)
    else:
        print('Realice bien el balanceo de símbolos porfavor')

def evaluation(postfix):
    stack = Stack()
    for i in postfix:
        if i not in '+-*/%^<>=':
            stack.push(int(i))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            resultado = resultadoOperacion(i, op1, op2)
            stack.push(resultado)
    print(f'Evaluación: ', end= '')
    return stack.pop()

def resultadoOperacion(operador, operando1, operando2):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2
    elif operador == '%':
        return operando1 % operando2
    elif operador == '^':
        return operando1 ** operando2
    elif operador == '=':
        if operando1 == operando2:
            return 1
        else:
            return 0
    elif operador == '>':
        if operando1 > operando2:
            return 1
        else:
            return 0
    elif operador == '<':
        if operando1 < operando2:
            return 1
        else:
            return 0


x = notacion("((9^5)/(8>5-2)+10)")
print(x)
print(evaluation(x.split()))
