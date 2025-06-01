# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# factorial(10)

# def curr_con(n):
#     print("USD to INR:",n*82.8)
# curr_con(100)

# def even_odd():
#     n=int(input("Enter a number"))
#     if n % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
# print(even_odd())

# def show(n):
#     print(n)
#     if n > 1:
#         show(n-1)
# show(10)

# def fact_recursive(n):
#     if (n == 1) or (n == 0):
#         return 1
#     else:
#         return n * fact_recursive(n-1)
# print(fact_recursive(5))

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n + sum(n-1)
# print(sum(20))

# def printList(list, index):
#     if index == len(list):
#         return 0
#     else:
#         print(list[index])
#         printList(list, index+1)
# printList([1,2,3,4,5,6,7,8,9,0], 1)

# f = open('demo.txt', 'r')
# data = f.readline()
# print(data)
# data2 = f.readline()
# print(data2)

# print(type(data))
# f.close()


# f=open('demo.txt', 'a')
# f.write('\ni am tired and bored')
# f.close()

# import os
# os.remove('demo.txt')

# with open("demo.txt", "r") as f:
#     data = f.read()
# newData = data.replace("Java","Python")
# print(newData)
# with open("demo.txt", "w") as f:
#     f.write(newData)

# class student:
#     def __init__(self, fullName):
#         self.naam = fullName
#         print("Student rocks")
# s1 = student("karan")
# print(s1.naam)

# class student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#     def calculate_average(self):
#         return (self.sub1 + self.sub2 + self.sub3) / 3
# s1 = student("John Doe", 90, 85, 95)
# print(s1.calculate_average())

# class account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_number = acc
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#     def get_balance(self):
#         return self.balance
# acc1 = account(1000, 12345)
# print(acc1.get_balance())
# acc1.deposit(500)
# print(acc1.get_balance())
# acc1.withdraw(200)
# print(acc1.get_balance())

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
# circle1 = circle(5)
# print(circle1.area())
# print(circle1.perimeter())

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showDetails(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")
# class Engineer(Employee):
#     def __init__(self, name, age):
#         name = self.name
#         age = self.age

 