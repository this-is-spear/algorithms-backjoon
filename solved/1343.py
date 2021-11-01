a = input().split(".")
answer = ""
for i in a:
    if i.count("X") % 2 != 0 and i.count("X") != 0:
        answer = "-1"
        break
    else:
        if i.count("X")//4:
            answer += "AAAA" * (i.count("X")//4)
            i = i[4*(i.count("X") // 4):]
        if i.count("X")//2:
            answer += "BB"
        answer += "."
print(answer[:-1] if answer[-1] == "." else answer)
