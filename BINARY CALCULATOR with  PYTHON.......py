def mainmenu():
    global choice
    print("\nPRESS-1 To Perform Arithmatic Operations...")
    print("\nPRESS-2 To Find Binary Of Negative Decimal Number...")
    print("\nPRESS-3 To Perform Logical Operations...")
    print("\nPRESS-4 To Perform Basic Cnversion Operations...")
    print("\nPRESS-5 To Perform Text Conversion Operations...")
    try:
        choice=int(input("\n\nWHAT DO YOU WANT..?  : "))
        if choice == 1:
            print("\nNOTE-Arithmatic Operations Perform Only On Real Integers\n")
            return Arithmatic()
        elif choice == 2:
            return Nega_binary()
        elif choice == 3:
            return checkbinary()
        elif choice ==4:
            return basic_con()
        elif choice == 5:
            return text_con()
        else:
            print("\n\n\Choose Only From Given Options..")
            return mainmenu()
    except:
        err()
        print("\nEnter correct Input1\n")
        return mainmenu()


def Arithmatic():
    global cho1
    print("\nPRESS-1 For Input in Binary & Get result in Binary...")
    print("\nPRESS-2  For Input in Binary & Get result in Decimal...")
    print("\nPRESS-3  For Input in Decimal & Get result in Binary...")
    try:
        cho1=int(input("\nENTER YOUR CHOICE... : "))
        if cho1 == 1 or cho1 ==2 :
            return checkbinary()
        elif cho1 == 3:
            return checkdecimal()
        else:
            print("\n\n\Choose Only From Given Options..!")
            return Arithmatic()
    except:
        err()
        print("\nEnter correct Input2\n")
        return Arithmatic()

def checkbinary():
    global choice
    global cho6
    co1,co2,co3=0,0,0
    b1=input("\nEnter Binary ..: ")
    for x in b1:
        if ord(x)==ord('1') or ord(x)==ord('0'):
            continue
        elif ord(x)==ord('.'):
            co3+=1
        else:
            co1+=1
    if choice==1:
        b2=input("\nEnter Second Binary ..: ")
        for y in b2:
            if ord(y)==ord('1') or ord(y)==ord('0'):
                continue
            else:
                co2+=1
    print(co1,co2,co3)
    if co1!=0 or co2!=0:
        print("\nPlease Enter a Valid Binary..!")
        return checkbinary()
    elif co3!=0:
        if co3>1:
            print("Invalid Floating binary !\n Try Again")
            return checkbinary()
        else:
            return flocon(b1)
              
    else:
        if choice == 1:
            no1=int(b1,2)
            no2=int(b2,2)
            return Arithperform(no1,no2)
        elif choice == 3:
            return logical(b1)
        else:
            return deci_con(b1)

def Arithperform(a,b):
    global cho1
    try:
        cho3=int(input("\nPRESS-1(Addition\nPRESS-2(Subtraction)\nPRESS-3(Division)\nPRESS-4(Multiplecation)\n      - "))
        if cho3==1:
            result=(a+b)
        elif cho3==2:
            result=(a-b)
        elif cho3==3:
            try:
                result=(a/b)
                res=float_bina(result)
            except ZeroDivisionError:
                print("You Can't Divide a No. By zero...\n\n")
                result=0
        elif cho3==4:
            result=(a*b)
        else:
            print("\n\n\Choose Only From Given Options..!")
            return Arithperform(a,b)

        if (cho1==1 or cho1==3) and cho3==3 :
            print("\n\nAnswer is =",res)
        elif cho1==1 or cho1==3:
            print("Answer is =" ,(bin(result).replace('0b','')))
        elif cho1==2:
            print("\n\nAnswer is =",result)

        else:
            pass
        conti=input("\n\nPRESS-1 To Continue as Arithmatic...\nPRESS-2 To Return in Main Menu...\n PRESS Any Key To Exit...\n     - ")
        if conti == '1':
            return Arithmatic()
        elif conti == '2':
            return mainmenu()
        else:
            exit()
    except:
        err()
    
        print("\n Enter a Correct Input 3\n")
        return Arithperform(a,b)

