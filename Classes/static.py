class Student:
    st_student_count = 0

    def __init__(self, name, id):
        self._name = name
        self._id = id
        Student.st_student_count += 1

    def __str__(self):
        return "{name}, {id}".format(name=self._name, id=self._id)

    def __del__(self):
        Student.st_student_count -= 1

    @property
    def student(self):
        print("Property")
        return self._name

    @student.setter
    def name(self, arg_name):
        print("P.Setter")
        self._name = arg_name

    @student.setter
    def id(self, arg_id):
        print("P.SetterID")
        self._id = arg_id

    @student.deleter
    def student(self):
        print("P.Deleter")
        del self._name
        del self._id


a = Student("Alex", 1)
b = Student("Macey", 2)
c = Student("Kosta", 3)
d = Student("Axoy", 4)
e = Student("Ksenia", 5)
print(Student.st_student_count)
del a, b, c
print(Student.st_student_count)
d.name = "Aksoy"
e.id = 6
print(d)
print(e)
print(Student.st_student_count)
