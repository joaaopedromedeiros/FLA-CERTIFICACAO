n = 5
ls = [None] * n


for i in range(n):#1,2,3,4,5
    ls.append(1) #add


ls[0] = 5
ls[3] = -3

print(ls)

# [5, None, None, -3, None,1,1,1,1,1]