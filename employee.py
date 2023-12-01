"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class HourlyContract:
    def __init__(self, hourly_pay, hours):
        self.hourly_pay = hourly_pay
        self.hours = hours

    def get_pay(self):
        return self.hourly_pay * self.hours

    def __str__(self):
        string = f'a contract of {self.hours} hours at {self.hourly_pay}/hour'
        return string

class SalaryContract:
    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        string = f'a monthly salary of {self.salary}'
        return string

class BonusCommission:
    def __init__(self, bonus):
        self.bonus = bonus

    def get_pay(self):
        return self.bonus

    def __str__(self):
        return f'a bonus commission of {self.bonus}'


class ContractCommission:
    def __init__(self, contracts, commission):
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return self.contracts * self.commission

    def __str__(self):
        return f'a commission for {self.contracts} contract(s) at {self.commission}/contract'

class Employee:
    def __init__(self, name, contract, commission = None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        pay = self.contract.get_pay()
        if self.commission:
            pay += self.commission.get_pay()
        return pay

    def __str__(self):
        contract_str = str(self.contract)
        commission_str = f' and receives {str(self.commission)}' if self.commission else ''
        total_pay_str = f'. Their total pay is {self.get_pay()}.'

        return f'{self.name} works on {contract_str}{commission_str}{total_pay_str}'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))
