# oper3
Definiton of the symbol `o`

    a o b = c o d
    
means that there are binary boolean operation `o1` and `o2` such that. Every single instance of a `o` in an expression is meaning a different operator

    a o1 b = c o2 d, for all q,b,c,d in {0,1}
    
Properties

    a o b = b o a
    ( a o a ) o b = a o b
    
0-ary- and 1-ary operators expressed as binary operators:
    False (`oF`), True (`oT`), 
    left Projection/Identity (`oIl`), right Projection/Identity (`oIr`), 
    left Negation (`oNl`), right Negation (`oNr`)

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

    vwxyz:
    v wxyz  (v(w(x(yz)))) (v(w((xy)z))) (v((wx)(yz))) (v((w(xy))z)) (v(((wx)y)z))
    vw xyz  ((vw)(x(yz))) ((vw)((xy)z))
    vwx yz  ((v(wx))(yz)) (((vw)x)(yz))
    vwxy z  ((v(w(xy)))z) ((v((wx)y))z) (((vw)(xy))z) (((v(wx))y)z) ((((vw)x)y)z)
    
    wxyz: (w(x(yz))) (w((xy)z)) ((wx)(yz)) ((w(xy))z) (((wx)y)z)
    w xyz (w(x(yz)))  (w((xy)z))
    wx yz ((wx)(yz))
    wxy z ((w(xy))z)  (((wx)y)z)
    
    xyz: (x(yz)) ((xy)z)
    x yz (x(yz))
    xy z ((xy)z)
    
    yz: (yz)
    y z: (yz)    
 
 
 reducing the cases
 
 three variables
 
    (x(yz))
    if |{w,x,y,z}|<3 then (x(yz)) = (uv), where {uv}={w,x,y,z}|, which is already processed
    (a(bc)) -> new
    ((xy)z)=(z(xy))~(x(yz))
  so the only case is (a(bc))
 
 four variables
 
    (w(x(yz))) 
    if |{w,x,y,z}|<3 then (w(x(yz))) = (uv), where {uv}={w,x,y,z}|, which is already processed
    so |{w,x,y,z}|=3
    (a(a(...)))=(a(...)) shorter
    (a(b(ac)) -> new 
    (a(b(bz))=(a(bz)),  shorter
    (a(b(cz)))=)(a(b(zc)), for z in {a,b}, already processed
    (a(b(cc)))=(a(bc)), shorter
    (a,c,...)~(a,b,...)) relabeling
    (w,...)~(a,...), w in {b,c},relabelling



    (w((xy)z))
    (w((xy)z))=(w(z(xy))~(w(y(yz)), already processed

    ((wx)(yz))
    if |{w,x,y,z}|<3 then ((wx)(yz)) = (uv), where {uv}={w,x,y,z}|, which is already processed
    so |{w,x,y,z}|=3
    ((aa)...)=(a...), shorter
    ((ab)(ac)) -> new
    ((ab)(bc)~((ba)(ac))=((ab)(ac), already processed
    ((ac)...)~((ab)...), relabeling
    ((b....)~((a....),relabeling
    ((c....)~((a....),relabeling

    ((w(xy))z)=(z(w(xy)))~(w(x(yz))), already processed 
    (((wx)y)z)=(z(y(wx)))~(w(x(yz))), already processed 

so the only cases are

    (a(b(ac))) 
    ((ab)(ac))
