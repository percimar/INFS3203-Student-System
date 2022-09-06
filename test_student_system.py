from unittest import TestCase
from student_system import StudentSystem, Student

class TestStudentSystem(TestCase):
    def test_add_student_success(self):
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertIs(student_system.students[1], test_student)

    
    def test_find_student_success(self):
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertIs(student_system.find_student(1), test_student)
    
    def test_delete_student_success(self):
        student_system = StudentSystem()
        test_student = Student("Asmar", 23, 1)

        student_system.add_student(test_student)

        self.assertTrue(student_system.delete_student(1))
        self.assertFalse(test_student.id in student_system.students)

    def test_add_student_exception(self):
        student_system = StudentSystem()
        
        with self.assertRaises(TypeError):
            student_system.add_student("Asmar", 23, 1)

    
    def test_find_student_not_exists(self):
        student_system = StudentSystem()
        
        self.assertEquals(student_system.find_student(1), None)

        test_student = Student("Asmar", 23, 1)
        student_system.add_student(test_student)

        self.assertEquals(student_system.find_student(0), None)

    
    def test_delete_student_not_exists(self):
        student_system = StudentSystem()
        
        self.assertFalse(student_system.delete_student(1))

        test_student = Student("Asmar", 23, 1)
        student_system.add_student(test_student)

        self.assertFalse(student_system.delete_student(0))
    
