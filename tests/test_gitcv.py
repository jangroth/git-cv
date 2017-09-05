import os
import shutil
import tempfile
import unittest

from gitcv.gitcv import GitCv


class GitcvTest(unittest.TestCase):

    def setUp(self):
        self.tmp_path = tempfile.mkdtemp('', 'gitcv_test')
        self.gitcv = GitCv('resources/simple_cv.yaml', self.tmp_path)

    def tearDown(self):
        shutil.rmtree(self.tmp_path)

    def test_should_read_simple_cv(self):
        # exercise
        cv = self.gitcv._cv

        # verify
        self.assertEqual(cv['streams'][0]['edu'][0]['year'], 2001)

    def test_should_create_empty_repo(self):
        # exercise
        self.gitcv.render()

        # verify
        git_repo = os.listdir(self.tmp_path)[0]
        self.assertEqual(git_repo, 'cv')


if __name__ == '__main__':
    unittest.main()
