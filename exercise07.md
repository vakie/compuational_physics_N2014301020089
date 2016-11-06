# Homework7



---

##摘要：
模拟物理摆在收阻尼和周期性驱动力之后的运动。

---
##正文：
公式推导：由euler-cromer方法可得：    
![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;%5B-%28g/l%29sin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)    

![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)    
![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i%20&plus;%5CDelta%20t)    

当周期性驱动力F_d较大时，物理摆将出现混沌现象。  


---
结论：
result：    
t=2nπ/Ω时    
![](https://github.com/vakie/compuational_physics_N2014301020089/blob/master/01.png) 

t=(2nπ+π/4)/Ω时    
![](https://github.com/vakie/compuational_physics_N2014301020089/blob/master/02.png)    
可以看出其分布特点大致相同。


---
##致谢：
参考了李贤达同学的代码，在此致谢。
