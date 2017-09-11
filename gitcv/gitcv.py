import os

import yaml
from git import Repo


class GitCv:
    def __init__(self, cv_path, repo_path):
        self._cv = self._load_cv(cv_path)
        self._repo_path = os.path.join(repo_path, 'cv')

    def _load_cv(self, cv_path):
        with open(cv_path, "r") as f:
            cv = yaml.load(f)
        return cv

    def _create_repo(self):
        self._repo = Repo.init(self._repo_path)

    def _create_branches(self):
        for stream in self._cv:
            for entry in stream:
                self._create_branch(entry)

    def _create_branch(self, branch_name):
        self._repo.create_head(branch_name)

    def _create_file_and_commit(self, file_name):
        open(os.path.join(self._repo_path, file_name), 'w').close()
        self._repo.index.add([file_name])
        self._repo.index.commit('Add {0}'.format(file_name))

    def create(self):
        self._create_repo()
        self._create_file_and_commit('dummy.txt')
        self._create_branches()


if __name__ == '__main__':
    GitCv('../cv.yaml', '../target').create()
