def solution(s):
    answer = len(s)
    for unit in range(1, len(s) // 2 + 1):
        tokens = [s[index:index + unit] for index in range(0, len(s), unit)]
        prev = tokens[0]
        cnt = 1
        substring = str()
        for i in range(1, len(tokens)):
            if prev == tokens[i]:
                cnt += 1
            else:
                substring += (str(cnt) + prev) if cnt >= 2 else prev
                cnt = 1
                prev = tokens[i]
        substring += (str(cnt) + prev) if cnt >= 2 else prev
        answer = min(answer, len(substring))

    return answer