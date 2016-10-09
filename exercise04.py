import pylab as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Program to solve 1.5
    """
    def __init__(self,Na=100,Nb=0,time_constant=1,time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.Na=[Na]
        self.Nb=[Nb]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial Na ->", Na)
        print("Initial Nb ->", Nb)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
	
    def calculate(self):
        for i in range(self.nsteps):
            tmp_a=self.Na[i] + (self.Nb[i] / self.tau - self.Na[i] / self.tau) * self.dt
            tmp_b=self.Nb[i] + (self.Na[i] / self.tau - self.Nb[i] / self.tau) * self.dt
            self.Na.append(tmp_a)
            self.Nb.append(tmp_b)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
            pl.plot(self.t, self.Na)
            pl.plot(self.t, self.Nb)
            pl.xlabel('time ($s$)')
            pl.ylabel('Number of Nuclei')
            pl.show()
		
#matplotlib inline
a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()
