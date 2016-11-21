#Sinai billiard
from __future__ import division, print_function
from visual import *
r=0.6
rb2=(2.+0.5*r)**2
L=8
side = 8.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
wallR = box (pos=( L, 0, 0), size=(thk, s2, s3),  color = (0.7, 0.7, 0.7))
wallL = box (pos=(-L, 0, 0), size=(thk, s2, s3),  color = (0.7, 0.7, 0.7))
wallB = box (pos=(0, -L, 0), size=(s3, thk, s3),  color = (0.7, 0.7, 0.7))
wallT = box (pos=(0, L, 0), size=(s3, thk, s3),  color = (0.7, 0.7, 0.7))
wallBK = box(pos=(0, 0, -0.5), size=(s2, s2, thk), color = color.green)
inner=sphere(pos=(0,0,0), radius=2, color=color.cyan) #Fixed obstacle
ball=sphere(pos=(2,3,0),radius=r,color=color.red,make_trail=True,retain=200) # Moving ball
ball.trail_object.radius = 0.05
v0=vector(1,-1.01,0)
ball.v=v0
trail=curve()
vel=sqrt(ball.v.x**2+ball.v.y**2)
dt=0.05
for i in arange(15000):
    rate(1000)
    ball.pos=ball.pos+ball.v*dt # update position
    if mod(i,20)==0:
        trail.append(pos=ball.pos) #sample position, sample time= 20*dt
    if not L>ball.x > -L: #bounce off walls
        ball.v.x=-ball.v.x
    if not L>ball.y >- L:
        ball.v.y=-ball.v.y
    rball2=ball.x**2+ball.y**2
    phinew=atan2(ball.v.y,ball.v.x)
    if rball2 < rb2: #bounce off ball in middle
        theta=atan2(ball.y,ball.x)
        phi=atan2(ball.v.y,ball.v.x)
        alpha=phi-theta
        phinew=theta-alpha
        ball.v=vector(-vel*cos(phinew),-vel*sin(phinew),0)
    phinew=atan2(ball.v.y,ball.v.x)
