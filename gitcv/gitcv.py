import yaml


class GitCv:
    def __init__(self, cv_path):
        self._cv = self._load_cv(cv_path)

    def _load_cv(self, cv_path):
        with open(cv_path, "r") as f:
            cv = yaml.load(f)
        return cv

    def render(self, cv_path):
        pass


if __name__ == '__main__':
    GitCv('../cv.yaml').render()
