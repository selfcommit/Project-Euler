

table.p375 td {
  padding: 0px 3px 0px 3px;
  vertical-align: bottom;
  text-align: left;
}

Let Sn be an integer sequence produced with the following pseudo-random number generator:


S0
=&#160;
290797&#160;

Sn+1
=&#160;
Sn2 mod 50515093



Let A(i, j) be the minimum of the numbers Si, Si+1, ... , Sj for i &#8804; j.
Let M(N) = &#931;A(i, j) for 1 &#8804; i &#8804; j &#8804; N.
We can verify that M(10) = 432256955 and M(10 000) = 3264567774119.

Find M(2 000 000 000).

