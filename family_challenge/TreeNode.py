class TreeNode:
    def __init__(self, father, mother, gender, spouse):
        self.father = father
        self.mother = mother
        self.gender = gender
        self.son = set()
        self.daughter = set()
        self.spouse = spouse