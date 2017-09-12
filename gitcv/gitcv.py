import os

import yaml
from git import Repo


class GitCv:
    def __init__(self, cv_path, work_dir):
        self._repo_dir = os.path.join(work_dir, 'cv')
        self._cv_path = cv_path
        self._cv = self._load_cv()

    def _load_cv(self):
        with open(self._cv_path, 'r') as f:
            return yaml.load(f)

    def _create_repo(self):
        self._repo = Repo.init(self._repo_dir)

    def _create_branches(self):
        for stream in self._cv:
            for entry in stream:
                self._create_branch(entry)

    def _create_branch(self, branch_name):
        self._repo.create_head(branch_name)

    def _create_or_append(self, file_name, content):
        path_and_file_name = os.path.join(self._repo_dir, file_name)
        write_or_append = 'w' if not os.path.exists(path_and_file_name) else 'a'
        with open(path_and_file_name, write_or_append) as f:
            f.writelines(content)

    def _commit_file(self, file_name):
        self._repo.index.add([file_name])
        self._repo.index.commit('Add {0}'.format(file_name))

    def create(self):
        self._create_repo()
        self._create_or_append('dummy.txt', 'test')
        self._commit_file('dummy.txt')
        self._create_branches()


if __name__ == '__main__':
    GitCv('../cv.yaml', '../target').create()
