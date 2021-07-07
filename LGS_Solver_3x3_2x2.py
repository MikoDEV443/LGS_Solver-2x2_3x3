

choser = float(input(" For 2x2 press 1 for 3x3 press 2: "))

if choser == 1:

    a1 = float(input("Ko für a1="))
    b1 = float(input("Ko für b1="))
    c1 = float(input("Ko für c1="))
    a2 = float(input("Ko für a2="))
    b2 = float(input("Ko für b2="))
    c2 = float(input("Ko für c2="))
    D = (a1*b2)-(a2*b1)
    Dx = (c1*b2)-(c2*b1)
    Dy = (a1*c2)-(a2*c1)

    x = Dx/D
    y = Dy/D
    #print("D=",float((a1*b2)-(a2*b1)),"=",str(D))
    print("D=", a1,"*",b2,"-",a2,"*",b1,"=", str(D))
    #print("Dx=",float((c1*b2)-(c2*b1)),"=",str(Dx))
    print("Dx=",c1,"*",b2,"-",c2,"*",b1,"=", str(Dx))
    #print("Dy=",float((a1*c2)-(a2*c1)),"=",str(Dy))
    print("Dy=",a1,"*",c2,"-",a2,"*",c1, "=", str(Dy))
    print("x ="+ str(x))
    print("y =" + str(y))

if choser == 2:
    a1 = float(input("Ko für a1="))
    b1 = float(input("Ko für b1="))
    c1 = float(input("Ko für c1="))
    d1 = float(input("Ko für d1="))
    a2 = float(input("Ko für a2="))
    b2 = float(input("Ko für b2="))
    c2 = float(input("Ko für c2="))
    d2 = float(input("Ko für d2="))
    a3 = float(input("Ko für a3="))
    b3 = float(input("Ko für b3="))
    c3 = float(input("Ko für c3="))
    d3 = float(input("Ko für d3="))

    D = (a1*b2*c3)+(a3*b1*c2)+(a2*b3*c1)-(a3*b2*c1)-(a1*b3*c2)-(a2*b1*c3)
    Dx = (d1*b2*c3)+(d3*b1*c2)+(d2*b3*c1)-(d3*b2*c1)-(d1*b3*c2)-(d2*b1*c3)
    Dy = (a1*d2*c3)+(a3*d1*c2)+(a2*d3*c1)-(a3*d2*c1)-(a1*d3*c2)-(a2*d1*c3)
    Dz = (a1*b2*d3)+(a3*b1*d2)+(a2*b3*d1)-(a3*b2*d1)-(a1*b3*d2)-(a2*b1*d3)

    x = Dx/D
    y = Dy/D
    z = Dz/D

    print("D=",a1,"*",b2,"*",c3,"+",a3,"*",b1,"*",c2,"+",a2,"*",b3,"*",c1,"-",a3,"*",b2,"*",c1,"-",a1,"*",b3,"*",c2,"-",a2,"*",b1,"*",c3, "=", str(D))
    print("Dx=",d1,"*",b2,"*",c3,"+",d3,"*",b1,"*",c2,"+",d2,"*",b3,"*",c1,"-",d3,"*",b2,"*",c1,"-",d1,"*",b3,"*",c2,"-",d2,"*",b1,"*",c3, "=", str(Dx))
    print("Dy=",a1,"*",d2,"*",c3,"+",a3,"*",d1,"*",c2,"+",a2,"*",d3,"*",c1,"-",a3,"*",d2,"*",c1,"-",a1,"*",d3,"*",c2,"-",a2,"*",d1,"*",c3, "=", str(Dy))
    print("Dz=",a1,"*",b2,"*",d3,"+",a3,"*",b1,"*",d2,"+",a2,"*",b3,"*",d1,"-",a3,"*",b2,"*",d1,"-",a1,"*",b3,"*",d2,"-",a2,"*",b1,"*",d3, "=", str(Dz))


    print("x =" + str(x))
    print("y =" + str(y))
    print("z =" + str(z))





