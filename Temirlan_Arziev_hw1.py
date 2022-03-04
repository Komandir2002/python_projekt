class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married):
        print(f"fullname: {full_name} \n age: {age} \n is_married: {is_married}")

    def output(self,):
        return f"full name {self.full_name}\n" \
               f"age {self.age}\n" \
               f"is married {self.is_married}\n" \



class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        Person.__init__(self, full_name, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) / 5)

class Teacher(Person):
    salary = 1200
    def __init__(self, full_name, age, is_married, experience=3):
        Person.__init__(self, full_name, age, is_married)
        self.experience = experience


    def Teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary

uchilka = Teacher("Абдумалик", 26, False, 5)

print(f'{uchilka.full_name} {uchilka.age} {uchilka.is_married} {uchilka.experience}')
print(uchilka.Teacher_cash())

def create_students():
    student1 = Student(full_name="Марат", age=22, is_married=True, marks={
        "биология": 5,
        "история": 4,
        "математика": 5,
        "физика": 2,
        "русский-язык": 3,
    })
    student2 = Student(full_name="Бексултан", age=15, is_married=False, marks={
        "биология": 4,
        "история": 5,
        "математика": 2,
        "физика": 5,
        "русский-язык": 4,
    })
    student3 = Student(full_name="Юрий", age=19, is_married=False, marks={
        "биология": 5,
        "история": 1,
        "математика": 5,
        "физика": 4,
        "русский-язык": 2,
    })

    resultu = [student1, student2, student3]
    return resultu

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.full_name}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Average marks: {sum(list)/len(list)}\n")