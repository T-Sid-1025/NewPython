employeeArr = []

class Employee:

    @staticmethod
    def displayEmployee():
        for j in range(len(employeeArr)):
            for k in range(1):
                for i in range(1):
                    print(employeeArr[j]["id"], end=" ")
                    print(employeeArr[j]["name"], end=" ")
                    print(employeeArr[j]["mobno"], end=" ")
                    print(employeeArr[j]["altmob"], end=" ")
                    print(employeeArr[j]["email"], end=" ")
                    print(employeeArr[j]["city"], end=" ")
                    print(employeeArr[j]["group"], end=" ")
                    print(employeeArr[j]["address"], end=" ")
                print()

    @staticmethod
    def addEmployee():
        print("-------------------------------------------")
        limit = int(input("Enter the limit: "))
        for i in range(limit):
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee name: ")
            employee_mobno = input("Enter mobile no: ")
            employee_altmob = input("Enter alternate mobile no: ")
            employee_email = input("Enter email: ")
            employee_city = input("Enter city: ")
            employee_group = input("Enter group: ")
            employee_address = input("Enter address: ")
            temp = {
                "id": employee_id,
                "name": employee_name,
                "mobno": employee_mobno,
                "altmob": employee_altmob,
                "email": employee_email,
                "city": employee_city,
                "group": employee_group,
                "address": employee_address
            }
            employeeArr.append(temp)
        print("-------------------------------------------")

    @staticmethod
    def searchEmployee():
        s_id = input("Enter Employee ID: ")
        for k in range(len(employeeArr)):
            if employeeArr[k]["id"] == s_id:
                print(employeeArr[k]["id"], end=" ")
                print(employeeArr[k]["name"], end=" ")
                print(employeeArr[k]["mobno"], end=" ")
                print(employeeArr[k]["altmob"], end=" ")
                print(employeeArr[k]["email"], end=" ")
                print(employeeArr[k]["city"], end=" ")
                print(employeeArr[k]["group"], end=" ")
                print(employeeArr[k]["address"], end=" ")
                break
        else:
            print("Employee not found.")

    @staticmethod
    def updateEmployee():
        sid = input("Enter Employee ID to update: ")
        for l in range(len(employeeArr)):
            if employeeArr[l]["id"] == sid:
                employee_id = input("Enter new Employee ID: ")
                employee_name = input("Enter new Employee name: ")
                employee_mobno = input("Enter new mobile no: ")
                employee_altmob = input("Enter new alternate mobile no: ")
                employee_email = input("Enter new email: ")
                employee_city = input("Enter new city: ")
                employee_group = input("Enter new group: ")
                employee_address = input("Enter new address: ")
                temp1 = {
                    "id": employee_id,
                    "name": employee_name,
                    "mobno": employee_mobno,
                    "altmob": employee_altmob,
                    "email": employee_email,
                    "city": employee_city,
                    "group": employee_group,
                    "address": employee_address
                }
                employeeArr[l] = temp1
                print("Employee updated successfully.")
                break
        else:
            print("Employee not found.")

    @staticmethod
    def groupEmployee():
        group_name = input("Enter group name: ")
        for m in range(len(employeeArr)):
            if employeeArr[m]["group"] == group_name:
                print(employeeArr[m]["id"], end=" ")
                print(employeeArr[m]["name"], end=" ")
                print(employeeArr[m]["mobno"], end=" ")
                print(employeeArr[m]["altmob"], end=" ")
                print(employeeArr[m]["email"], end=" ")
                print(employeeArr[m]["city"], end=" ")
                print(employeeArr[m]["group"], end=" ")
                print(employeeArr[m]["address"], end=" ")
                print("*")


c = Employee
con = 1

while con != 0:
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. View by Group")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        c.addEmployee()
    elif choice == 2:
        c.displayEmployee()
    elif choice == 3:
        c.searchEmployee()
    elif choice == 4:
        c.updateEmployee()
    elif choice == 5:
        c.groupEmployee()
    elif choice == 6:
        print("Bye bye!")
        con = 0
    else:
        print("Invalid choice!")
        print("For exit press 6 and for main menu press between 1 to 5")
