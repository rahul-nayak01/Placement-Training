
x=int(input())
y=int(input())
z=int(input())
n=int(input())




output=[[i,j,k] for i in range(x+1) for j in range(y+1) for k i in range(z+1) if i+j+k!=n]
print(output)

#next

if __name__=='__main__':
n=int(input())
arr=map(int,input().split())
run_up=list(set(arr))
run_up.sort()
print(run_up[-2])