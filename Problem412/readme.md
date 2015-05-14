
For integers m, n (0&#160;&#8804;&#160;n&#160;<&#160;m), let L(m,&#160;n) be an m&#215;m grid with the top-right n&#215;n grid removed.
For example, L(5, 3) looks like this:

We want to number each cell of L(m,&#160;n) with consecutive integers 1, 2, 3, ... such that the number in every cell is smaller than the number below it and to the left of it.
For example, here are two valid numberings of L(5,&#160;3):

Let LC(m, n) be the number of valid numberings of L(m, n).
It can be verified that LC(3,&#160;0) = 42, LC(5,&#160;3) = 250250, LC(6,&#160;3) = 406029023400 and LC(10,&#160;5) mod 76543217 = 61251715.
Find LC(10000,&#160;5000) mod 76543217.
