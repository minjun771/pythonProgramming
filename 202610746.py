a= int(input("입력 진수 결정(16/10/8/2) :"))

if a==16:
    num = int(input("값 입력 :"),16)
    c= hex(num)
    print ("16진수 ==>",c)
    print ("10진수 ==>",num)
    c= oct(num)
    print ("8진수 ==>",c)
    c= bin(num)
    print ("2진수 ==>",c)

if a==10:
    num = int(input("값 입력 :"))
    c= hex(num)
    print ("16진수 ==>",c)
    print ("10진수 ==>",num)
    c= oct(num)
    print ("8진수 ==>",c)
    c= bin(num)
    print ("2진수 ==>",c)

if a==8:
    num = int(input("값 입력 :"),8)
    c= hex(num)
    print ("16진수 ==>",c)
    print ("10진수 ==>",num)
    c= oct(num)
    print ("8진수 ==>",c)
    c= bin(num)
    print ("2진수 ==>",c)

if a==2:
    num = int(input("값 입력 :"),2)
    c= hex(num)
    print ("16진수 ==>",c)
    print ("10진수 ==>",num)
    c= oct(num)
    print ("8진수 ==>",c)
    c= bin(num)
    print ("2진수 ==>",c)