class SalariedEmployee():
    def __init__(self, name='', salary=0):
        self.salary = salary
        self.name = name

    def calculatePay(self):
        print(self.name,"Salary is",self.salary)
        return self.salary


class HourlyEmployee():
    def __init__(self, name='', hour=0, hourlyworked=0):
        self.name = name
        self.hourlyRate = hour
        self.hourlyworked = hourlyworked

    def calculatePay(self):
        print(self.name,"Salary is",self.hourlyworked*self.hourlyRate)
        return self.hourlyworked * self.hourlyRate


Ram = SalariedEmployee('Ram',1000)
Raj =HourlyEmployee('Raj',40,50)
Raj.calculatePay()
Ram.calculatePay()
