def upper1(x):
    s=""
    for y in x:
            if ord("a")<=ord(y)<=ord("z"):
                 s+= chr(ord(y)-32)
            else:
                s+=y
    return s


def lower1(x):
    s=""
    for y in x:
            if ord("A")<=ord(y)<=ord("Z"):
                 s+= chr(ord(y)+32)
            else:
                s+=y
    return s

                 
def isupper1(x):
    s=0
    for y in x:
            if ord(y)>=65 and ord(y)<=90 or (ord(y)>=32 and ord(y)<=64) or (ord(y)>=91 and ord(y)<=96):
                 s+=1
            else:
                continue
    if s==len(x):
        return True
    else:
        return False

            
def islower1(x):
    s=0
    for y in x:
        if ord(y)>=97 and ord(y)<=122 or (ord(y)>=32 and ord(y)<=64) or (ord(y)>=91 and ord(y)<=96):
                 s+=1
        else:
             continue
            
    if s==len(x):
            return True
    else:
            return False    
                

            
def isalpha1(x):
    s=0
    for y in x:
        if ord("A")<=ord(y)<=ord("Z") or  ord("a")<=ord(y)<=ord("z"):
            s+=1
        else: 
            continue
    if s==len(x):
            return True
    else:
            return False

        
def isdigit1(x):
    s=0
    for y in x:
        if ord(y)>=33 and ord(y)<=64:
            s+=1
        else:
            continue
    if s==len(x):
            return True
    else:
            return False

        
def isalnum1(x):
    s=0
    for y in x:
        if ((ord("A")<=ord(y)<=ord("Z")) or (ord("a")<=ord(y)<=ord("z")) or ("0"<=y<="9")) :
            s+=1
        else: 
            continue
    if s==len(x):
         return True
    else:   
         return False
   

def capitalize1(x):
        s=""
        for y in range(len(x)):
            if y==0:
                if ord("a")<=ord(x[0])<=ord("z"):
                    s+=chr(ord(x[0])-32)
                else:
                    s+=x[0]
            else: 
                if ord("A")<=ord(x[y])<=ord("Z"):
                    s+=chr(ord(x[y])+32)
                else:
                    s+=x[y]         
        return s


def swapcase1(x):
    s=""
    for y in x:
        if ord("a")<=ord(y)<=ord("z"):
            s+=chr(ord(y)-32)
        elif ord("A")<=ord(y)<=ord("Z"):
            s+=chr(ord(y)+32)
        else:
            s+=y
    return s


def title1(st):
    s="";a=0
    for x in st:
        if x==" ":
            a=0
            for y in x:
                if (ord(x)>=97 and ord(x)<=122) and a==0:
                    s+=chr(ord(x)-32)
                    a+=1
                elif ord(x)>=65 and ord(x)<=90 and not(a==0):
                    s+=chr(ord(x)+32)
                    a+=1
                else:
                    s+=x
        elif a==0:
            if (ord(x)>=97 and ord(x)<=122):
                s+=chr(ord(x)-32)
                a+=1
            elif ord(x)>=65 and ord(x)<=90:
                s+=x
            else:
                s+=x
        else:
            if ord(x)>=65 and ord(x)<=90:
                s+=chr(ord(x)+32)
            else:
                s+=x
    return s