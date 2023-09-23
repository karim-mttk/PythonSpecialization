class Employee:
    def __init__(self, first_name, last_name, emp_id, years_of_experience):
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.years_of_experience = years_of_experience

    def get_monthly_salary(self):
        pass

    def get_annual_bonus(self):
        pass

class FullTimeManagementEmployees(Employee):

    __management_bonus_percentage = 20
    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.annual_salary = annual_salary

    def get_monthly_salary(self):
        return round(self.annual_salary /12, 2)

    def get_annual_bonus(self):
        std_bonus = self.annual_salary * (self.__management_bonus_percentage / 100)
        exp_bonus = std_bonus * (self.years_of_experience/100)
        return std_bonus + exp_bonus

class FullTimeSalariedEmployee(Employee):
    __employee_bonus_percentage = 5

    def __init__(self, first_name, last_name, emp_id, years_of_experience, annual_salary):
        super().__init__(first_name, last_name, emp_id, years_of_experience)
        self.annual_salary = annual_salary

    def get_monthly_salary(self):
        return round(self.annual_salary /12, 2)

    def get_annual_bonus(self):
        std_bonus = self.annual_salary * (self.__employee_bonus_percentage / 100)
        exp_bonus = std_bonus * (self.years_of_experience/100)
        return std_bonus + exp_bonus






