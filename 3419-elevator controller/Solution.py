class LiftState:
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass

class OpenState(LiftState):
    def open(self):
        print ("OPEN:The door is opened...")
        return self
    def close(self):
        print ("OPEN:The door start to close...")
        print ("OPEN:The door is closed")
        return StopState()
    def run(self):
        print ("OPEN:Run Forbidden.")
        return self
    def stop(self):
        print ("OPEN:Stop Forbidden.")
        return self
    
class RunState(LiftState):
    def open(self):
        print ("RUN:Open Forbidden.")
        return self
    def close(self):
        print ("RUN:Close Forbidden.")
        return self
    def run(self):
        print ("RUN:The lift is running...")
        return self
    def stop(self):
        print ("RUN:The lift start to stop...")
        print ("RUN:The lift stopped...")
        return StopState()
    
class StopState(LiftState):
    def open(self):
        print ("STOP:The door is opening...")
        print ("STOP:The door is opened...")
        return OpenState()
    def close(self):
        print ("STOP:Close Forbidden")
        return self
    def run(self):
        print ("STOP:The lift start to run...")
        return RunState()
    def stop(self):
        print ("STOP:The lift is stopped.")
        return self

class Context:
    # write your code here
    def __init__(self):
        self.state = None
    def setState(self, state):
        self.state = state   
    def open(self):
        self.state = self.state.open()    
    def close(self):
        self.state = self.state.close()
    def run(self):
        self.state = self.state.run()
    def stop(self):
        self.state = self.state.stop()
