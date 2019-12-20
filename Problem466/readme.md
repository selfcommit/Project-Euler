

table.p466, table.p466 th, table.p466 td {
  border-width: 1px 1px 1px 1px;
  border-style: solid solid solid solid;
  border-color: black black black black;
  text-align:right;
  -moz-border-radius: 0px 0px 0px 0px;
}
table.p466 {
  table-layout: fixed;
  border-spacing: 1px;
  border-collapse: separate;
  background-color: rgb(224,237,252);
}
table.p466 th, table.p466 td {
  padding: 1px 6px 1px 6px;
  width: 20%;
}
table.p466 th { background-color: rgb(193,218,249); }
table.p466 td { background-color: rgb(255,255,255); }

Let P(m,n) be the number of distinct terms in an m&#215;n multiplication table.
For example, a 3&#215;4 multiplication table looks like this:

&#215; 1234
1 1234
2 2468
3 36912

There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.
You are given that:
P(64,64) = 1263,
P(12,345) = 1998, and
P(32,1015) = 13826382602124302.
Find P(64,1016).
