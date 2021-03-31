import unittest
from models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','Fidie','business','marketing','http://www.abc.net.au/news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


