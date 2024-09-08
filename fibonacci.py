def fibo(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num -2)
for i in range (5):
    print(i, end = ' ')
    print(fibo(i))
