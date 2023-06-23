def find_nearest_smaller_elements(a):
    n = len(a)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] >= a[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(a[i])

    return result
a = [1,6,2]
print(find_nearest_smaller_elements(a))
