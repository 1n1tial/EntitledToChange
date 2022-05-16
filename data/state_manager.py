
class StateManager():
    def __init__(self, over=False, state_dict={}, state_name=None, state=None, now=None):
        self.over = False
        self.state_dict = {}
        self.state = None
        self.state_name = None
        self.now = None

    def createStateDict(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def checkFlip(self, keys, now):
        self.now = now
        if self.state.quit:
            self.over = True
        elif self.state.done:
            self.flipState()
        self.state.update(keys, now)

    def draw(self, surface, interpolate):
        self.state.draw(surface, interpolate)
    
    def flipState(self):
        previous = self.state_name
        self.state_name = self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.now, persist)
        self.state.previous = previous
    
    def getEvent(self, event):
        self.event.getEvent(event)


class State():
    def __init__(self):
        self.start_time = 0
        self.now = 0
        self.quit = False
        self.done = False
        self.next = None
        self.previous = None
        self.persist = {}

    def getEvent(self, event):
        pass

    def startup(self, now, persist):
        self.persist = persist
        self.start_time = now

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self):
        pass