val = {
    "*": 1,
    "/": 1,
    "+": 2,
    "-": 2,
}
def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

def calculate(left, operator, right):
    total = 0
    if operator == "*":
        total += multiply(float(left), float(right))
    if operator == "/":
        total += divide(float(left), float(right))
    if operator == "+":
        total += add(float(left), float(right))
    if operator == "-":
        total += substract(float(left), float(right))
    return total
    
def normalize(userInput):
    if not userInput or not isinstance(userInput, str):
        return userInput
    tokenize = []
    number = ''
    for c in userInput:
        if c.isdigit():
            number += c  
        else:
            if number:
                tokenize.append(number)
                number = ''
            tokenize.append(c) 
    if number:
        tokenize.append(number)
    return tokenize
    
def func(userInput):
    if not userInput:
        return None
    tokenize = normalize(userInput) if isinstance(userInput, str) else userInput
    
    if len(tokenize) == 1:
        print("Final result:", tokenize[0])
        return tokenize[0]
    
    max_prec = float('inf')
    index = -1

    for i, token in enumerate(tokenize):
        if token in val and val[token] < max_prec:
            max_prec = val[token]
            index = i
    if index == -1:
        return None 
    
    left = tokenize[index - 1]
    operator = tokenize[index]
    right = tokenize[index + 1]
    result = calculate(left, operator, right)
    tokenize = tokenize[:index - 1] + [str(result)] + tokenize[index + 2:]
    
    return func(tokenize)
                 
def getUserInput():
    equation = input("Type an equation, with no parenthesis: ")
    func(equation)
getUserInput()