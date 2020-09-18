from family_challenge.Relationships import Uncle, Aunt
from family_challenge.Relationships import SisterInLaw, BrotherInLaw
from family_challenge.Relationships import Son, Daughter, Siblings

class Relation:
    def __init__(self, relation):
        if relation == 'Paternal-Uncle':
            self.relation = Uncle('Paternal') 
        elif relation == 'Maternal-Uncle':
            self.relation = Uncle('Maternal')
        elif relation == 'Paternal-Aunt':
            self.relation = Aunt('Paternal')
        elif relation == 'Maternal-Aunt':
            self.relation = Aunt('Maternal')
        elif relation == 'Sister-In-Law':
            self.relation = SisterInLaw()
        elif relation == 'Brother-In-Law':
            self.relation = BrotherInLaw()
        elif relation == 'Son':
            self.relation = Son()
        elif relation == 'Daughter':
            self.relation = Daughter()
        elif relation == 'Siblings':
            self.relation = Siblings()
    
          