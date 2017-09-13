import os
import shutil
import tempfile
import unittest

from gitcv.gitcv import GitCv


class GitcvTest(unittest.TestCase):
    def setUp(self):
        self._temp_dir = tempfile.mkdtemp('', 'gitcv_test_')

    def tearDown(self):
        shutil.rmtree(self._temp_dir)

    def test_should_read_simple_cv(self):
        # setup
        cv = self._setup_gitcv()._cv

        # verify
        self.assertEqual(cv[0]['education'][0]['year'], 2001)

    def test_should_create_empty_repo(self):
        # setup
        gitcv = self._setup_gitcv()

        # exercise
        gitcv.create()

        # verify
        repo_files = os.listdir(gitcv._repo_dir)
        self.assertTrue('.git' in repo_files)

    def test_should_create_branch_per_stream(self):
        # setup
        gitcv = self._setup_gitcv()

        # exercise
        gitcv.create()

        # verify
        repo = gitcv._repo
        self.assertEqual(len(repo.branches), 2)
        self.assertTrue('education' in repo.branches)

    def test_should_create_file_if_it_doesnt_already_exist(self):
        # setup
        gitcv = self._setup_gitcv()
        gitcv._repo_dir = self._temp_dir

        # exercise
        gitcv._create_or_append('dummy.txt', 'test')

        # verify
        with open(os.path.join(self._temp_dir, 'dummy.txt'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], 'test')

    def test_should_append_to_file_if_it_already_exists(self):
        # setup
        gitcv = self._setup_gitcv()
        gitcv._repo_dir = self._temp_dir

        # exercise
        gitcv._create_or_append('dummy.txt', 'foo')
        gitcv._create_or_append('dummy.txt', 'bar')

        # verify
        with open(os.path.join(gitcv._repo_dir, 'dummy.txt'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], 'foobar')

    def test_should_create_file_per_branch(self):
        # setup
        gitcv = self._setup_gitcv()

        # exercise
        gitcv.create()

        # verify
        with open(os.path.join(gitcv._repo_dir, 'education'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], '2001: MIT - CS')

    def _setup_gitcv(self, file_name='simple_cv.yaml'):
        return GitCv(self._get_absolute_resource_path(file_name), self._temp_dir)

    def _get_absolute_resource_path(self, file_name):
        return os.path.join((os.path.dirname(os.path.realpath(__file__))), 'resources', file_name)


if __name__ == '__main__':
    unittest.main()
