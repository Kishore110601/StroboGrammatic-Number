'''      StroboGrammatic Number      '''
a=input()
b=['8','1','0']
c=0
for i in range(0,len(a)//2):
    if (a[i] in b and a[i]==a[len(a)-i-1]) or ((a[i]=='6' and a[len(a)-i-1]=='9') or (a[i]=='9' and a[len(a)-i-1]=='6')):
            c+=2
            print(c,i)
if len(a)%2==1 and a[len(a)//2] in b:
    c+=1
if c==len(a):
    print("YES")
else:
    print("NO")
print(c,len(a))
