class A:

    def instance_mthod(self):
        print('Instance Method')
        print(f'''Instance method means it contains self variable 
        for reference of object address is called instance method''')

    @classmethod
    def cls_method(cls):
        print("Class methods can using decorators concepts")
        print('Class methods can taking CLASS Name As reference is called Class Methods....')
        print('Class methods no need object creating because of it can taking self parameter as class name...')


A.cls_method()
a = A()
a.instance_mthod()
