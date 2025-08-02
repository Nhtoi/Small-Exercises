# def ReverseString(string):
#     string_array = []  
#     for c in string:
#         string_array.append(c)
#     reversed_string = ""
#     for i in range(len(string) - 1, -1, -1):
#         reversed_string += string[i] 
#     return reversed_string    
# print(ReverseString("Hello"))


def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Hello"))


# def sum_digits(n):
#     if n < 10:
#         return n
#     return (n % 10) + sum_digits(n // 10)

# print(sum_digits(123))