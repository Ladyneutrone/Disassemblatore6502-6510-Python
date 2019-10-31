
import sys

print("START")

args = sys.argv

finput = args[1]
mod = args[2]

startInt = int('0x'+args[3], 16)
startHEX = hex(startInt)

#print("COMPLEMEMTO A 2 lOADING ... ")
compA2 = []
for number in range(0,128):
    tmp = []
    tmp.append(bin(number))
    tmp.append(number)
    compA2.append(tmp)
    #print(number,bin(number))
count=255    
while count > 127:    
    tmp = []
    tmp.append(bin(count))
    number=count-256
    tmp.append(number)
    compA2.append(tmp)
    #print(number,bin(count),count)
    count=count-1
#print("COMPLEMEMTO A 2 lOADED ... ")
    
opcodes = []
opcodeST= []
print("OPCODE lOADING ... ")
count=-1
for line in open('opcodes6502-6510.txt'):
    fields = line.split("|")
    opcodeST= []
    opcodeST.append(fields[0])
    opcodeST.append(fields[1])
    opcodeST.append(fields[2][:1])
    opcodes.append(opcodeST)    
print("OPCODE lOADED ...")

#print("OPCODE VERIFY START ... ")
#for count in range(0,len(opcodes)):
#    print(opcodes[count][0]+" "+opcodes[count][1]+" "+opcodes[count][2])    
#print("OPCODE VERIFY END ... \n")

fw = open('listOpCode.txt', 'w+')
assembler = []
opcodesInt = []
#nsFlg="D" or "H"
nsFlg=mod
print("ASSEMBLER lOADING ... ")
for line in open(finput):
    line=line[:-1]
    line=line.upper()
    opcode = line.split(",")
    for count in range(0,len(opcode)):
        if nsFlg=="D":
            hesa=hex(int(opcode[count]))
            esa=str(hex(int(opcode[count])))
            esa=esa[2:].upper()
            opcodesInt.append(int(opcode[count]))
        else:
            esa=opcode[count]
            opcodesInt.append(int(opcode[count],16))
        if len(esa)==1: esa="0"+esa
        #print(esa+" "+opcode[count])
        assembler.append(esa)
        if nsFlg=="D":
            fw.writelines(opcode[count]+" "+esa+"\n")
        else:
            dec=int(opcode[count],16)
            fw.writelines(str(dec)+" "+opcode[count]+"\n")
            
print("ASSEMBLER lOADED ... \n")

fw = open('listato.txt', 'w+')
#start=0xC000
#start=0x6000
#start=828
start = startInt

countStat=start
countStatNext=0
count = 0
while count < len(assembler):
    for count1 in range(0,len(opcodes)):
        if opcodes[count1][0]==assembler[count]:
            opcode=assembler[count]
            ##print(opcodes[count1][0]+" "+assembler[count])
            stat = opcodes[count1][1]
            #print(opcodes[count1][1][:3])
            if opcodes[count1][2]=="1":
                countStatNext=countStat+1
                opcode=opcode+"\t\t\t\t"                
            elif opcodes[count1][2]=="2":
                countStatNext=countStat+2
                opcode=opcode+" "+assembler[count+1]+"\t\t"
                ##print(assembler[count+1])
                # BEQ,BNE,BCC,BCS,BVC,BVS,BPL,BMI
                if "BEQ BNE BCC BCS BVC BVS BPL BMI".find(opcodes[count1][1][:3])!=-1:
                    bi=bin(opcodesInt[count+1])
                    #print(bi,int(bi[2:], 2))
                    for cmp2 in range(0,len(compA2)):
                        if compA2[cmp2][0]==bi:
                            #print(compA2[cmp2][0],compA2[cmp2][1])
                            break
                    #print(countStatNext,compA2[cmp2][1])
                    x=countStatNext+compA2[cmp2][1]
                    esa=str(hex(x))
                    esa=esa[2:].upper()     
                    stat=stat.replace("@",esa)
                else:
                    stat=stat.replace("@",assembler[count+1])
                count=count+1                  
            elif opcodes[count1][2]=="3":
                countStatNext=countStat+3
                #print(assembler[count+2][1])
                opcode=opcode+" "+assembler[count+1]+" "+assembler[count+2]+"\t"
                ##print(assembler[count+1])
                ##print(assembler[count+2])
                stat=stat.replace("@",assembler[count+2])
                stat=stat.replace("&",assembler[count+1])
                count=count+2
            countStatHex=str(hex(countStat)).upper()
            countStatHex=countStatHex[2:]
            ##print(countStatHex+" "+opcode+" "+stat)
            countStat=countStatNext
            fw.writelines(countStatHex+" "+opcode+stat+"\n")
            break
    count=count+1

print("END")

