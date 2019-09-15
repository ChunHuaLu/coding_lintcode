#lintcode-145
# print(str(ord('a') ) + str( ord('A')))
# lintcode 366
n = int(input())
fib_num = []
fib_num.append(0)
fib_num.append(1)
if n >= 2:
    for i in range(2,n):
        fib_num.append(fib_num[i-1] + fib_num[i-2])
print(str( fib_num[n-1] ))