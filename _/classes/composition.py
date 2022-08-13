class Salary:
    def __init__(self, pay) -> None:
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus
        self.salary_obj = Salary(self.pay)

    def annual_salary(self):
        return f'Total: {self.salary_obj.get_total()+self.bonus}'


employee = Employee(10, 50)
print(employee.annual_salary())
