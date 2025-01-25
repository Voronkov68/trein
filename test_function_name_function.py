import unittest
from name_function import name_function as f 


class Test_Function_name_function(unittest.TestCase):
	'''Тесты для функции name_function'''

	def test_name_and_latname(self):
		'''Тестирует что правильно функция работатет с именем и фамилией'''
		name_lastname = f('Саша', 'Воронков')
		self.assertEqual(name_lastname, 'Воронков Саша')


	def test_full_name(self):
		'''Тестирует что правильно функция работет с полными именами'''
		name_fullname = f('Александр', 'Воронков', 'Альбертович')
		self.assertEqual(name_fullname, 'Воронков Александр Альбертович')









if __name__ == '__main__':
	unittest.main()
