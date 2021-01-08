a = int(input())
b = int(input())


for i in range(a,b+1):
    oreginal_num = 0
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
            oreginal_num = i
    print(oreginal_num,count)