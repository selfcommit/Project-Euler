
Let n be a positive integer.
A 6-sided die is thrown n times. Let c be the number of pairs of consecutive throws that give the same value.
For example, if n = 7 and the values of the die throws are (1,1,5,6,6,6,3), then the following pairs of consecutive throws give the same value:
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
(1,1,5,6,6,6,3)
Therefore, c = 3 for (1,1,5,6,6,6,3).
Define C(n) as the number of outcomes of throwing a 6-sided die n times such that c does not exceed &#960;(n).1
For example, C(3) = 216, C(4) = 1290, C(11) = 361912500 and C(24) = 4727547363281250000.
Define S(L) as &#8721; C(n) for 1 &#8804; n &#8804; L.
For example, S(50) mod 1&#160;000&#160;000&#160;007 = 832833871.
Find S(50&#160;000&#160;000) mod 1&#160;000&#160;000&#160;007.
1 &#960; denotes the prime-counting function, i.e. &#960;(n) is the number of primes &#8804; n.
