
import sys
# exec(int(input())*"print(\"Case #1:\", sum(map(int, sys.stdin.readline().split())));")

for i in range(int(input())):
    print("Case #"+str(i+1)+": "+str(sum(map(int, input().split()))))
