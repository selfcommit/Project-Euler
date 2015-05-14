

Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices any of the given points and not containing any of the given points in its interior (in addition to the vertices, other given points may lie on the perimeter of the polygon). 


As an example, the image below shows a set of twenty points and a few such convex holes. 
The convex hole shown as a red heptagon has an area equal to 1049694.5 square units, which is the highest possible area for a convex hole on the given set of points.





table.p252 td {
  padding: 0px 3px 0px 3px;
  vertical-align: bottom;
  text-align: left;
}

For our example, we used the first 20 points (T2k&#8722;1,&#8201;T2k), for k&#8201;=&#8201;1,2,&#8230;,20, produced with the pseudo-random number generator:


S0
=&#160;
290797&#160;

Sn+1
=&#160;
Sn2 mod 50515093

Tn
=&#160;
(&#8201;Sn mod 2000&#8201;) &#8722; 1000&#160;



i.e. (527,&#8201;144), (&#8722;488,&#8201;732), (&#8722;454,&#8201;&#8722;947), &#8230;


What is the maximum area for a convex hole on the set containing the first 500 points in the pseudo-random sequence? Specify your answer including one digit after the decimal point.

