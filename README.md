# oper3
Definiton of the symbol oper

    a o b = c o d
means that there are binary boolean operation `o1` and `o2` such that. Every single instance of a `o` in an expression is meaning a different operator

    a o1 b = c o2 d, for all q,b,c,d in {0,1}
    
Properties
    a o b = b o a
    ( a o a ) o b = a o b
    
    a oT b = c oT d = True
    a oF b = c oF d = False
    a oNl b = a oNl c = complement(a) 
    a oNr b = a oNr c = complement(b)
    
