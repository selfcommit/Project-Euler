
The most naive way of computing n15 requires fourteen multiplications:
n &#215; n &#215; ... &#215; n = n15
But using a "binary" method you can compute it in six multiplications:
n &#215; n = n2
n2 &#215; n2 = n4
n4 &#215; n4 = n8
n8 &#215; n4 = n12
n12 &#215; n2 = n14
n14 &#215; n = n15
However it is yet possible to compute it in only five multiplications:
n &#215; n = n2
n2 &#215; n = n3
n3 &#215; n3 = n6
n6 &#215; n6 = n12
n12 &#215; n3 = n15
We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.
For 1 &#8804; k &#8804; 200, find &#8721; m(k).
