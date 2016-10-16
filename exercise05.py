import pylab as pl
import math

g=9.8
B2m=0.00004
a=0.0065
T0=300
Alpha=2.5
dt=0.01

class cannon_trajectory:
    """
    programto calculate the trajectory of cannon
    """
    def __init__(self,v0,theta):
        self.v0=v0
        self.v0_=v0
        self.theta=theta*math.pi/180
        self.theta_=theta
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
    
    def F_drag(self,v_x,v_y,y=1):
        v=math.sqrt(v_x**2+v_y**2)
        self.Fx=-B2m*v_x*v*(1-a*y/T0)**Alpha
        self.Fy=-B2m*v_y*v*(1-a*y/T0)**Alpha
        return self.Fx,self.Fy

    def calculate(self):
        self.x=[0]
        self.y=[0]
        self.vx=[self.vx0]
        self.vy=[self.vy0]
        self.t=[0]
        while not(self.y[-1]<0):
            
            next_vx=self.vx[-1]-self.F_drag(self.vx[-1],self.vy[-1],self.y[-1])[0]*dt
            next_vy=self.vy[-1]-g*dt-self.F_drag(self.vx[-1],self.vy[-1])[1]*dt
            self.vx.append(next_vx)
            self.vy.append(next_vy)
            next_x=self.x[-1]+next_vx*dt 
            next_y=self.y[-1]+next_vy*dt
            self.x.append(next_x)
            self.y.append(next_y)
            
        r=-self.y[-2]/self.y[-1]
        self.x[-1]=(self.x[-2]+r*self.x[-1])/(r+1)
        self.y[-1]=0
    def plot(self,color):
        pl.title("cannon trajectory")
        pl.xlabel("x/Km")
        pl.ylabel("y/Km")
        temp_,=pl.plot(self.x,self.y,color,label="$v0=%dm/s$,$\\theta=%d\degree$"%(self.v0_,self.theta_))
        pl.legend(handles=[temp_], loc=4)

        
        
    
        
A=cannon_trajectory(500,45)
A.calculate()
A.plot("black")
pl.show()
