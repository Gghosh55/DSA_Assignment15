def reverseString(S):
    stack = []


    for char in S:
        stack.append(char)

    reversed_string = ""


    while stack:
        reversed_string += stack.pop()

    return reversed_string
input_string = "GeeksforGeeks"
reversed_string = reverseString(input_string)
print(reversed_string)
