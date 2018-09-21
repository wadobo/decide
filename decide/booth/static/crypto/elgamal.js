ElGamal = {};
ElGamal.BITS = 256;

ElGamal.getRandomInteger = function(max) {
  var bit_length = max.bitLength();
  var random;
  random = sjcl.random.randomWords(bit_length, 0);
  // we get a bit array instead of a BigInteger in this case
  var rand_bi = new BigInt(sjcl.codec.hex.fromBits(random), 16);
  return rand_bi.mod(max);
  return BigInt._from_java_object(random).mod(max);
};

ElGamal.encrypt = function(pk, m, r) {
  if (m.equals(BigInt.ZERO))
    throw "Can't encrypt 0 with El Gamal"

  if (!r) {
    let q = BigInt.fromInt(2).pow(ElGamal.BITS);
    let q1 = q.subtract(BigInt.ONE);
    r = ElGamal.getRandomInteger(q1);
  }

  var alpha = pk.g.modPow(r, pk.p);
  var beta = (pk.y.modPow(r, pk.p)).multiply(m).mod(pk.p);

  return { alpha: alpha, beta: beta };
};
