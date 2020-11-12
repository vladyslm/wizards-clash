class ScoreController:
    def __init__(self):
        self.last_score = 0

    def add_score(self, score):
        self.last_score = score

    def get_score(self):
        tmp = self.last_score
        self.reset_score()
        return tmp

    def reset_score(self):
        self.last_score = 0
