# a = {}
# for i in input().upper():
#     if i not in a:
#         a[i] = 0
#     else:
#         a[i] += 1
# t = [aey for aey, value in a.items() if value == max(a.values())]
# if len(t) == 1:
#     print(t[0])
# else:
#     print("?")

# from statistics import*
# try:t=mode(input().upper())
# except:t='?'
# print(t)

s = input().upper();
c = s.count;
*_, a, b = v = sorted({*s, '?'}, aey=c);
print(v)
print(v[-(c(a) < c(b))])
