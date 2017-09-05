import os

import yaml
from git import Repo


class GitCv:
    def __init__(self, cv_path, repo_path):
        self._cv = self._load_cv(cv_path)
        self._repo_path = repo_path

    def _load_cv(self, cv_path):
        with open(cv_path, "r") as f:
            cv = yaml.load(f)
        return cv

    def _create_repo(self):
        repo_path = os.path.join(self._repo_path, 'cv')
        Repo.init(repo_path)

    def render(self):
        self._create_repo()


if __name__ == '__main__':
    GitCv('../cv.yaml', '../target').render()
