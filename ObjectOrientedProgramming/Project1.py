#create the employee Management class:

class employeeManagement:
    EmployerRetirementPer = 0.5
    vacaPerWeek = 2
    vacaB1 = 0.1
    vacaB2 = 0.2
    vacaB3 = 0.3
    vacaB4 = 0.4
    vacaB5 = 0.5

    # class constructor/initializer
    def __init__(self, first, last, salaryAnnual, bonusAnnual, years, EmployeeRetirement):
        self.first = first
        self.last = last
        self.salaryAnnual = salaryAnnual
        self.bonusAnnual = bonusAnnual
        self.years = years
        self.EmployeeRetirement = EmployeeRetirement

    #create methods for the various calculations involved

    def calcBonus(self):
        return self.salaryAnnual * self.bonusAnnual

    def calcVacaHrs (self):
        VacaHrs = self.vacaPerWeek * 52

        if self.years == 1:
            bonusVacaHrs = VacaHrs * self.vacaB1
        if self.years == 2:
            bonusVacaHrs = VacaHrs * self.vacaB2
        if self.years == 3:
            bonusVacaHrs = VacaHrs * self.vacaB3
        if self.years == 4:
            bonusVacaHrs = VacaHrs * self.vacaB4
        if self.years >= 5:
            bonusVacaHrs = VacaHrs * self.vacaB5
        return round(VacaHrs + bonusVacaHrs, 2)

    def totalRetirementFund(self):
        rf = self.salaryAnnual * self.retirementPack

        if self.EmployeeRetirement <= .05:
            erf = rf * self.EmployerRetirementPer
            return rf + erf
        if self.EmployeeRetirement > 0.5:
            rf5 = self.salaryAnnual * 0.005
            rf = rf5 * self.EmployerRetirementPer
            return rf + erf
