from sh import git


class GitBranch:
    def __init__(self, name):
        self.name = name

    def create(self):
        git.checkout("-b", self.name)
