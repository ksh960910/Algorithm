num = int(input())
x = list()
for i in range(num):
    a, b = map(int, input().split(' ' ))
    x.append(a+b)
for i in range(num):
    print('Case #'+str(i+1)+':', x[i])