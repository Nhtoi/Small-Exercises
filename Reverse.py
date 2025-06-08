def ReverseString(string):
    string_array = []  
    for c in string:
        string_array.append(c)
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i] 
    return reversed_string    
print(ReverseString("Hello"))