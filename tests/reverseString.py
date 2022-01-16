string = str(input())
cnt_one = 0
cnt_zero = 0
if string[0] == '1':
    cnt_one += 1
else:
    cnt_zero +=1
for i in range(1,len(string)):
    if string[i] == string[i-1]:
        continue
    if string[i] == '1':
        cnt_one +=1
    else:
        cnt_zero +=1
print(min(cnt_one,cnt_zero))
