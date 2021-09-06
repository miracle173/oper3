from itertools import product, permutations
from time import time
binops=list(product([0,1], repeat=4))
arg=list(product([0,1],repeat=3))
o3=[0]*256
o4=[0]*256



a=[[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1]]

def create_oplist():
    return [0]*256

def idx(termresult):
    myresult=reversed(termresult)
    acc=0
    for bit in myresult:
        acc=2*acc+bit
    return(acc)

def calc(arg1,arg2,oper):
    return([oper[arg1[i]+2*arg2[i]] for i in range(len(arg1))])


def calc_perm_idx(bit,perm):
    s=0
    for i in range(8):
        s*=2
        s+=bit[perm[7-i]]
    return s

def calc_bit_list(n):
    v=[]
    for i in range(8):
        v.append(n%2)
        n//=2
    return v

def apply_permute(idx,oplist):
    if oplist[idx]==0:
        return
    v=calc_bit_list(idx)
    # apply relabeling
    oplist[calc_perm_idx(v,[0,2,1,3,4,6,5,7])]=1
    oplist[calc_perm_idx(v,[0,1,4,5,2,3,6,7])]=1
    oplist[calc_perm_idx(v,[0,4,1,5,2,6,3,7])]=1
    oplist[calc_perm_idx(v,[0,2,4,6,1,3,5,7])]=1
    oplist[calc_perm_idx(v,[0,4,2,6,1,5,3,7])]=1
    return oplist

def adjust_oplist(oplist):
    for i in range(len(oplist)):
        apply_permute(i,oplist)
    return oplist

def print_ops(oplist):
    print([0,0,0,0,1,1,1,1])
    print([0,0,1,1,0,0,1,1])
    print([0,1,0,1,0,1,0,1])
    print(" -  -  -  -  -  -  -  -")
    for i in range(len(oplist)):
        if oplist[i]==1:
            print(calc_bit_list(i),i)
    print(sum(oplist))

def run_var1(oplist):
    for op1 in binops:
        result=calc(a[0],a[0],op1)
        oplist[idx(result)]=1
    return oplist

def run_var2(oplist):
    for op1 in binops:
        result=calc(a[0],a[1],op1)
        oplist[idx(result)]=1
    return oplist

def run_var3(oplist):
    for op1 in binops:
        for op2 in binops:
            result=calc(a[0],calc(a[1],a[2],op1),op2)
            oplist[idx(result)]=1
    return oplist

def run_var4(oplist):
    for op1 in binops:
        for op2 in binops:
            for op3 in binops:
                result=calc(a[0],calc(a[1],calc(a[0],a[2],op1),op2),op3)              
                oplist[idx(result)]=1
                result=calc(calc(a[0],a[1],op1),calc(a[0],a[2],op2),op3) 
                oplist[idx(result)]=1 
                result=calc(calc(a[0],a[1],op1),calc(a[1],a[2],op2),op3) 
                oplist[idx(result)]=1 
    return oplist

def run_var5(oplist):
    for op1 in binops:
        for op2 in binops:
            for op3 in binops:
                for op4 in binops:
                    result=calc(a[0],calc(a[1],calc(a[0],calc(a[1],a[2],op1),op2),op3),op4)   
                    oplist[idx(result)]=1
                    result=calc(a[0],calc(a[1],calc(a[2],calc(a[0],a[1],op1),op2),op3),op4)   
                    oplist[idx(result)]=1
                    result=calc(a[0],calc(calc(a[0],a[1],op1),calc(a[0],a[2],op2),op3),op4)
                    oplist[idx(result)]=1 
                    result=calc(a[0],calc(calc(a[0],a[1],op1),calc(a[1],a[2],op2),op3),op4)
                    oplist[idx(result)]=1 
                    result=calc(calc(a[0],a[1],op1),calc(a[0],calc(a[1],a[2],op2),op3),op4) 
                    oplist[idx(result)]=1 
                    result=calc(calc(a[0],a[1],op1),calc(a[1],calc(a[0],a[2],op2),op3),op4) 
                    oplist[idx(result)]=1 
                    result=calc(calc(a[0],a[1],op1),calc(a[2],calc(a[0],a[1],op2),op3),op4) 
                    oplist[idx(result)]=1            
    return oplist
def run_test():
    start_time=time()
    first_start_time=start_time
    oplist=create_oplist()
    oplist=run_var1(oplist)
    oplist=adjust_oplist(oplist)
    print_ops(oplist)
    end_time=time()
    print(end_time-start_time,end_time-first_start_time)
    start_time=end_time
    print()
    oplist=run_var2(oplist)
    oplist=adjust_oplist(oplist)
    print_ops(oplist)
    end_time=time()
    print(end_time-start_time,end_time-first_start_time)
    start_time=end_time
    print()
    oplist=run_var3(oplist)
    oplist=adjust_oplist(oplist)
    print_ops(oplist)
    end_time=time()
    print(end_time-start_time,end_time-first_start_time)
    start_time=end_time
    print()
    oplist=run_var4(oplist)
    oplist=adjust_oplist(oplist)
    print_ops(oplist)
    end_time=time()
    print(end_time-start_time,end_time-first_start_time)
    start_time=end_time
    print()
    oplist=run_var5(oplist)
    oplist=adjust_oplist(oplist)
    print_ops(oplist)
    end_time=time()
    print(end_time-start_time,end_time-first_start_time)

def parse(expr):
    result=[]
    


def list_assoc(vars=None,expressionList=None):
    if expressionList is None:
        # initial call of function
        if not vars:
            raise ValueError("vars is empty or not given")
        return(list_assoc(None,[vars]))

    assert(vars is None)
    #print("enter:"+str(expressionList))
    newExpressionList=[]
    for expr in expressionList:
        if len(expr)<1:
            raise ValueError("invalid length of expr: '"+expr+"'")
        elif len(expr)==1:
            newExpressionList.append(expr)
        elif len(expr)==2:
            newExpressionList.append("("+expr+")")
        else:
            for n in range(1,len(expr)):
                #print(n,expr,expr[:n],list_assoc(None,expr[:n]),expr[n:],list_assoc(None,expr[n:]))
                exprlst=["("+t[0]+t[1]+")" for t in product(list_assoc(None,[expr[:n]]),
                    list_assoc(None,[expr[n:]]))]
                newExpressionList.extend(exprlst)
    #print("leave:"+str(newExpressionList))
    return(newExpressionList)

def test_t1():
    n=idx([0,0,0,0,1,1,1,1])
    print(n)

def test_t2(vv):
    o3=o4[:]
    o3[idx(vv)]=1
    apply_permute(idx(vv),o3)
    return sum(o3)


run_test()


