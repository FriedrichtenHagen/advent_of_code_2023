
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a

# use a queue for next steps

class PulsePropagater():
    def __init__(self):
            self.queue = []
            # example_queue = ['a', 'd', 'c']
            self.modules = {}

    def read_input(self):
        with open('/Users/friedrichtenhagen/coding/advent_of_code_2023/day20/debug.txt.') as i:
            lines = i.read().split('\n')
            for line in lines:




                # module:
                modules = {
                    'a': {
                        'type': 'conjunction&',
                        'targets': ['b', 'c']
                    },
                    'b': {
                        # If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. 
                        # If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.
                        'type': 'flipflop%',
                        'targets': ['a', 'c'],
                        'status': True #False
                    },
                    'c': {
                        'type': 'broadcaster',
                        'targets': ['a', 'c']
                    },
                }
    def handle_step(self, module_name):
        # look up module by name in self.modules dict

        pass

    



