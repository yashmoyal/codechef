x=int(input())
while(x !=0):
    pearls=str(input())
    minestone=str(input())
    count=0
    for k in minestone:
        if(k in pearls):
            count +=1
    print(count)
    x -=1
    #submit on codechef