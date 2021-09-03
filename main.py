from itertools import product, permutations
from time import time
binops=list(product([0,1], repeat=4))
arg=list(product([0,1],repeat=3))
o3=[0]*256
o4=[0]*256

a=[[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1]]

def idx(termresult):
    myresult=reversed(termresult)
    acc=0
    for bit in myresult:
        acc=2*acc+bit
    return(acc)
#def cmp(v1,v2,o)
def calc(arg1,arg2,oper):
    return([oper[arg1[i]+2*arg2[i]] for i in range(len(arg1))])
'''
for op1 in binops:
    for op2 in binops:
         result=calc(a[0],calc(a[1],a[2],op2),op1)
         o3[idx(result)]=1
print(sum(o3))

for op1 in binops:
    for op2 in binops:
        for op3 in binops:
            result=calc(calc(a[0],a[1],op1),calc(a[0],a[2],op3),op2)
            o4[idx(result)]=1
print(sum(o4))
print( [(o4[i]-o3[i]) for i in range(len(o3))])
'''
for op1 in binops:
    for op2 in binops:
        result=calc(a[0],calc(a[1],a[2],op1),op2)
        o3[idx(result)]=1
print(sum(o3))

for op1 in binops:
    for op2 in binops:
        result=calc(calc(a[0],a[1],op2),a[2],op1)
        o4[idx(result)]=1


print(sum(o4))
diff= [(o4[i]-o3[i]) for i in range(len(o3))]
print(diff)


''''
start=time()
for p in [[0,1,2]]:
    for op1 in binops:
        result=calc(a[0],calc(a[p[0]],a[p[1]],op1),[0,1,1,1])
        if o3[idx(result)] == 0:
            o3[idx(result)]=1
            print(result,idx(result))

        #o3[idx(calc(a[p[0]],calc(a[p[1]],a[p[2]],[0,1,1,1]),op1))]=1
print(time()-start)
print(sum(o3))
'''

''''
start=time()
for p in product([0,1,2], repeat=3):
    for op1 in binops:
        for op2 in binops:
            result=calc(calc(a[p[0]],a[p[1]],op1),a[p[2]],op2)
            o3[idx(result)]=1
            result=calc(a[p[0]],calc(a[p[1]],a[p[2]],op1),op2)
            o3[idx(result)]=1
print(time()-start)
print(sum(o3))

start=time()
for p in product([0,1,2], repeat=4):
    if p[:3]!=[0,1,2] or p[:3]!=[0,0,1]  or p[:3]!=[0,0,0]:
        continue
    for op1 in binops:
        for op2 in binops:
            for op3 in binops:
                #(((a0+a1)+a2)+a3)
                result=calc(calc(calc(a[p[0]],a[p[1]],op1),a[p[2]],op2),a[p[3]],op3)
                o3[idx(result)]=1
                #((a0+a1)+(a2+a3))
                result=calc(calc(a[p[0]],a[p[1]],op1),calc(a[p[2]],a[p[3]],op1),op3)
                o3[idx(result)]=1
                #((a0+(a1+a2))+a3)
                result=calc(calc(a[p[0]],calc(a[p[1]],a[p[2]],op1),op2),a[p[3]],op3)
                o3[idx(result)]=1
                #(a0+((a1+a2)+a3))
                result=calc(a[p[0]],calc(calc(a[p[1]],a[p[2]],op1),a[p[3]],op2),op3)
                o3[idx(result)]=1
                #(a0+(a1+(a2+a3)))
                result=calc(a[p[0]],calc(a[p[1]],calc(a[p[2]],a[p[3]],op1),op2),op3)
                o3[idx(result)]=1
print(time()-start)
print(sum(o3))

ll=list(product([0,1], repeat=8))
for i in range(len(o3)):
    if o3[i]==0:
        print(i,ll[i])
'''
'''
++xx+xx
+++xxxx
+x++xxx
+x+x+xx
++x+xxx


+ +xx x
+ x +xx
+ ++xxx x

+ +xx +xx

+ x ++xxx

+ ++xxx x

+ + +xx x x

+ + x +xx x
'''

