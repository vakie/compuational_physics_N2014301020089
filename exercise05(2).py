#exact solution
class exact_solution:
    def __init__(self, x_0, y_0, initial_velocity, theta_0):
        self.theta = theta_0
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = math.cos(theta_0 * math.pi / 180) * initial_velocity
        self.v_y = math.sin(theta_0 * math.pi / 180) * initial_velocity
        self.t = numpy.linspace(0, 150)
    def run(self):
        for i in self.t:
            self.x.append(exact_solution.xshift(self, i))
            self.y.append(exact_solution.yshift(self, i))
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
        pl.xlim(0, 60)
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.text(self.x[15], self.y[15],\
                str(self.theta) +'$\degree$', fontdict = font)
        pl.text(35, 18,\
                'Exact Solution', fontdict = font)        
    def xshift(self, t):
        return self.v_x * t + self.x[0]
    def yshift(self, t):
        return -(9.8 * t ** 2) / 2 + self.v_y * t + self.y[0]
b = exact_solution(0, 0, 700, 30)
b.run()
b.show_results()
b = exact_solution(0, 0, 700, 35)
b.run()
b.show_results()  
b = exact_solution(0, 0, 700, 40)
b.run()
b.show_results() 
b = exact_solution(0, 0, 700, 45)
b.run()
b.show_results()   
b = exact_solution(0, 0, 700, 50)
b.run()
b.show_results()
b = exact_solution(0, 0, 700, 55)
b.run()
b.show_results()
pl.show()
