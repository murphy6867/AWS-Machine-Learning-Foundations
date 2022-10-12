import math

arr = [600, 470, 170, 430, 300]

def mean(arr):
    sum = 0
    count = 0
    for i in arr:
        count += 1
        sum = sum + int(i)
    return (sum / count)

def stdev(arr):
    mu = mean(arr)
    var = []
    var_2 = 0.0
    n = 0
    for i in arr:
        var.append(i - mu)
    
    for i in var:
        n += 1
        var_2 = var_2 + (i * i)
    return(math.sqrt(var_2 / n))
    
#test = stdev()
print(stdev(arr))