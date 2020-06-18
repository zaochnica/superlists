from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''

    def setUp(self) -> None:  # def setUp(self): по книге
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:  # def tearDown(self):
        '''ДЕМОНТАЖ'''

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
#
# assert 'Django'
#
#
#
# browser.title
