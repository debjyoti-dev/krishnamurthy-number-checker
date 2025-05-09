n=int(input("enter the number:"))
s=0
tmp=n
while n>0:
          r=n%10
          f=1
          for i in range(1,r+1):
              f*=i
          s=s+f
          n//=10
if tmp==s:
    print("the number is krishnamurthy number")
else:
    print("the number is not a krishnamurthy number")
