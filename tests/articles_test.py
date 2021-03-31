import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('business','marketing','http://www.abc.net.au/news',"2020-11-22T18:49:22Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))



    