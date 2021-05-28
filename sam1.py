name = input('enter the name :')
x = 'haii'+name
print(x)
with open("coptfile.txt","w") as f:
    f.write('print(x)')
