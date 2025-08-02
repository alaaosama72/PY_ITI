class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        self.employees = [emp for emp in self.employees if emp.emp_id != empId]
        Office.employeesNum -= 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.emp_id == empId:
                return emp
        return None

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        arrival_time = moveHour + time_needed
        return arrival_time > targetHour

    def check_lateness(self, empId, moveHour, velocity):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, velocity)
            if is_late:
                self.deduct(emp.emp_id, 10)
                print(f"{emp.name} is late! Salary deducted.")
            else:
                self.reward(emp.emp_id, 10)
                print(f"{emp.name} arrived on time! Salary rewarded.")
