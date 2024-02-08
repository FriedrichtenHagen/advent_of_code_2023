
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a

# use a queue for next steps

class PulsePropagater():
    def __init__(self):
            self.queue = []


            self.flops = {}
            # high pulse: it is ignored and nothing happens. 
            # low pulse: 
            #   if off: turns on and sends a high pulse. 
            #   If on: turns off and sends a low pulse.
            # starts at off (False)
            self.conj = {}
            # have list of all inputs
            # initialy low (False) for all inputs
            # if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            self.graph = {}

    def read_input(self, input_path):
        with open(input_path) as i:
            lines = i.read().split('\n')
            for line in lines:
                source, target = line.split('->')
                source = source.strip()
                dests = target.strip().split(',')

                if source[0] == '%':
                    source = source[1:]
                    self.flops[source] = False
                elif source[0] == '&':
                    source = source[1:]
                    self.conj[source] = {}
                self.graph[source] = dests


    def fill_conjunctions(self):
        for source, dests in self.graph.items():
            for dest in dests:
                if dest in self.conj:
                    self.conj[dest][source] = False
        print(self.conj)

    
if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day20/debug.txt'
    
    PulseMachine = PulsePropagater()
    PulseMachine.read_input(input_path)
    print(PulseMachine.flops)
    print(PulseMachine.conj)
    print(PulseMachine.graph)

    PulseMachine.fill_conjunctions()