from unittest import TestCase
from student import Student

class TestStudent(TestCase):
    def test_id_getter(self):
        test_student = Student("Asmar", 23, 1)

        self.assertEqual(test_student.id, 1)

    
    def test_name_getter(self):
        test_student = Student("Asmar", 23, 1)

        self.assertEqual(test_student.name, "Asmar")

    
    def test_age_getter(self):
        test_student = Student("Asmar", 23, 1)

        self.assertEqual(test_student.age, 23)

    def test_no_id_exception(self):
        with self.assertRaises(TypeError):
            Student("Asmar", 23)
    
    def test_no_name_exception(self):
        with self.assertRaises(TypeError):
            Student(age=23, id=1)
    
    def test_no_age_exception(self):
        with self.assertRaises(TypeError):
            Student("Asmar", id=1)
    
    def test_wrong_id_type_exception(self):
        with self.assertRaises(TypeError):
            Student("Asmar", 23, "1")
        
        with self.assertRaises(TypeError):
            Student("Asmar", 23, True)
        
        with self.assertRaises(TypeError):
            Student("Asmar", 23, 1.0)
    
    def test_wrong_age_type_exception(self):
        with self.assertRaises(TypeError):
            Student("Asmar", "23", 1)
        
        with self.assertRaises(TypeError):
            Student("Asmar", False, 1)
        
        with self.assertRaises(TypeError):
            Student("Asmar", 23.0, 1)
        
    def test_wrong_name_type_exception(self):
        with self.assertRaises(TypeError):
            Student(True, 23, 1)
        
        with self.assertRaises(TypeError):
            Student(5, 23, 1)
        
        with self.assertRaises(TypeError):
            Student(['A', 's', 'm', 'a', 'r'], 23, 1)
        

    