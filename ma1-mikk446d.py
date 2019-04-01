class CA:
    """Elementary Cellular Automaton - by mikk446d Mikkel Sjølund Pieler
    
    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""
    rule = []
    cstate = ""
    nstate = ""
    
    def __init__(self, rule, init_state='0'*20+'1'+'0'*20):
        """Initialize the CA with the given rule and initial state."""
        self.rule = self.generate_rule(rule)
        self.cstate = init_state
    
    def state(self):
        """Returns the current state."""
        return self.cstate
    
    def next(self):
        """Progress one step and then return the current state."""

        self.cstate = "0" + self.cstate + "0"
        self.nstate = ""
        number = 0
        
        for n in range(0, 41):   
            self.nstate += self.rule[str(self.state()[number:number+3])]       
            number+=1
        self.cstate = self.nstate
        
        return self.cstate
        
    def run(self, num=18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""

        i=0
        while i<20:
            print(self.state().replace("0", " ").replace("1", "*"))
            print(self.next().replace("0", " ").replace("1", "*"))
            i+=1
    

    def binary_value(self, n):
        return f'{n:08b}'

    def generate_rule(self, n):
        rule = {}
        for i in range(1,9):
            str_value = str(self.binary_value(n))[-i]
            rule.update({self.binary_value(i-1)[-3:]: str_value})         
        return rule
