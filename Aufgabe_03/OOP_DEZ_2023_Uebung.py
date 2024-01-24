from enum import Enum

class Gender(Enum):
    female = 0
    male = 1

class Person:
    person_count = 0
    gender_count = {Gender.female: 0, Gender.male: 0}

    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        Person.person_count += 1
        Person.gender_count[gender] += 1

    def percentage_gender():
        return Person.gender_count[Gender.male] / Person.person_count, \
                Person.gender_count[Gender.female] / Person.person_count

class Employee(Person):
    employee_count = 0

    def __init__(self, firstname, lastname, gender, strength):
        super().__init__(firstname, lastname, gender)
        self.department = None
        self.strength = strength
        Employee.employee_count += 1


class Department_Head(Employee):
    department_head_count = 0

    def __init__(self, firstname, lastname, gender, strength):
        super().__init__(firstname, lastname, gender, strength)
        Department_Head.department_head_count += 1


class Department:
    department_count = 0
    department_strength = {}

    def __init__(self, name, department_head):
        self.name = name
        self.employee = []
        self.department_head = department_head
        self.department_head.department = self
        Department.department_count += 1

    def add_employee(self, employee):
        self.employee.append(employee)
        employee.department = self
        Department.department_strength[self.name] = self.employee_strength()

    def employee_strength(self):
        count = 0
        for employee in self.employee:
            count += employee.strength
        return count

class Company:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

if __name__ == "__main__":
    person1 = Person("Tobias", "Hauser", Gender.male)
    person2 = Person("Sahra", "Mueller", Gender.female)
    employee1 = Employee("Julian", "Jungmann", Gender.male, 150)
    department_head1 = Department_Head("Max", "Mustermann", Gender.male, 200)
    department1 = Department("Hardware", department_head1)
    department2 = Department("Software", department_head1)
    department1.add_employee(employee1)
    department2.add_employee(department_head1)
    departments_list = [department1, department2]
    company1 = Company("FischerGmbH", departments_list)
    print(f"Der Name der Firma lautet: {company1.name}" + f" und besitzt folgende Abteilungen: {company1.departments[0].name, company1.departments[1].name}")
    print(f"Die Anzahl der Mitarbeiter beträgt: {Employee.employee_count}")
    print(f"Die Anzahl der Abteilungsleiter beträgt: {Department_Head.department_head_count}")
    print(f"Die Anzahl der Abteilungen beträgt: {Department.department_count}")
    print(f"Die Stärkste Abteilung ist: {max(Department.department_strength)}")
    print(f"Prozentueller Anteil zwischen Männern und Frauen: {Person.percentage_gender()}")