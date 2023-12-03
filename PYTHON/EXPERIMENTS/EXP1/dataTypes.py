a = "hello world"
print('\nStrings implemenation : ',a,type(a))
b = 2
print('\ninteger implemenation : ',b,type(b))
c = 29.87
print('\nfloat implemenation : ',c,type(c))
com = 15+98j
print('\nComplex numbers implemenation : ',com,type(com))
l = [1,'one',1.00,1+2j]
print('\nlist implemenation : ',l,type(l))
ran = range(10)
print('\nRange implemenation : ',ran,type(ran))
tup = ('abc',12,0.92)
print('\ntuple implemenation : ',tup,type(tup))

dic = {1:'hi',2:'you'}
print('\nDictionary implemenation : ')
print(dic,type(dic))
print('Dictionary values : ',dic.values())
print('Dictionary items : ',dic.items())
print('Dictionary keys : ',dic.keys())

s = {'hello','world','python'}
print('\nSet Implementation : ',s,type(s))

by = b'hi'
print('\nByte implemenation : ',by,type(by))

n = None
print('\nNone type : ',n,type(n))

id1 = 1223
print('id of id1 : ',id(id1),'is id of ',id1)