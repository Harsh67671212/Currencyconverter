print('''Welcome to Currency Converter App
       For Indian Currency Conversion:
       To US Dollar          Type:1
       To POUND              Type:2
       To Euro               Type:3
       To CANADIAN DOLLAR    Type:4
       To CHINESE YUAN       Type:5
       To RUSSIA RUBEL       Type:6
       EXIT                  Type:7''')
while(1):
    choice=int(input("Enter your choice: "))
    match choice:
        case 1:
           x=str(input('''For:
IND To USD Type-a 
USD To IND Type-b
'''))
           if(x == "a"):
               ITU=int(input("Enter IND: "))
               print("USD =",ITU*0.012)
           elif(x=="b"):
               UTI = int(input("Enter USD: "))
               print("IND=", UTI * 81.70)
           else:
               print("Invalid Choice")
        case 2:
            x = str(input('''For:
IND To GBP Type-a 
GBP To IND Type-b
'''))
            if (x == "a"):
                ITP = int(input("Enter IND: "))
                print("GBP =", ITP * 0.012)
            elif(x=="b"):
                PTI = int(input("Enter GBP: "))
                print("IND=", PTI * 70)
            else:
                print("Invalid Choice")
        case 3:
            x = x=str(input('''For: 
IND To EUR Type-a 
IND To EUR Type-b
'''))
            if (x =="a"):
                ITE = int(input("Enter IND: "))
                print("EUR =", ITE * 0.010)
            elif(x=="b"):
                ETI = int(input("Enter EUR: "))
                print("IND=", ETI *99.14 )
            else:
                print("Invalid Choice")
        case 4:
            x = str(input('''For:
IND To CAD Type-a  
CAD To IND Type-b
'''))
            if (x =="a"):
                ITCD = int(input("Enter IND: "))
                print("CAD=", ITCD * 0.016)
            elif(x=="b"):
                CDTI = int(input("Enter CAD: "))
                print("IND=", CDTI * 61.20)
            else:
                print("Invalid Choice")
        case 5:
            x = str(input('''For:
IND to CNY Type-a  
CNY to IND Type-b
'''))
            if (x =="a"):
                ITCY = int(input("Enter IND: "))
                print("CNY  =", ITCY * 0.087)
            elif(x=="b"):
                CYTI = int(input("Enter CNY: "))
                print("IND=", CYTI * 11.45)
            else:
                print("Invalid Choice")
        case 6:
            x = str(input('''For:
IND To RUB Type-a 
RUB To IND Type-b
'''))
            if (x == "a"):
                ITRR = int(input("Enter IND: "))
                print("RUB=", ITRR * 0.74)
            elif(x=="b"):
                RRTI = int(input("Enter RUB: "))
                print("IND=", RRTI * 1.36)
            else:
                print("Invalid Choice")
        case 7:
             exit((0))
        case default:
            print("Invalid Choice")
