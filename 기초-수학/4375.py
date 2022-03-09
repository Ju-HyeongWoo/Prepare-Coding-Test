from operator import truediv

n = int(input())
x = 1
a = 1
m = 1
while m != 0:
    for i in range(x):
        a += 10 ** i
        m = a % n
        x += 1
    print(x)

    
    
                     # a 를 n으로 나누어서 나머지가 0이 아니면 i를 1씩 증가
                                # a 를 n으로 나누어서 나머지가 0이면 i를 출력

    