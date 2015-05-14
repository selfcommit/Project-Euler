
A sequence of integers S = {si} is called an n-sequence if it has n elements and each element si satisfies 1 &#8804; si &#8804; n. Thus there are nn distinct n-sequences in total.
For example, the sequence S = {1, 5, 5, 10, 7, 7, 7, 2, 3, 7} is a 10-sequence.
For any sequence S, let L(S) be the length of the longest contiguous subsequence of S with the same value.
For example, for the given sequence S above, L(S) = 3, because of the three consecutive 7's.
Let f(n) = &#8721; L(S) for all n-sequences S.
For example, f(3) = 45, f(7) = 1403689 and f(11) = 481496895121.
Find f(7&#160;500&#160;000) mod 1&#160;000&#160;000&#160;009.
