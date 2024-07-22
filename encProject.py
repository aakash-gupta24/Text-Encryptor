import random
import time
letters=[]
def genLetters():
    global letters
    templetters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ',':','1','2','3','4','5','6','7','8','9','0','+']
    
    letters=[]
    while(len(templetters)>0):
        tempnum=random.randint(0,len(templetters)-1)
        if(templetters[tempnum] not in letters):
            letters.append(templetters[tempnum])
        templetters.pop(templetters.index(templetters[tempnum]))
codes=[]
encDW=""
codeW=""
def rerandomize(re):#create new combo for repeats
    global letters,codes
    temp=""
    for x in range(3):#create new combo
        l=random.randint(0,len(letters)-1)
        temp+=letters[l]
    if(temp!=re and temp not in codes):#compare for presence if not the  sends to out
        return temp
    else:
        rerandomize(re)#else create a new combo
    
def randomize():
    global letters,codes
    out=""#store and send codes
    for y in range(len(letters)):
        for x in range(3):#create a combo
            l=random.randint(0,len(letters)-1)
            out+=letters[l]
        if(out not in codes):#check for any occurance
            codes.append(out)
            out=""
        else:
            out=rerandomize(out)#sends for new combo  creation
            codes.append(out)
            out=""

def codew():
    global codes,codeW
    codeW=""
    for x in codes:
        codeW+=x+"."

def encD():
    global encDW,codes,letters
    #time.sleep(2)
    fname=input("Enter the THE NAME OF THE FILE TO ENCRIPT:")
    f=open(fname+".txt",'r')
    dat=(f.read()).split("\n")
    for y in dat:
        for x in y:
            encDW+=codes[letters.index(x)]+"."
        encDW+="|||."
    f.close()
def backfor():
    global letters
    let=""
    for x in letters:
        let+=x+"."
    return let+"\n"
    
print("===========WELCOME===========")
print("")
#time.sleep(1)
print("======CHOOSE=THE=OPTION======")
print("=   1.Encrip                =")
print("=   2.Decript               =")
print("=   0.End                   =")
print("=============================")
#time.sleep(1)
opt=input("Enter the OPTION:")
while(True):
    if(int(opt)==1):
        genLetters()
        randomize()
        encD()
        #time.sleep(1)
        pas=input("Enter the PASSWORD for the file:")
        #time.sleep(2)
        pasW=""
        for x in pas:
            pasW+=codes[letters.index(x)]+"."
        pasW+="\n"
        codew()
        codeW+="\n"
        encDW+="\n"
        fnss=input("Enter the Name of the ENCRIPTED FILE:")
        f=open(fnss+".txt",'w')
        f.write(pasW)
        f.write(backfor())
        #print("backfor---",backfor())
        f.write(codeW)
        f.write(encDW)
        f.close()
        #time.sleep(1)
        print("DONE")
        pasW=""
        codeW==""
        encDW=""
        #time.sleep(2)
        print("======CHOOSE=THE=OPTION======")
        print("=   1.Encript               =")
        print("=   2.Decript               =")
        print("=   0.End                   =")
        print("=============================")
        opt=int(input("Enter the option:"))
        #time.sleep(1)
    elif(int(opt)==2):
        #time.sleep(1)
        fn=input("Enter the NAME of the FILE:")
        f=open(fn+".txt",'r')
        temppas=((f.readline()).strip("\n"))
        letters=((f.readline()).strip("\n")).split(".")
        #print("letters----",letters)
        rec=((f.readline()).strip("\n")).split(".")
        #print("rec----",rec)
        #time.sleep(1)
        pa=input("Enter the PASSWORD:")
        #time.sleep(1)
        TRY=""
        for x in pa:
           TRY+=rec[letters.index(x)]+"."
        if(TRY==temppas):
            time.sleep(1)
            print("CORRECT,and DONE")
            Edata=(f.readline().strip("\n")).split(".")
            new=""
            for z in Edata:
                if(z!=''):
                    if(z!='|||'):
                        new+=letters[rec.index(z)]
                    else:
                        new+="\n"
            f.close()
            f=open(fn+".txt",'w')
            f.write(new)
            f.close()
        else:
            #time.sleep(1)
            print("WRONG PASSWORD!!")
            print("======CHOOSE=THE=OPTION======")
            print("=   1.Encrit                =")
            print("=   2.Decript               =")
            print("=   0.End                   =")
            print("=============================")
        opt=int(input("Enter the OPTION:"))
    elif(int(opt)==0):
        break
