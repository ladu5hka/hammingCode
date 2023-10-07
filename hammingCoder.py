while True:
    numDec=int(input('Введите число (dec), которое хотите закодировать кодом Хемминга (15,11): '))
    numBin=str(bin(numDec)[2:])
    print(numBin)
    while len(numBin)<11:
        numBin='0'+numBin
    num=[i for i in numBin]
    num.insert(0,'0')
    num.insert(1,'0')
    num.insert(3,'0')
    num.insert(7,'0')
    s1=0
    s2=0
    s3=0
    s4=0
    for i in range(15):
        n1=i+1
        if n1%2==1:
            s1+=int(num[i])
    if s1%2==1: num[0]='1'

    for i in range(15):
        n2=i+1
        if n2%4>=2:
            s2+=int(num[i])
    if s2%2==1: num[1]='1'

    for i in range(15):
        n3=i+1
        if n3%8>=4:
            s3+=int(num[i])
    if s3%2==1: num[3]='1'

    for i in range(15):
        n4=i+1
        if n4%16>=8:
            s4+=int(num[i])
    if s4%2==1: num[7]='1'
    print(num)
    num.insert(0,'0')
    
    byte1="".join(num[:8])
    byte2="".join(num[8:])
    print('Закодированное число:',int(byte1,base=2),int(byte2,base=2),' = ', hex(int(byte1,base=2))[2:].upper(),hex(int(byte2,base=2))[2:].upper())
    
