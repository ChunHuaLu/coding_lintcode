# lintcode 37
num_in = int(input())
num_reverse = i = 0
while ( num_in != 0 ):
    num_reverse = num_reverse * 10 +  num_in %10
    num_in = num_in // 10
    i+=1
    #print(str(num_in))
print(str(num_reverse))