def func(array):

    stack = []
    if len(stack) == 1:
        return stack
    else:
        for num in array:
            if num != "+" and num != "-" and num != "/" and num != "*": 
                stack.append(int(num))
                print(stack)
            else:
                print(num)
                if num ==  "+":
                    print(stack)
                    right = stack.pop(-1)
                    left = stack.pop(-1)
                    result = left + right
                    stack.append(result)
                if num ==  "-":
                    print(stack)
                    right = stack.pop(-1)
                    left = stack.pop(-1)
                    result = left - right
                    stack.append(result)
                if num ==  "*":
                    print(stack)
                    right = stack.pop(-1)
                    left = stack.pop(-1)
                    result = left * right
                    stack.append(result)
                if num ==  "/":
                    print(stack)
                    right = stack.pop(-1)
                    left = stack.pop(-1)
                    result = int(left / right)
                    stack.append(result)
    return stack

print(func(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))