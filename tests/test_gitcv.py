import unittest

from gitcv.gitcv import GitCv


class GitcvTest(unittest.TestCase):
    def test_should_read_simple_cv(self):
        # setup
        gitcv = GitCv('resources/simple_cv.yaml')

        # exercise
        cv = gitcv._cv

        # verify
        self.assertEqual(cv['streams'][0]['edu'][0]['year'], 2001)


if __name__ == '__main__':
    unittest.main()
