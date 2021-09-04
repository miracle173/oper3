# oper3
Definiton of the symbol `o`

    a o b = c o d
    
means that there are binary boolean operation `o1` and `o2` such that. Every single instance of a `o` in an expression is meaning a different operator

    a o1 b = c o2 d, for all q,b,c,d in {0,1}
    
Properties

    a o b = b o a
    ( a o a ) o b = a o b
    
0-ary- and 1-ary operators expressed as binary operators:
    False (oF), True (oT), 
    left Projection/Identity (oIl), right Projection/Identity (oIr), 
    left Negation (oNl), right Negation (oNr)

      oF     oT     oIl    oIr    oNl    oNr
    a b r  a b r  a b r  a b r  a b r  a b r
    0 0 0  0 0 1  0 0 0  0 0 0  0 0 1  0 0 0
    0 1 0  0 1 1  0 1 0  0 1 1  0 1 1  0 1 0
    1 0 0  1 0 1  1 0 1  1 0 0  1 0 0  1 0 1
    1 1 0  1 1 1  1 1 1  1 1 1  1 1 0  1 1 1

Properties

    a oT b = c oT d = True
    a oF b = c oF d = False
    a oIl b = a oIl c = a
    a oIr b = a oIr c = b
    a oNl b = a oNl c = C(a) 
    a oNr b = a oNr c = C(b)
    
    a o a in {T,F,a, C(a)}
    (a o a) o b = a o b
    (a o b) o a = a o b 
    

different paranthese settings
    abcde:
    a bcde  (a(b(c(de)))) (a(b((cd)e))) (a((bc)(de))) (a((b(cd))e)) (a(((bc)d)e))
    ab cde  ((ab)(c(de))) ((ab)((cd)e))
    abc de  ((a(bc))(de)) (((ab)c)(de))
    abcd e  ((a(b(cd)))e) ((a((bc)d))e) (((ab)(cd))e) (((a(bc))d)e) ((((ab)c)d)e)
    
    rstu: (r(s(tu))) (r((st)u)) ((rs)(tu)) ((r(st))u) (((rs)t)u)
    r stu (r(s(tu)))  (r((st)u))
    rs tu ((rs)(tu))
    rst u ((r(st))u)  (((rs)t)u)
    
    xyz: (x(yz)) ((xy)z)
    x yz (x(yz))
    xy z ((xy)z)
    
    mn: (mn)
    m n: (mn)    
