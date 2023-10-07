while True:
    byte1,byte2=map(int,input('Введите 2 числа (dec), закодированные кодом Хемминга (15,11): ').split())
    binByte1=str(bin(byte1)[2:])
    binByte2=str(bin(byte2)[2:])

    while len(binByte1) < 8:
        binByte1='0'+binByte1

    while len(binByte2) < 8:
        binByte2='0'+binByte2

    numBin=binByte1+binByte2
    num=[i for i in numBin]

    num.pop(0)
    num.pop(0)
    num.pop(0)
    num.pop(1)
    num.pop(4)
    num="".join(num)
    numDec=int(num,base=2)
    print(numDec)
    


