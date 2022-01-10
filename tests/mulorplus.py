str = input()
sum = 0
if str[0] =='0' or str[0] == '1' or str[1] == '0' or str[1] == '1':
    sum += int(str[0]) + int(str[1])
else:
    sum += int(str[0]) * int(str[1])

if len(str) >=2:
    for i in str[2:]:
        num = int(i)
        if num == 0 or num == 1:
            sum +=num
        else:
            sum *=num

print(sum)