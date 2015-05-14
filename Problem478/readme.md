
Let us consider mixtures of three substances: A, B and C. A mixture can be described by a ratio of the amounts of A, B, and C in it, i.e., (a&#160;:&#160;b&#160;:&#160;c). For example, a mixture described by the ratio (2&#160;:&#160;3&#160;:&#160;5) contains 20% A, 30% B and 50% C.
For the purposes of this problem, we cannot separate the individual components from a mixture. However, we can combine different amounts of different mixtures to form mixtures with new ratios.
For example, say we have three mixtures with ratios (3&#160;:&#160;0&#160;:&#160;2), (3&#160;:&#160;6&#160;:&#160;11) and (3&#160;:&#160;3&#160;:&#160;4). By mixing 10 units of the first, 20 units of the second and 30 units of the third, we get a new mixture with ratio (6&#160;:&#160;5&#160;:&#160;9), since:
(10&#183;3/5&#160;+&#160;20&#183;3/20&#160;+&#160;30&#183;3/10&#160;:&#160;10&#183;0/5&#160;+&#160;20&#183;6/20&#160;+&#160;30&#183;3/10&#160;:&#160;10&#183;2/5&#160;+&#160;20&#183;11/20&#160;+&#160;30&#183;4/10)
= (18&#160;:&#160;15&#160;:&#160;27) = (6&#160;:&#160;5&#160;:&#160;9)
However, with the same three mixtures, it is impossible to form the ratio (3&#160;:&#160;2&#160;:&#160;1), since the amount of B is always less than the amount of C.
Let n be a positive integer. Suppose that for every triple of integers (a, b, c) with 0 &#8804; a, b, c &#8804; n and gcd(a, b, c) = 1, we have a mixture with ratio (a&#160;:&#160;b&#160;:&#160;c). Let M(n) be the set of all such mixtures.
For example, M(2) contains the 19 mixtures with the following ratios:
{(0&#160;:&#160;0&#160;:&#160;1), (0&#160;:&#160;1&#160;:&#160;0), (0&#160;:&#160;1&#160;:&#160;1), (0&#160;:&#160;1&#160;:&#160;2), (0&#160;:&#160;2&#160;:&#160;1), 
(1&#160;:&#160;0&#160;:&#160;0), (1&#160;:&#160;0&#160;:&#160;1), (1&#160;:&#160;0&#160;:&#160;2), (1&#160;:&#160;1&#160;:&#160;0), (1&#160;:&#160;1&#160;:&#160;1), 
(1&#160;:&#160;1&#160;:&#160;2), (1&#160;:&#160;2&#160;:&#160;0), (1&#160;:&#160;2&#160;:&#160;1), (1&#160;:&#160;2&#160;:&#160;2), (2&#160;:&#160;0&#160;:&#160;1), 
(2&#160;:&#160;1&#160;:&#160;0), (2&#160;:&#160;1&#160;:&#160;1), (2&#160;:&#160;1&#160;:&#160;2), (2&#160;:&#160;2&#160;:&#160;1)}.
Let E(n) be the number of subsets of M(n) which can produce the mixture with ratio (1 : 1 : 1), i.e., the mixture with equal parts A, B and C. 
We can verify that E(1) = 103, E(2) = 520447, E(10)&#160;mod&#160;118 = 82608406 and E(500)&#160;mod&#160;118 = 13801403.
Find E(10&#160;000&#160;000)&#160;mod&#160;118.
