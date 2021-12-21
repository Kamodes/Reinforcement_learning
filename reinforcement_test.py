class MDP:
    
    def __init__(self, init, actlist, terminals, gamma=.9):
        self.init = init
        self.actlist = actlist
        self.terminals = terminals
        if not (0 <= gamma < 1):
            raise ValueError("An MDP must have 0 <= gamma < 1")
        self.gamma = gamma
        self.states = set()
        self.reward = {}

    def R(self, state):
        return self.reward[state]

    def T(self, state, action):
        raise NotImplementedError

    def actions(self, state):
        if state in self.terminals:
            return [None]
        else:
            return self.actlist