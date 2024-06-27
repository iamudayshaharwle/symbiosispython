class employee :
    def __init__(self, name, salary, phone_no, address):
        self.name = name
        self.salary=salary
        self.phone_no =phone_no
        self.address =address

    def print(self):
        return f'name is {self.name} his salary is {self.salary},phone number: {self.phone_no} and address: {self.address}'


worker1 = employee('rick','2000000','8787877','us')
worker2 = employee('negen','35000','987764','new york')


print(worker1.print())
print(worker2.print())

