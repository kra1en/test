n=int(input())
a=[[0 for i in range(n)] for j in range(n)]
i,j = input().split()
a[j][i]+=1
print(a)