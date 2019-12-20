
Let y0, y1, y2,... be a sequence of random unsigned 32 bit integers
(i.e. 0 &#8804; yi < 232, every value equally likely).
For the sequence xi the following recursion is given:

x0 = 0 and
xi = xi-1 | yi-1, for i > 0. ( | is the bitwise-OR operator)

It can be seen that eventually there will be an index N such that xi = 232 -1 (a bit-pattern of all ones) for all i &#8805; N.
Find the expected value of N. 
Give your answer rounded to 10 digits after the decimal point.
