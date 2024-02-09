from collections import deque
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

    def run(self):
        q = deque([('button', 'broadcaster', False)])
        # (sender, receiver, pulse)
        number_hi = 0
        number_low = 0

        while q:
            sender, receiver, pulse = q.popleft()

            # count the pulses. This is needed for the result
            if pulse:
                number_hi += 1
            elif not pulse:
                number_low += 1

            if receiver in self.flops:
                # not affected by high pulse
                if pulse:
                    return
                # invert pulse
                next_pulse = self.flops[receiver] = not self.flops[receiver]
            elif receiver in self.conj:
                self.conj[receiver][sender] = pulse
                next_pulse = not all(self.conjs[receiver].values())

            elif receiver in self.graph:
                # Neither a flip-flop nor a conjunction, propagate the pulse as is
                next_pulse = pulse
            else:
                # the module is a dead end
                return
        
            # send pulse to all receiver modules
            for new_receiver in self.graph[receiver]:
                q.append((receiver, new_receiver, next_pulse))

        return number_hi, number_low
    
if __name__ == "__main__":
    input_path = '/Users/friedrichtenhagen/coding/advent_of_code_2023/day20/debug.txt'
    
    PulseMachine = PulsePropagater()
    PulseMachine.read_input(input_path)
    print(PulseMachine.flops)
    print(PulseMachine.conj)
    print(PulseMachine.graph)

    PulseMachine.fill_conjunctions()
    print(PulseMachine.conj)
    tothi = totlo = 0
    for _ in range(1000):
        nhi, nlo = PulseMachine.run()
        tothi += nhi
        totlo += nlo

    answer = tothi * totlo
    print('Part 1:', answer)