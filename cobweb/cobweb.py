class cobweb(object):
    def __init__(self):
        L = 2.75    #Dimensions of the Square
        ActiveLength=2.72 
        ReflecLen=2.41
	self.L=L
        Z=0.005
        self.Z=Z
        self.side1 = [(L / 2, 0  ,0),
                      (L / 2, L/2,0),
                      (L / 2, L/2,Z),
                      (L / 2, 0  ,Z),
        	      ((L/100)*3,0,Z) 
                      ]
        self.side2 = [(-L / 2, 0  ,0),
                      (-L / 2, L/2,0),
                      (-L / 2, L/2,Z),
                      (-L / 2, 0  ,Z),
        	      ((-L/100)*3,0,Z) 
                      ]
        #Start from 1st Tuple
	#These are the unterminated parts
	self.loop1 = [ (L / 2, L/2,0),
                       (L/2  , L  ,0),
                       (L/10*1,L  ,0)
		     ]
	self.loop2 = [ (L / 2, L/2,Z),
                       (L/2  , L  ,Z),
                       (L/10*1,L  ,Z)
		     ]

	self.loop3 = [ (-L / 2, L/2,0),
                       (-L/2  , L  ,0),
                       (-L/10*1,L  ,0)
		     ]
	self.loop4 = [ (-L / 2, L/2,Z),
                       (-L/2  , L  ,Z),
                       (-L/10*1,L  ,Z)
		     ]




    def output(self,pre,a):
        print('{:8.4f},\t{:8.4f},\t{:8.4f},\t{:8.4f},\t{:8.4f},\t{:8.4f},\t8.000e-04,\t-1'.format(pre[0], pre[1],pre[2], a[0], a[1],a[2]))


    def show(self):
        #pre = (-1*self.L/2,0, 0.05)
        #a=(self.L/2,0,0.05)
        #self.output(a,pre)
        pre = (-1*self.L/2,0, 0)
        a=(self.L/2,0,0)
        self.output(a,pre)

	ele=[self.side1, self.side2,self.loop1, self.loop2, self.loop3,self.loop4]
	for data_element in ele:
	    pre=data_element[0]
            for a in data_element[1:]:
               self.output(pre,a)
               pre=a


