import math
p=0.54
n=4
ans=0
for i in range(n,2*n-1):
    k=math.comb(i-1,n-1)*p**n*(1-p)**(i-n)
    ans+=k
    print(i,k)

print()

for i in range(n,2*n-1):
    k=math.comb(i-1,n-1)*(1-p)**n*(p)**(i-n)
    ans+=k
    print(i,k)

print(ans)
ans+=(1-p)**(n-1)*p**(n-1)*math.comb(2*n-2,n-1)
print(ans)