def checkdecimal():
    try:
        n1=int(input("Enter First No.  : "))
        n2=int(input("Enter second No.  : "))
        return Arithperform(n1,n2)
    except:
        err()
        print("\n Enter a Correct Input 4\n")
        return checkdecimal()


def float_bina(num):
    b=0
    nn,spa,rp,str1,str2='','','','',''
    n=int(num)
    floa=num-n
    nn=bin(n)
    str2=nn[2::1]
    x=1
    count=0
    while(x!=0 and count<=8):
        if(x==1):
            x=floa
        x=x*2
        b=int(x)
        x-=b
        rp=rp+str(b)
        count+=1

    l=str2+'.'+rp
    return(l)



def Nega_binary():
    try:
        neg=int(input("Enter that Negative No..  : "))
        pos=abs(neg)
        str2,str3,str4='','',''
        str2=bin(pos)
        for i in range(2,len(str2)):
            if str2[i]=='0':
                b='1'
            else:
                b='0'
            str4+=b
        rev=list(str4[::-1])
        if rev[0]=='0':
            rev[0]='1'
        else:
            rev[0]='0'
            for x in range(1,len(rev)):
                if rev[x]=='0':
                    rev[x]='1'
                    break
                else:
                    rev[x]='0'

        for x in rev:
            str3=x+str3
        print("Binary of -",neg, "=", str3)
        cho4=input("\n\nPRESS-1 To Continue as Negative No. Binary...\nPRESS-2 To Return in Main Menu...\n PRESS Any Key To Exit...\n     - ")
        if cho4=='1':
            return Nega_binary()
        elif cho4=='2':
            return mainmenu()
        else:
            exit()
    except:
        err()
        print("\n Enter a Correct Input5 \n")
        return Nega_binary()


def logical(toper):
    try:
        cho5=int(input("\nPRESS-1 To perform Left Shift\nPRESS-2 To perform Right Shift\nPRESS-3 To perform Circular Left Shift\nPRESS-4 To perform Circular Right Shift\n      - "))
        str1,temp='',''
        if cho5 == 1:
            toper=list(toper)
            toper.pop(0)
            toper.insert(len(toper),'0')
            for i in toper:
                str1+=i
            print(str1)
        elif cho5 == 2:
            toper=list(toper)
            toper.pop()
            toper.insert(0,'0')
            for i in toper:
                str1+=i
            print(str1)
        
        elif cho5 == 3:
            toper=list(toper)
            temp=toper[0]
            toper.pop(0)
            toper.insert(len(toper),temp)
            for i in toper:
                str1+=i
            print(str1)
        elif cho5 == 4:
            toper=list(toper)
            temp=toper[len(toper)-1]
            toper.pop()
            toper.insert(0,temp)
            for i in toper:
                str1+=i
            print(str1)

        else:
            print("\n\n\Choose Only From Given Options..!")
            return logical(toper)

        contin=input("\n\nPRESS-1 To Continue as Logical...\nPRESS-2 To Return in Main Menu...\n PRESS Any Key To Exit...\n     - ")

        if contin=='1':
            return checkbinary(choice)
        elif contin=='2':
            return mainmenu()
        else:
            exit()
    except:
        err()
        print("\n Enter a Correct Input 6\n")
        return logical(toper)
        
def deci_con(Bin):
    try:
        print("Answer is =",int(Bin,2))
        cont=input("PRESS-1 Continue as Basic conversion..\nPRESS-2 Main menu..\nPRESS any key to Exit..")
        if cont == '1':
            return basic_con()
        elif cont == '2':
            return mainmenu()
        else:
            exit()
    except:
        print("\nInvalid Binary !\n")
        err()
        checkbinary()

def cut(str1):
    str2=''
    for i in str1:
        if i=='.' or i=='':
            break
        else:
            str2+=i
    return str2

def flocon(n):
    no,sum1=1,0
    p1=cut(n)
    n=list(n)
    n.reverse()
    p2=cut(n)
    for i in p2[::-1]:
        if i=='1':
            sum1+=(1/(2**no))
        no+=1
    x=(int('0'+p1,2)+sum1)
    return(x)


