class cobweb(object):
    def __init__(self):
        L = 2.720
	self.L=L
        Z=0.02
        self.side1 = [(L / 2, 0),
                      (L / 2, L),
                      ((L / 2) * 1 / 10, L),
                      ((L / 2) * 1 / 10, L-Z),
                      (L / 2, L-Z),
                      (L / 2, 0-Z),
                      (L/20,-Z)
                      ]
        self.side2 = [(-L / 2, 0),
                      (-L / 2, L),
                      ((-L / 2) * 1 / 10, L),
                      ((-L / 2) * 1 / 10, L - Z),
                      (-L / 2, L - Z),
                      (-L / 2, 0 - Z),
                      (-L/20,-Z)
                      ]

    def output(self,pre,a):
        print('{:8},\t{:8},\t{:8},\t{:8},\t{:8},\t{:8},\t8.000e-04,\t-1'.format(pre[0], pre[1],0, a[0], a[1],0))

    def show(self):
        pre = (-1*self.L/2, 0)
        a=(self.L/2,0)
        self.output(a,pre)


        pre=self.side1[0]
        for a in self.side1[1:]:
            self.output(pre,a)
            pre=a


        pre=self.side2[0]
        for a in self.side2[1:]:
            self.output(pre,a)
            pre=a
