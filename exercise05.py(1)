import numpy
import math
import pylab as pl
class cannon_shell:
    def __init__(self, x_0, y_0, initial_velocity, theta_0, \
                 time_step, total_time):
        self.theta = theta_0
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [math.cos(theta_0 * math.pi / 180) * initial_velocity]
        self.v_y = [math.sin(theta_0 * math.pi / 180) * initial_velocity]
        self.g = 9.8
        self.dt = time_step
        self.time = total_time
    def run(self):
        for i in range(self.time):
            self.v_x.append(self.v_x[i])
            self.x.append(self.x[i] + self.dt * self.v_x[i])
            self.v_y.append(self.v_y[i] - self.g * self.dt)
            self.y.append(self.y[i] + self.dt * self.v_y[i])
            if self.y[i] >= 0 and self.y[i + 1] <= 0:
                break
        r = - self.y[-2] / self.y[-1]
        self.x[-1] = (self.x[-2] + r * self.x[-1]) / (r + 1)
        for j in range(len(self.x)):
            self.x[j] = self.x[j] / 1000
        for j in range(len(self.y)):
            self.y[j] = self.y[j] / 1000
        print "在初射角为", str(self.theta), "度时:"
        print "炮弹在水平方向的位移为：", self.x[-1], 'km'
        print "炮弹在竖直方向的最大高度为：", max(self.y), 'km'
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.ylim(0, 20)
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.text(self.x[450], self.y[500],\
                str(self.theta) +'$\degree$', fontdict = font)
        pl.text(35, 18,\
                'Euler Method', fontdict = font)
a = cannon_shell(0 , 0, 700, 30, 0.1, 1500)
a.run()
a.show_results()
a = cannon_shell(0 , 0, 700, 35, 0.1, 1500)
a.run()
a.show_results()
a = cannon_shell(0 , 0, 700, 40, 0.1, 1500)
a.run()
a.show_results()
a = cannon_shell(0 , 0, 700, 45, 0.1, 1500)
a.run()
a.show_results()
a = cannon_shell(0 , 0, 700, 50, 0.1, 1500)
a.run()
a.show_results()
a = cannon_shell(0 , 0, 700, 55, 0.1, 1500)
a.run()
a.show_results()
pl.show()
