class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Init SchoolMember: {}'.format(self.name))
    def tell(self):
        print('name:"{}" age:"{}"'.format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Init Teacher: {}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
        print('Init Teacher: {}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('score: "{:d}'.format(self.score))


t = Teacher('Mr. Jeff', 45, 5000000)
s = Student('Joy', 24, 80)

print()

members = [t,s]
for member in members:
    member.tell()
