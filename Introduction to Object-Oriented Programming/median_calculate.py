arr = [130, 132, 135, 140, 142, 150, 158, 160]

def median_calculate(arr):
    median_value = 0.0
    arr.sort()
    n = len(arr)
    if (n % 2 == 0):
        print(f"List is Even: {n}")
        pos_1 = int(n / 2)
        pos_2 = int((n / 2) + 1)
        median_value = (arr[pos_1 - 1] + arr[pos_2 - 1]) / 2
        return (f"Median Value: {median_value}")
    else:
        print(f"List is Odd:{n}")
        median_value = int((n + 1) / 2)
        return(f"Median Value: {arr[median_value - 1]}")

test = median_calculate(arr)
print(test)