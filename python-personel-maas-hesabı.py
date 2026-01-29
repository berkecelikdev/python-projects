class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method!")
    
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
class Freelancer(Employee):
    def __init__(self, name, project_rate, completed_projects):
        super().__init__(name)
        self.project_rate = project_rate
        self.completed_projects = completed_projects

    def calculate_salary(self):
        return self.project_rate * self.completed_projects

employees = [FullTimeEmployee("Berke Çelik", 7000),
             PartTimeEmployee("Sema Çelik", 500, 80),
             Freelancer("Ali Çelik", 2500, 10)]

for item in employees:
    print(f"{item.name}: {item.calculate_salary()}")
