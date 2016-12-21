class cobweb(object):
    def __init__(self):
        len = 2720
        Z=2
        self.side1 = [(len / 2, 0),
                      (len / 2, len),
                      ((len / 2) * 1 / 10, len),
                      ((len / 2) * 1 / 10, len-Z),
                      (len / 2, len-Z),
                      (len / 2, 0-Z),
                      (len/20,-Z)
                      ]
        self.side2 = [(-len / 2, 0),
                      (-len / 2, -len),
                      ((-len / 2) * 1 / 10, -len),
                      ((-len / 2) * 1 / 10, len - Z),
                      (-len / 2, len - Z),
                      (-len / 2, 0 - Z),
                      (-len/20,-Z)
                      ]

    def show(self):
        pre = (0, 0)
        for a in self.side1:
            print('{:8} {:8} {:8}, {:8} {:8} {:8}'.format(pre[0], pre[1],0, a[0], a[1],0))
            pre = a
        pre = (0, 0)
        for a in self.side2:
            print('{:8} {:8} {:8}, {:8} {:8} {:8}'.format(pre[0], pre[1],0, a[0], a[1],0))
            pre = a
