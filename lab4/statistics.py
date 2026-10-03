a=0
b=0
c=-1000000
for i in range(int(input())):
 s=int(input())
if c>0:
 a+=1
 b+=s
c=max(c,s)
print(a, b, c)
