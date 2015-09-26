
class Mine:
    def __init__(self, vec, controlled=False):
	    self.location = vec                     
	    self.controlled = controlled
        
    def astuple(self):
        return (self.__class__, self.location.x, self.location.y, self.controlled)

    def __repr__(self):
        if self.controlled:
            cont = 1
        else:
            cont = 0
        return "Mine(%f, %f, %d)" %(self.location.x, self.location.y, cont)

    def __eq__(self, other):
        return self.astuple() == other.astuple()

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.astuple())
