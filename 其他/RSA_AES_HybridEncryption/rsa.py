def quickMod(a:int, x:int, n:int) -> int:
    """
    快速模幂算法
    计算a^x mod n
    """

    result = 1
    while(x!=0):
        if(x&1==1):
            result = (result*a)%n
        x = x >> 1
        a = (a*a)%n
    return result

def RSA_Encryption(plainText:str, n:int, e:int) -> int :
    """
    plainText为要加密的明文，8字节一组
    n, e为公钥，进行RSA加密
    """

    plainTextByte = plainText.encode('utf-8')
    # 二进制数直接读取为整型
    plainTextInt = int.from_bytes(plainTextByte, 'big', signed=False)
    cipherTextInt = quickMod(plainTextInt, e, n)
    return cipherTextInt

def RSA_Decryption(cipherTextInt:int, d:int, n:int) -> str :
    """
    cipherTextInt是密文
    d是私钥
    """
    
    plainTextInt = quickMod(cipherTextInt, d, n)
    # 转换成字节流的位数当与n相同
    plainTextByte = plainTextInt.to_bytes(128, byteorder='big', signed=False)
    # 去掉\x00
    plainText = plainTextByte.decode('utf-8')
    plainText = plainText.lstrip(b'\x00'.decode('utf-8'))
    return plainText