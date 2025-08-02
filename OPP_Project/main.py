from car import Car
from employee import Employee
from office import Office

if __name__ == "__main__":
    # Create Samy's car
    car = Car("Fiat 128", 100, 60)

    # Create Samy as an employee
    samy = Employee("Samy", 500, "Happy", 100, 1, car, "samy@iti.org", 3000, 20)

    # Create the office
    iti = Office("ITI Smart Village")
    iti.hire(samy)

    print("=== Samy's Day ===")

    # Samy sleeps 6 hours
    samy.sleep(6)
    print(f"After sleep: Mood = {samy.mood}")

    # Samy eats 2 meals
    samy.eat(2)
    print(f"After eating: Health = {samy.healthRate}%")

    # Samy buys 3 items
    samy.buy(3)
    print(f"After buying: Money = {samy.money} L.E")

    # Samy drives to work at 60 km/h
    drive_speed = 60
    samy.drive(drive_speed)

    # Check lateness (left home at 7:30)
    iti.check_lateness(1, 7.5, drive_speed)

    print(f"Final Salary: {samy.salary} L.E")
