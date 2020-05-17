from comemp import CommissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(CommissionEmployee):

    def __init__(self, first_name, last_name, ssn,
                gross_sales, commission_rate, base_salary):
                """Initialize SalariedCommissionEmployee`s attributes """
                super().__init__(first_name, last_name, ssn,
                                gross_sales, commission_rate)

                self._base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        if salary < Decimal("0.00"):
            raise ValueError("Base salary must be >= 0")

            self._base_salary = salary

    def earning(self):
        return super().earnings() + self.base_salary

    def __repr__(self):
        return("Salaried" + super().__repr__() +
        f'\nbase salary: {self.base_salary:.2f}')
