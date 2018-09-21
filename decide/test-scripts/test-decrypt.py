#!/usr/bin/env python

import sys
from mixnet.mixcrypt import MixCrypt
from mixnet.mixcrypt import ElGamal


SK = sys.argv[1]
MSG = sys.argv[2]

p, g, y, x = map(int, SK.split(','))
a, b = map(int, MSG.split(','))

k = MixCrypt(bits=256)
k.k = ElGamal.construct((p, g, y, x))

print(k.decrypt((a, b)))
