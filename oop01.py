class Employee:

    # class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variable
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # accessing the class variable BUT....

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Example using a class method as a constuctor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-') # parsing the param
        return cls(first, last, pay)    # Effectively creating an object from the class constructor: Employee(self, first, last, pay) 
                                        # and returning that object as:
                                        # new_employee = Employee.from_string('Tony-Lacson-8000')

    @staticmethod
    def is_workday(day):  # Static methods don't take 'self' or 'cls' as parameters and hence the method should have no association with instance or class attributes.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
            