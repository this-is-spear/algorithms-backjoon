doc = input()
search_str = input()
index = 0
result = 0

while index < len(doc):
    if search_str == doc[index:index + len(search_str)]:
        result += 1
        index += len(search_str) - 1
    index += 1

print(result)