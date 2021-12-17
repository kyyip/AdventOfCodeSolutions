#Solution for https://adventofcode.com/2021/day/16 by Kelvin Yip
puzzleinput = "020D64AEE52E55B4C017938FBBAC2D6002A53D21F9E90C18023600B80021D0862DC1700043232C2284D3B0105007251DE33CF281802D0E7001A0958C3B6EB542D2014340010B89112E228803518E2047E0004322B4128352DFE72BFE1CC77000E226B92FF7F7F0F4899CCEB788FBA632A444019349E40A801CA941898B661ECBC40820061A78E254024C126797B31A804B27C0582B2D7D4AF02791E431531100B2458A6219D29CB6C4247F7D6DB27BCBA4065138014C05B00801CC0513280108047020106460079801000332200B60002832801C200718012801503801A800B02801723F9B90009D6600D44A87B0CC8010B89D0661F980331F20A44470076767F8EF75AA94F5E1E6E9790C9008BF801AB8002171CA2A45C100661FC508B911C8043EC00C224BB8A753A6677FDB7B8EA85932F4600BE0039138612F684AB86392889C4A201253C013100623D464834200CC1787D09E76FC78200A16603A543E6D9E695E4C74C012D004646D08CAF74391B4232BDD1E4FFEE033805B3DAB074ACF351399FCCEA5F592697E1CB802B2D1D0BCFE410C015B004E46BE17973C949C213153005A6932C0129BDF675DD2CBF3482401BE7802D37AA4DFE6F549BD4A42363A200D5F40149985FEDF2ACF35AB4BD3003004A730F74019B8803F08A0943B1007A21C2487C0002DC578BC600A497B35A8050020F24432444401415002AF07A7F7FE004DB93001A931FC33A802B37FB517A4A52254010E2374C637895BF7E5CC66F53EB0CC2F4C92080292B1E7A0DB26BE6008CE1ACC801804938F530A1227F2A6A4004349A31009F7801A900021908A18C5D100722C43C8F9312CFD4040269934949661E0096FE75092ACA4F0B6A005CD6CBE1218027258AA3F00439377F5D566E338D121C0239DD9C4942FA4E8F73DFA62656402704E523896FAE9E00B4E779DE6BF15595C56DBF0ACD391802F400FA4FEADD769FD5BAE7318FCF32AB8"

#Dictionary to convert hexadecimal into binary
bindict = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000",
          "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F":"1111"}
bincode = ""
for i in puzzleinput:
    bincode += bindict[i]


#Base conversion functions
def hextobin(num):
    global bindict
    bincode = ""
    for i in num:
        bincode += bindict[i]
    return bincode

def bintodec(num):
    tot = 0
    for i in range(len(num)):
        tot += int(num[-i-1]) * 2 ** i
    return tot


#Part 1 Hierarchy doesn't matter, it's easy enough to know when a new packet starts so just find and add version numbers
tot = 0
state = 'V'
pos = 0
bincode = hextobin(puzzleinput)
while pos < len(bincode):
    if state == 'V':
        if len(bincode[pos:]) < 4:
            break
        tot += bintodec(bincode[pos:pos+3])
        pos += 3
        state = 'T'
    if state == 'T':
        if bintodec(bincode[pos:pos+3]) != 4:
            state = 'I'
        else:
            state = 'literal'
        pos += 3
    if state == 'literal':
        mod = 2
        while True:
            if bincode[pos] == '0':
                pos += 5
                mod += 5
                break
            else:
                pos += 5
                mod += 5
        state = 'V'
    if state == 'I':
        if bincode[pos] == '0':
            pos += 16
        else:
            pos += 12
        state = 'V'
            
        
print(tot)

#Part 2 Unwieldy state machine 
def statefunc(values, state):
    if state == 0:
        return sum(values)
    elif state == 1:
        result = 1
        for i in values:
            result = result * i
        return result
    elif state == 2:
        return min(values)
    elif state == 3:
        return max(values)
    elif state == 5:
        if values[0] > values[1]:
            return 1
        else:
            return 0
    elif state == 6:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    elif state == 7:
        if values[0] == values[1]:
            return 1
        else:
            return 0

#Use recursion to parse subpackets
#Default values for optional arguments correspond to the first packet in the signal
#In the case of my input, it's an operator packet of state 0 containing 53 subpackets
def packets(signal, pos = 18, values = [], subpackets = 53, length = 0, state=0):
    while subpackets > 0 or length > 0:
        if bintodec(signal[pos+3:pos+6]) == 4:
            tot = ""
            pos += 6
            while True:
                tot += signal[pos+1:pos+5]
                pos += 5
                if signal[pos-5] == '0':
                    break
            values.append(bintodec(tot))
            if subpackets > 0:
                subpackets -= 1
            if length > 0:
                length -= 6 + len(tot) + len(tot)/4
        else:
            newstate = bintodec(signal[pos+3:pos+6])
            if signal[pos+6] == '0':
                newpos, newvalue = packets(signal, pos+22, values=[],
                                          subpackets=0, length = bintodec(signal[pos+7:pos+22]), state=newstate)
            else:
                newpos, newvalue = packets(signal, pos+18, values=[], 
                                      subpackets=bintodec(signal[pos+7:pos+18]), length = 0, state=newstate)
            if length > 0:
                length -= newpos-pos
            pos=newpos
            values.append(newvalue)
            if subpackets > 0:
                subpackets -= 1
    return pos, statefunc(values, state)

print(packets(bincode, pos=18, values=[], subpackets= 53, length=0, state=0)[1])

