
There are n stones in a pond, numbered 1 to n. Consecutive stones are spaced one unit apart.
A frog sits on stone 1. He wishes to visit each stone exactly once, stopping on stone n. However, he can only jump from one stone to another if they are at most 3 units apart. In other words, from stone i, he can reach a stone j if 1 &#8804; j &#8804; n and j is in the set {i-3, i-2, i-1, i+1, i+2, i+3}.
Let f(n) be the number of ways he can do this. For example, f(6) = 14, as shown below:
1 &#8594; 2 &#8594; 3 &#8594; 4 &#8594; 5 &#8594; 6 
1 &#8594; 2 &#8594; 3 &#8594; 5 &#8594; 4 &#8594; 6 
1 &#8594; 2 &#8594; 4 &#8594; 3 &#8594; 5 &#8594; 6 
1 &#8594; 2 &#8594; 4 &#8594; 5 &#8594; 3 &#8594; 6 
1 &#8594; 2 &#8594; 5 &#8594; 3 &#8594; 4 &#8594; 6 
1 &#8594; 2 &#8594; 5 &#8594; 4 &#8594; 3 &#8594; 6 
1 &#8594; 3 &#8594; 2 &#8594; 4 &#8594; 5 &#8594; 6 
1 &#8594; 3 &#8594; 2 &#8594; 5 &#8594; 4 &#8594; 6 
1 &#8594; 3 &#8594; 4 &#8594; 2 &#8594; 5 &#8594; 6 
1 &#8594; 3 &#8594; 5 &#8594; 2 &#8594; 4 &#8594; 6 
1 &#8594; 4 &#8594; 2 &#8594; 3 &#8594; 5 &#8594; 6 
1 &#8594; 4 &#8594; 2 &#8594; 5 &#8594; 3 &#8594; 6 
1 &#8594; 4 &#8594; 3 &#8594; 2 &#8594; 5 &#8594; 6 
1 &#8594; 4 &#8594; 5 &#8594; 2 &#8594; 3 &#8594; 6
Other examples are f(10) = 254 and f(40) = 1439682432976.
Let S(L) = &#8721; f(n)3 for 1 &#8804; n &#8804; L.
Examples:
S(10) = 18230635
S(20) = 104207881192114219
S(1 000) mod 109 = 225031475
S(1 000 000) mod 109 = 363486179
Find S(1014) mod 109.
