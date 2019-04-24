##### An ant is standing on one corner of a cube and can only walk on the edges. The ant is drunk and from any corner, it moves randomly by choosing any edge! What is the expected number of edges the ant travels, to reach the opposite corner?

---

Let the expected number of step required to go from (0,0,0) to (1,1,1) be $E_0$. 

Also let expected number of step required to reach (1,1,1) from (0,0,1)(Or from (0,1,0) or from (1,0,0)) be $E_1$. 

Similarly expected number of step required to reach (1,1,1) from (0,1,1) (Or from (1,0,1) or from (1,1,0)) be $E_2$.

Then we can write:
$E_0=1/3(E_1+E_1+E_1)+1$
$E_1= 1/3E_0 + 2/3E_2 + 1$
$E_2 = 2/3E_1 + 1$
solving this we find $E_0$ as 10.

