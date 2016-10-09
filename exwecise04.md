## 一 摘要
一个系统中有A，B两种粒子，他们之间可以互相转化，并最终达到平衡。衰变的方程为：    
![ ][1]     
![ ][2]    
考虑不同初始值时方程的解（Na=100，Nb=0），并验证。

---
## 二 正文
推导方程的解：    
用欧勒法，对Na进行泰勒展开并舍弃二阶小量：    
![ ][3]    
将Na代入得：    
![ ][4]    
同理可得：    
![ ][5]    
Na=100  Nb=0

Code：（https://github.com/vakie/compuational_physics_N2014301020089/blob/master/exercise04.py）

result：    
![ ][6]    
Na=80  Nb=20    
result:    
![ ][7]

## 三 结论

两种粒子最终会达到一种平衡状态，数量将达到总数的一半，两种粒子的衰变速度将相等
  
## 四 致谢
参考了李贤达和郭忠志同学的代码，在此谢谢

  [1]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/CodeCogsEqn_raw%3Dtrue.gif
  [2]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/CodeCogsEqn%2520(1)_raw%3Dtrue.gif
  [3]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/CodeCogsEqn%2520(2)_raw%3Dtrue.gif
  [4]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/CodeCogsEqn%2520(3)_raw%3Dtrue.gif
  [5]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/CodeCogsEqn%2520(4)_raw%3Dtrue.gif
  [6]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/123.png
  [7]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/234.png
