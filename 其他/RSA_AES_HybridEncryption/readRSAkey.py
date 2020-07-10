from Crypto.PublicKey import RSA


def readKey() -> list :
    """
    返回(n, e, d)
    """
    public_key = RSA.importKey(open('./pub.key', 'r').read())
    private_key = RSA.importKey(open('./pri.key', 'r').read())
    return (public_key.n, public_key.e, private_key.d)