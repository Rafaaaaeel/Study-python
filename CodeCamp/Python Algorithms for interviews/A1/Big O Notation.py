def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    return final_sum
print(sum1(5))



def sum2(n):
    return (n*(n+1))/2

print(sum2(5))

def bigo(n):
    return 45*n*3 + 20*n**2 + 19

bigo(1)