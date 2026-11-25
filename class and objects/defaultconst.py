class D:
    def __init__(self):
        print("This is a default constructor")

a=D()

#This error pops up when there is no self 
#    a=D()
#      ^^^
#TypeError: D.__init__() takes 0 positional arguments but 1 was given

