

# First test
out_1 = [17,28,30]
out_2 = [99,16,8]

# Second Test

out_3 = [5,6,7]
out_4 = [3,6,10]

def compareTriplets(a, b):
    ans = [0,0]
    for x in a:
        for y in b:    
            if x > y:
                if ans[0] > 0:
                    ans[0] = 2
                ans[0] = 1
                continue
            if x < y:
                ans[1] = 1
                continue
            if x == y:
                continue
    return ans

print(compareTriplets(out_4,out_3))

