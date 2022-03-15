a, b = map(int,input().split())
c = int(input())
m = 0 
if b + c >= 60:
    m = (b + c) % 60
    a = a + (b + c) // 60
    if a >= 24:
        a = a % 24
    print(a, m)
else:
    m = b + c
    print(a, m)