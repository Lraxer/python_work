b64index = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/')
def base64Encode(plaintext : str) -> str :
    if(not len(plaintext)):
        return ""
    binstr = str()
    b64str = []
    for ch in plaintext :
        binstr+='{:08b}'.format(ord(ch))
    length = len(binstr)
    comlen = length//6
    tail = length%6
    for c in range(comlen):
        tmpstr = '{:08b}'.format(int(binstr[c*6:(c+1)*6], 2))
        b64str.append(tmpstr)
    lastbyte = '00'+binstr[comlen*6:]+'0'*(6-tail)
    b64str.append(lastbyte)

    addilen = 3 - (length//8)%3
    b64code = str()
    for b in b64str :
        b64code += b64index[int(b, 2)]
    b64code+='='*addilen

    return b64code


if __name__ == "__main__":
    s = "asldk"
    b64code = base64Encode(s)
    print(b64code)