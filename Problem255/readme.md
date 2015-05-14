
We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.
The following procedure (essentially Heron's method adapted to integer arithmetic) finds the rounded-square-root of n:
Let d be the number of digits of the number n.
If d is odd, set x0 = 2&#215;10(d-1)&#8260;2.
If d is even, set x0 = 7&#215;10(d-2)&#8260;2.
Repeat:



until xk+1 = xk.

As an example, let us find the rounded-square-root of n = 4321.
n has 4 digits, so x0 = 7&#215;10(4-2)&#8260;2 = 70.


Since x2 = x1, we stop here.
So, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137&#8230;).

The number of iterations required when using this method is surprisingly low.
For example, we can find the rounded-square-root of a 5-digit integer (10,000 &#8804; n &#8804; 99,999) with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).

Using the procedure described above, what is the average number of iterations required to find the rounded-square-root of a 14-digit number (1013 &#8804; n < 1014)?
Give your answer rounded to 10 decimal places.

Note: The symbols &#8970;x&#8971; and &#8968;x&#8969; represent the floor function and ceiling function respectively.

