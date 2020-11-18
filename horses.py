x=int(input())
while(x !=0):
    y=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    r=lst[1]
    for i in range(1,y):
            if(r<lst[i]-lst[i-1]):
                r=lst[i]-lst[i-1]
    print(r)
    x -=1
    #submit on codechef