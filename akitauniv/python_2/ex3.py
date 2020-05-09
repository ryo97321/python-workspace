input_list = []

while True:
    s = input()
    if s == 'quit':
        break
    else:
        input_list.append(s)

input_list.sort()
print(input_list)