k = list(")(")
stack = []
f = True

for el in k:
    if el == '(':
        stack.append('(')
    elif stack:
        stack.pop()
    else:
        print("Нельзя убрать из пустого стека")
        f = False
        break

if f:
    if stack:
        print(stack)
        print("неправильная")
    else:
        print("правильная")

