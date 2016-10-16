# Homework5



---

##摘要：
我选择2.6题，本题是炮弹发射抛物线运动的近似计算，用Euler Method进行数值近似运算，并用解析的方法求得常微分方程的解析解

---
##正文：
公式推导   

![ ][1]    

引入速度Vx,Vy

![ ][2]

应用欧拉方法

![ ][3]

用解析的求法

![ ][4]   

欧拉方法代码

Code: (https://github.com/vakie/compuational_physics_N2014301020089/blob/master/exercise05(1).py)

结果图如下

![ ][5]

解析方法代码

Code: (https://github.com/vakie/compuational_physics_N2014301020089/blob/master/exercise05(2).py)

结果图如下

![ ][6]

---
##结论
两种方法数据有所不同，可根据实际情况对数据进行取舍，如果对所考虑问题的精度造成的影响不大，则可以选择欧拉方法进行近似计算。

---
##致谢
感谢郭忠志同学的代码支援

  [1]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/1.png
  [2]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/2.png
  [3]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/3.png
  [4]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/4.png
  [5]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/5.png
  [6]: https://github.com/vakie/compuational_physics_N2014301020089/blob/master/6.png
