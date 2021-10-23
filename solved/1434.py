input()
box = list(map(int, input().split()))
book = list(map(int, input().split()))
answer = 0
while book:
    book_pop = book.pop(0)
    while box:
        box_pop = box.pop(0)
        if book_pop > box_pop:
            answer += box_pop
        else:
            box.insert(0, box_pop-book_pop)
            break
else:
    answer += sum(box)
print(answer)