def basic_con():
    global cho6
    print("\nPRESS-1 For Fixed Point Decimal NO. To Binary..")
    print("\nPRESS-2 For Fixed Bnary To Fixed Point Decimal NO...")
    print("\nPRESS-3 For Floating Point No. To Floating Binary...")
    print("\nPRESS-4 For Floating Point Binary To Floating No.")
    try:
        cho6=int(input("Enter Choice.. : "))
        if cho6==1:
            num=int(input("Enter Number.. : "))
            print(bin(num).replace('0b',''))
            conti=input("PRESS-1 To Continue as Basic Canversion..\n2.PRESS-2 To Return Main Menu...\nPRESS any Key To Exit..\n      ")
            if conti=='1':
                return basic_con()
            elif conti=='2':
                return mainmenu()
            else:
                exit()

        elif cho6==2:
            return checkbinary()
        elif cho6==3:
            num1=float(input("Enter No.. : "))
            print(float_bina(num1))
            conti=input("Press-1 For Continue as Basic Conversion\nPRESS-2 For Return Main Menu\nPRESS Any key To Exit..\n       : ")
            if conti=='1':
                return basic_con()

            elif conti=='2':
                return mainmenu()
            else:
                exit()    

        elif cho6==4:
            print(checkbinary())
            cho=input("PRESS-1 Continue as basic Conversion\nPRESS-2 Return in Main Menu\nPRESS Any Key to Exit..")
            if cho=='1':
                return basic_con()
            elif cho=='2':
                return mainmenu()
            else:
                exit()
        else:
            print("Choose only Given Below..\n")
            return basic_con()
    except:
        err()
        print("Enter a Valid Input7\n")
        return basic_con()
def err():
    global count
    count+=1
    if count==3:
        print("\n\n-! ALERT -\- WARNING !....!- \n-!If You Enter INVALID INPUT Again Then it will Exit...!-\n")
    elif count>3:
        print("I HAVE BEEN TOLD YOU \n\nBYE BYE DEAR.....")
        exit()
    else:
        pass

    
def text_con():
    print("\nPRESS-1 For Text To Binary...\n")
    print("\nPRESS-2 For Binary To Text...\n")
    try:
        cho7=int(input("Enter Your Choice : "))
        if cho7==1:
            return Text()
        elif cho7==2:
            return Bin()
        else:
            print("Choose Only From Given Below...")
            return text_con()
    except:
        err()
        print("\nInvalid Input!\n")
        return text_con()


def Text():
    n=input("Enter Text : \n\n")
    sum1=''
    for x in n:
        binary=bin(ord(x)).replace('0b','')
        sum1=sum1+' '+binary
    print(sum1)
    conti=input("PRESS-1 To Continue as Text Conversion..\nPRESS-2 To Return Main Menu..\nPRESS Any Key To Exit..")
    if conti=='1':
        return text_con()
    elif conti == '2':
        return mainmenu()
    else:
        exit()

def Bin():
    co1=0
    Bin=input("\nEnter Binary : \n\n")
    for x in Bin:
        if x=='1' or x=='0' or x==' ':
            continue
        else:
            co1+=1
    if co1!=0:
        print("Invalid Binary Set !\nTry Again !")
        return Bin()
    else:
        bina,word,sum2='','',''
        Bin=Bin.strip()
        Bin=list(Bin)
        Bin.insert(len(Bin),' ')
        for i in Bin:
            if i==' ':
                if int(bina,2)>65535:
                    print("A Set of binary is found to 'OUT OF RANGE' of characters which is not Supperted.\nTry  Again!")
                    return Bin()
                else:
                    sum2=chr(int(bina,2))
                    word+=sum2
                    bina=''
            else:
                bina=bina+i
        print(word)
    conti=input("\n\nPRESS-1 To Continue as Test Conversion..\nPRESS-2 To Return in Main Menu..\nPRESS Any to Exit... : ")
    if conti == '1':
        return text_con()
    elif conti=='2':
        return mainmenu()
    else:
        exit()

     

print("\n\n\n        -----------------------------------------------------WELCOME  TO BINARY CALCULATOR----------------------------------------------------- \n\n\n")
count=0
mainmenu()            
