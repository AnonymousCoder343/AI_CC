data = [-2, 45, 0, 11, -9]
for i in range(len(data)):
    temp=i
    for j in range(i+1,len(data)):        
        if data[i]>data[j]:
            temp=j
    data[i],data[temp]=data[temp],data[i]
print(data)