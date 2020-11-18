x=int(input())
for i in range(x):
    n=int(input())
    j=5
    count = 0
    while(n/j>=1):
        count +=int(n/j)
        j *=5
    print(count)
#submit on codechef
