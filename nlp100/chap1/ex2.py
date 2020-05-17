s = 'パタトクカシーー'

result1 = ''
result2 = ''

for i in range(len(s)):
    if i % 2 == 0:
        result1 += s[i]
    elif i % 2 == 1:
        result2 += s[i]

print(result1)
print(result2)