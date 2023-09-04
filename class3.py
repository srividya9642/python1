class test:
    a=100
    def __init__(self):
        test.b=200
       
    def m1(self):
        test.c=300
    @classmethod
    def m2(cls):
        cls.d=400
        test.e=500
    @staticmethod
    def m3():
        test.f=600
t1=test()
t1.m1()
t1.m2()
t1.m3()
test.g=700
print(test.__dict__)




