import os
import shutil
import tempfile
import unittest

from gitcv.gitcv import GitCv


class GitcvTest(unittest.TestCase):

    def setUp(self):
        self.tmp_path = tempfile.mkdtemp('', 'gitcv_test')
        resource_path = self._get_abs_path('resources/simple_cv.yaml')
        self.gitcv = GitCv(resource_path, self.tmp_path)

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

    def _get_abs_path(self, rel_path):
        return os.path.join((os.path.dirname(os.path.realpath(__file__))), rel_path)


if __name__ == '__main__':
    unittest.main()
