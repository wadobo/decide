'''
>>> B = 256
>>> k1 = MixCrypt(bits=B)
>>> k2 = MixCrypt(k=k1.k, bits=B)
>>> k3 = gen_multiple_key(k1, k2)
>>> N = 4
>>> clears = [random.StrongRandom().randint(1, B) for i in range(N)]
>>> cipher = [k3.encrypt(i) for i in clears]
>>> d = multiple_decrypt_shuffle(cipher, k1, k2)
>>> clears == d
False
>>> sorted(clears) == sorted(d)
True

>>> B = 256
>>> k1 = MixCrypt(bits=B)
>>> k1.setk(167,156,89,130) #doctest: +ELLIPSIS
<Crypto.PublicKey.ElGamal.ElGamalobj object at 0x...>
>>> k2 = MixCrypt(bits=B)
>>> k2.setk(167,156,53,161) #doctest: +ELLIPSIS
<Crypto.PublicKey.ElGamal.ElGamalobj object at 0x...>
>>> k3 = MixCrypt(bits=B)
>>> k3.k = ElGamal.construct((167, 156, 4717))
>>> k3.k.p, k3.k.g, k3.k.y
(167, 156, 4717)
>>> N = 4
>>> clears = [2,3,6,4]
>>> cipher = [(161, 109), (17, 101), (148, 163), (71, 37)]
>>> d = multiple_decrypt_shuffle(cipher, k2, k1)
>>> clears == d
False
>>> sorted(clears) == sorted(d)
True
'''


from pprint import pprint

from Crypto.PublicKey import ElGamal
from Crypto.Random import random
from Crypto import Random
from Crypto.Util.number import GCD


def rand(p):
    while True:
        k = random.StrongRandom().randint(1, int(p) - 1)
        if GCD(k, int(p) - 1) == 1: break
    return k


def gen_multiple_key(*crypts):
    k1 = crypts[0]
    k = MixCrypt(k=k1.k, bits=k1.bits)
    k.k.y = 1
    for kx in crypts:
        k.k.y *= kx.k.y
    k.k.y = k.k.y % k.k.p
    return k


def multiple_decrypt(c, *crypts):
    a, b = c
    for k in crypts:
        b = k.decrypt((a, b))
    return b


def multiple_decrypt_shuffle(ciphers, *crypts):
    b = ciphers
    for i, k in enumerate(crypts):
        last = i == len(crypts) - 1
        b = k.shuffle_decrypt(b, last)
    return b

def multiple_decrypt_shuffle2(ciphers, *crypts, pubkey=None):
    '''
    >>> B = 256
    >>> k1 = MixCrypt(bits=B)
    >>> k2 = MixCrypt(k=k1.k, bits=B)
    >>> k3 = gen_multiple_key(k1, k2)
    >>> pk = pubkey=(k3.k.p, k3.k.g, k3.k.y)
    >>> N = 8
    >>> clears = [random.StrongRandom().randint(1, B) for i in range(N)]
    >>> cipher = [k3.encrypt(i) for i in clears]
    >>> d = multiple_decrypt_shuffle2(cipher, k1, k2, pubkey=pk)
    >>> clears == d
    False
    >>> sorted(clears) == sorted(d)
    True
    '''

    b = ciphers.copy()

    # shuffle
    for k in crypts:
        b = k.shuffle(b, pubkey)

    # decrypt
    for i, k in enumerate(crypts):
        last = i == len(crypts) - 1
        b = k.multiple_decrypt(b, last=last)
    return b


class MixCrypt:
    def __init__(self, k=None, bits=256):
        self.bits = bits
        if k:
            self.k = self.getk(k.p, k.g)
        else:
            self.k = self.genk()

    def genk(self):
        self.k = ElGamal.generate(self.bits, Random.new().read)
        return self.k

    def getk(self, p, g):
        x = rand(p)
        y = pow(g, x, p)
        self.k = ElGamal.construct((p, g, y, x))
        return self.k

    def setk(self, p, g, y, x):
        self.k = ElGamal.construct((p, g, y, x))
        return self.k

    def encrypt(self, m, k=None):
        r = rand(self.k.p)
        if not k:
            k = self.k
        a, b = k._encrypt(m, r)
        return a, b

    def decrypt(self, c):
        m = self.k._decrypt(c)
        return m

    def multiple_decrypt(self, msgs, last=True):
        msgs2 = []
        for a, b in msgs:
            clear = self.decrypt((a, b))
            if last:
                msg = clear
            else:
                msg = (a, clear)
            msgs2.append(msg)
        return msgs2

    def shuffle_decrypt(self, msgs, last=True):
        msgs2 = msgs.copy()
        msgs3 = []
        while msgs2:
            n = random.StrongRandom().randint(0, len(msgs2) - 1)
            a, b = msgs2.pop(n)
            clear = self.decrypt((a, b))
            if last:
                msg = clear
            else:
                msg = (a, clear)
            msgs3.append(msg)

        return msgs3

    def reencrypt(self, cipher, pubkey=None):
        '''
        >>> B = 256
        >>> k = MixCrypt(bits=B)
        >>> clears = [random.StrongRandom().randint(1, B) for i in range(5)]
        >>> cipher = [k.encrypt(i) for i in clears]
        >>> cipher2 = [k.reencrypt(i) for i in cipher]
        >>> d = [k.decrypt(i) for i in cipher]
        >>> d2 = [k.decrypt(i) for i in cipher2]
        >>> clears == d == d2
        True
        >>> cipher != cipher2
        True
        '''

        if pubkey:
            p, g, y = pubkey
            k = ElGamal.construct((p, g, y))
        else:
            k = self.k

        a, b = map(int, cipher)
        a1, b1 = map(int, self.encrypt(1, k=k))
        p = int(k.p)

        return ((a * a1) % p, (b * b1) % p)

    def gen_perm(self, l):
        x = list(range(l))
        for i in range(l):
            d = random.StrongRandom().randint(0, i)
            if i != d:
                x[i] = x[d]
                x[d] = i
        return x

    def shuffle(self, msgs, pubkey=None):
        '''
        Reencrypt and shuffle
        '''

        msgs2 = msgs.copy()
        perm = self.gen_perm(len(msgs))
        for i, p in enumerate(perm):
            m = msgs[p]
            nm = self.reencrypt(m, pubkey)
            msgs2[i] = nm

        return msgs2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
