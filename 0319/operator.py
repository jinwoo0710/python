a = 3;
b = ~a;
print("a=",a,"b=", b)

a = 3; b = 5;
c = a & b #AND 둘 중에 하나라도 0이면 0(둘다1이면1)

print("a=",a,"b=", b,"c=", c)

a = 3; b = 5;
c = a ^ b #exclusive OR 두 개가 같으면 0 다르면 1
print("a=",a, "b=",b, "c=",c) 

a = 3
b = 5
c = a | b # OR 두개 중 하나라도 1이면 1(둘 다 0이면0)
print("a=",a, "b=",b, "c=",c)
