x=int(input())
while(x !=0):
    ncars=int(input())
    lst=list(map(int,input().split()))
    r=lst[0]
    count = 1
    for i in lst[1:]:
        if(r>=i):
            r=i
            count +=1
    print(count)
    x -=1
 # submit on codechef