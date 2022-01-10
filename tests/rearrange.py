string = input()
sorted_str = sorted(string)
answer = str()
sum = 0
index = 0
for i in sorted_str:
    if i.isnumeric() == True:
        sum += int(i)
        index += 1
    else:
        break
for i in sorted_str[index:]:
    answer+=i
print(answer+str(sum))

