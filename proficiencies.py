"""
Universal class for saving throws and skills
"""
### SAVING THROWS ###
class Score:
    def init(self, score, bonus):
        self.proficiency = False
        self.score = (score//2)-5

    def update_score(self, score, bonus):
        self.score = (score//2)-5
        if self.proficiency:
            self.score += bonus

    def update_proficiency(self, proficiency):
        self.proficiency = proficiency
