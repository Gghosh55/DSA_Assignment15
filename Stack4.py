def reverseStack(St):
    if not St:
        return

    topElement = St.pop()
    reverseStack(St)
    insertAtBottom(St, topElement)


def insertAtBottom(St, item):
    if not St:
        St.append(item)
        return

    topElement = St.pop()
    insertAtBottom(St, item)
    St.append(topElement)



stack = [3,2,1,7,6]
print("Original stack:", stack)

reverseStack(stack)
print("Reversed stack:", stack)
