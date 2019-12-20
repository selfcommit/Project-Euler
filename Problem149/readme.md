
Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).

&#8722;2532
9&#8722;651
3273
&#8722;18&#8722;4&#160; 8

Now, let us repeat the search, but on a much larger scale:
First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":
For 1 &#8804; k &#8804; 55, sk = [100003 &#8722; 200003k + 300007k3] (modulo 1000000) &#8722; 500000.
For 56 &#8804; k &#8804; 4000000, sk = [sk&#8722;24 + sk&#8722;55 + 1000000] (modulo 1000000) &#8722; 500000.
Thus, s10 = &#8722;393027 and s100 = 86613.
The terms of s are then arranged in a 2000&#215;2000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.
Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
