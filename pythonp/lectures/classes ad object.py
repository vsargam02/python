class computer:
    def __init__(self):
        self.name='navin'
        self.age=26

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            False

c1 =computer()
c1.age=30
c2 =computer()

if c1.compare(c2):
    print('they are sme')
else:
    print('they are different')

c1.name='rashi'
c1.age =27

#c1.update()
#c2.update()

# print(c1.name)
# print(c2.name)
print(c1.name,c1.age)
print(c2.name,c2.age)