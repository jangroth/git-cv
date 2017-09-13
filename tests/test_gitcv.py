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

    def atest_should_read_simple_cv(self):
        cv = self._setup_gitcv()._cv

        self.assertEqual(cv[0]['education'][0]['year'], 2001)

    def atest_should_create_empty_repo(self):
        gitcv = self._setup_gitcv()

        gitcv.create()

        repo_files = os.listdir(gitcv._repo_dir)
        self.assertTrue('.git' in repo_files)

    def test_should_commit_cv_first(self):
        gitcv = self._setup_gitcv()

        gitcv.create()

        repo = gitcv._repo
        commit = repo.active_branch.commit
        self.assertEqual(commit.message, 'First commit')

    def atest_should_create_branch_per_stream(self):
        gitcv = self._setup_gitcv()

        gitcv.create()

        repo = gitcv._repo
        self.assertEqual(len(repo.branches), 2)
        self.assertTrue('education' in repo.branches)

    def atest_should_create_file_if_it_doesnt_already_exist(self):
        gitcv = self._setup_gitcv()
        gitcv._repo_dir = self._temp_dir

        gitcv._create_or_append('dummy.txt', 'test')

        with open(os.path.join(self._temp_dir, 'dummy.txt'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], 'test')

    def atest_should_append_to_file_if_it_already_exists(self):
        gitcv = self._setup_gitcv()
        gitcv._repo_dir = self._temp_dir

        gitcv._create_or_append('dummy.txt', 'foo')
        gitcv._create_or_append('dummy.txt', 'bar')

        with open(os.path.join(gitcv._repo_dir, 'dummy.txt'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], 'foobar')

    def atest_should_create_file_per_branch(self):
        gitcv = self._setup_gitcv()

        gitcv.create()

        with open(os.path.join(gitcv._repo_dir, 'education'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], '2001: MIT - CS\n')

    def atest_should_add_commits_to_file(self):
        gitcv = self._setup_gitcv('complex.yaml')

        gitcv.create()

        with open(os.path.join(gitcv._repo_dir, 'bar'), 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines[0], '2010: Gri - Gor\n')
        self.assertEqual(lines[1], '2012: Gol - Gil\n')
        

    def _setup_gitcv(self, file_name='simple.yaml'):
        return GitCv(self._get_absolute_resource_path(file_name), self._temp_dir)

    def _get_absolute_resource_path(self, file_name):
        return os.path.join((os.path.dirname(os.path.realpath(__file__))), 'resources', file_name)


if __name__ == '__main__':
    unittest.main()
