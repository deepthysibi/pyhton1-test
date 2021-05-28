def avg(lst):
    n = len(lst)
    sum = 0
    for i in lst:
        r=int(i)
        sum=sum + r
    average = sum/n
    return average

print(avg([1,2,3,4,5]))

