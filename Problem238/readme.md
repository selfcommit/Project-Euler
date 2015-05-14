

table.p238 td { padding: 0px 3px 0px 3px; }

Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number generator:


s0
=
14025256

sn+1
=
sn2 mod 20300713


Concatenate these numbers &#8201;s0s1s2&#8230; to create a string w of infinite length.
Then, w&#8201;=&#8201;14025256741014958470038053646&#8230;
For a positive integer k, if no substring of w exists with a sum of digits equal to k, p(k) is defined to be zero. If at least one substring of w exists with a sum of digits equal to k, we define p(k)&#8201;=&#8201;z, where z is the starting position of the earliest such substring.
For instance:
The substrings 1, 14, 1402, &#8230; 
with respective sums of digits equal to 1, 5, 7, &#8230;
start at position 1, hence p(1)&#8201;=&#8201;p(5)&#8201;=&#8201;p(7)&#8201;=&#8201;&#8230;&#8201;=&#8201;1.
The substrings 4, 402, 4025, &#8230;
with respective sums of digits equal to 4, 6, 11, &#8230;
start at position 2, hence p(4)&#8201;=&#8201;p(6)&#8201;=&#8201;p(11)&#8201;=&#8201;&#8230;&#8201;=&#8201;2.
The substrings 02, 0252, &#8230;
with respective sums of digits equal to 2, 9, &#8230;
start at position 3, hence p(2)&#8201;=&#8201;p(9)&#8201;=&#8201;&#8230;&#8201;=&#8201;3.
Note that substring 025 starting at position 3, has a sum of digits equal to 7, but there was an earlier substring (starting at position 1) with a sum of digits equal to 7, so p(7)&#8201;=&#8201;1, not 3.
We can verify that, for 0&#8201;<&#8201;k&#8201;&#8804;&#8201;103, &#8721;&#8201;p(k) = 4742.
Find &#8721;&#8201;p(k), for 0&#8201;<&#8201;k&#8201;&#8804;&#8201;2&#183;1015.
