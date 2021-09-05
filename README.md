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
    
    xy
    (xy)
    
    
    xyz
    (x(yz))

    wxyz
    (w(x(yz)))
    ((wx)(yz))

    vwxyz

    (v(w(x(yz))))
    (v((wx)(yz)))
    ((vw)(x(yz)))

    uvwxyz
    (u(v(w(x(yz)))))
    (u(v((wx)(yz))))
    (u((vw)(x(yz))))
    ((uv)(w(x(yz))))
    ((uv)((wx)(yz)))
    ((u(vw))(x(yz)))



    yz::
    (yz):
    (ab)
    
    xyz::
    (x(yz)):
    (a(bc))
    
    wxyz::
    (w(x(yz))):
    (a(b(ac)))
    
    ((wx)(yz)):
    ((ab)(ac))
    ((ab)(bc))
    
    vwxyz::
    (v(w(x(yz)))):
    (a(b(a(bc))))
    (a(b(c(ab))))
    
    (v((wx)(yz))):
    (a((ab)(ac)))
    (a((ab)(bc)))
    
    ((vw)(x(yz))):
    ((ab)(a(bc)))
    ((ab)(b(ac)))
    ((ab)(c(ab)))
    
    uvwxyz::
    (u(v(w(x(yz))))):
    (a(b(a(b(ac)))))
    (a(b(a(c(ab)))))
    (a(b(c(a(bc)))))
    (a(b(c(b(ac)))))

    (u(v((wx)(yz)))):
    (a(b((ab)(ac))))
    (a(b((ab)(bc))))

    (u((vw)(x(yz)))):
    (a((ab)(a(bc))))
    (a((ab)(b(ac))))
    (a(bc)(b(ac)))))
    (a(bc)(c(ab)))))

    ((uv)(w(x(yz)))):
    ((ab)(a(b(ac))))
    ((ab)(a(c(ab))))
    ((ab)(b(a(bc))))
    ((ab)(b(c(ab))))
    ((ab)(c(a(bc))))
    ((ab)(c(b(ac))))

    ((uv)((wx)(yz))):
    ((ab)((ac)(bc)))

    ((u(vw))(x(yz))):
    ((a(bc))(b(ac)))
    ((a(bc))(c(ab)))
    
the six relabeling permutations

    n  x y z v     x z y v     y x z v 
    0  0 0 0 v0    0 0 0 v0    0 0 0 v0
    1  0 0 1 v1    0 0 1 v2    0 0 1 v1
    2  0 1 0 v2    0 1 0 v1    0 1 0 v4
    3  0 1 1 v3    0 1 1 v3    0 1 1 v5
    4  1 0 0 v4    1 0 0 v4    1 0 0 v2
    5  1 0 1 v5    1 0 1 v6    1 0 1 v3
    6  1 1 0 v6    1 1 0 v5    1 1 0 v6
    7  1 1 1 v7    1 1 1 v7    1 1 1 v7
       
    n  y z x v     z x y v     z y x v 
    0  0 0 0 v0    0 0 0 v0    0 0 0 v0
    1  0 0 1 v4    0 0 1 v2    0 0 1 v4
    2  0 1 0 v1    0 1 0 v4    0 1 0 v2
    3  0 1 1 v5    0 1 1 v6    0 1 1 v6
    4  1 0 0 v2    1 0 0 v1    1 0 0 v1
    5  1 0 1 v6    1 0 1 v3    1 0 1 v5
    6  1 1 0 v3    1 1 0 v5    1 1 0 v3
    7  1 1 1 v7    1 1 1 v7    1 1 1 v7
    
    
    ((((((2*v[7]+v[6])*2+v[5])*2+v[4])*2+v[3])*2+v[2])*2+v[1])*2+v[0]
    ((((((2*v[7]+v[5])*2+v[6])*2+v[4])*2+v[3])*2+v[1])*2+v[2])*2+v[0]
    ((((((2*v[7]+v[6])*2+v[3])*2+v[2])*2+v[5])*2+v[4])*2+v[1])*2+v[0]
    ((((((2*v[7]+v[3])*2+v[6])*2+v[2])*2+v[5])*2+v[1])*2+v[4])*2+v[0]
    ((((((2*v[7]+v[5])*2+v[3])*2+v[1])*2+v[6])*2+v[4])*2+v[2])*2+v[0]
    ((((((2*v[7]+v[3])*2+v[5])*2+v[1])*2+v[6])*2+v[2])*2+v[4])*2+v[0]    
