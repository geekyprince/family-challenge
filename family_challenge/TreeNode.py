class TreeNode:
    def __init__(self, father, mother, gender, spouse):
        self.father = father
        self.mother = mother
        self.gender = gender
        self.son = {}
        self.daughter = {}
        self.spouse = spouse