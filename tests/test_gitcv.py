import os
import shutil
import tempfile
import unittest
from git import Repo

from gitcv.gitcv import GitCv


class GitcvTest(unittest.TestCase):
    def setUp(self):
        self.repo_path = tempfile.mkdtemp('', 'gitcv_test')
        resource_path = self._get_abs_path('resources/simple_cv.yaml')
        self.gitcv = GitCv(resource_path, self.repo_path)
        print("Create repo at {}".format(self.repo_path))

    def tearDown(self):
        shutil.rmtree(self.repo_path)

    def test_should_read_simple_cv(self):
        # exercise
        cv = self.gitcv._cv

        # verify
        self.assertEqual(cv[0]['education'][0]['year'], 2001)

    def test_should_create_empty_repo(self):
        # exercise
        self.gitcv.create()

        # verify
        git_repo = os.listdir(self.repo_path)[0]
        self.assertEqual(git_repo, 'cv')

    def test_should_create_branch_per_stream(self):
        # exercise
        self.gitcv.create()

        # verify
        repo = self._get_repo()
        self.assertEqual(len(repo.branches), 2)
        self.assertTrue('education' in repo.branches)

    def _get_abs_path(self, rel_path):
        return os.path.join((os.path.dirname(os.path.realpath(__file__))), rel_path)

    def _get_repo(self):
        return Repo(os.path.join(self.repo_path, 'cv'))


if __name__ == '__main__':
    unittest.main()
