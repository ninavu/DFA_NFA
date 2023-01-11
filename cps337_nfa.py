from cps337_dfa import *

class NFA:
	current_states = None   # A list of current states
	#initialize all variable when calling the class NFA
	def __init__(self, states, alphabet, transition_function, start_state, accept_states):
		self.states = states
		self.alphabet = alphabet
		self.transition_function = transition_function
		self.start_state = start_state
		self.accept_states = accept_states
		self.current_state = start_state
		return


	def transition_on_input(self, input_value):
		# For a given input character, update the list of current states
		if ((self.current_state, input_value) not in self.transition_function.keys()):
			self.current_state = None
			return
		
		# print("current states: " + str(self.current_states))

		if type(self.current_states) == list:
			state_list = []
			for state in self.current_states:
				# print("1 state: " + str(state))
				self.current_state = self.transition_function[(state, input_value)]

				if type(self.current_state) == list:
					for s in self.current_state:
						state_list.append(s)
				else:
					state_list.append(self.current_state)
				# print("(" + str(self.current_state) + ", " + input_value + ")")
			self.current_states = state_list
			print("(" + str(state_list) + ", " + input_value + ")")

		else:
			self.current_states = self.transition_function[(self.current_state, input_value)]
			print("(" + str(self.current_states) + ", " + input_value + ")")
	
		return 

	# Returns true if the NFA is currently in an accepting state; false otherwise
	def in_accept_state(self, accept_states):
		print("(" + str(self.current_states) + ", <E>)")  
		if type(self.current_states) == list:
			for state in self.current_states:
				if state in accept_states: 
					return True
			return False
		else:
			return self.current_states in accept_states

	#run the given word through the NFA and return TRUE if it is accepted; FALSE otherwise
	def accept(self, word):
		self.current_state = self.start_state
		self.current_states = self.current_state
		for char in word:
			self.transition_on_input(char)
			continue 
		return self.in_accept_state(self.accept_states)
	
	def new_state(self, l):
		n = ""
		for state in l:
			n += state
		return n
	
	def check_transition(self, s, val, extra):
		cur = ""
		if ((s, val) not in self.transition_function.keys()): 
			cur = extra
		else: 
			cur = self.transition_function[(s, val)]
		return cur
	
	def add_states(self, states):
		l = []
		for s in states:
			l.append(s)
		return l
	
	#return an equivalent DFA - ignore empty string transitions
	def dfa(self):
		dfa_start = self.start_state
		dfa_states = self.add_states(self.states)
		dfa_transition = {}
		dfa_final = []
		empty_state = ""

		i = 0
		while i < len(dfa_states):
			cur = dfa_states[i]
			# print("cur: " + cur)
			for j in self.alphabet:
				cur_states = ""
				if cur in self.states:
					cur_states = self.check_transition(cur, j, empty_state)
				else: 
					for k in range(0, len(cur), 2):
						s = self.check_transition(cur[k:k+2], j, empty_state)
						if type(s) == list:
							s = self.new_state(s)
						cur_states += s
						
				# print("states: " + str(cur_states) + " + val: " + str(j))
				if type(cur_states) == list:
					cur_states = self.new_state(cur_states)
				dfa_transition[(cur, j)] = cur_states
				# print(dfa_transition)

				if cur_states not in dfa_states:
					dfa_states.append(cur_states)
				# print("states list: " + str(dfa_states))
			i += 1
		
		for k in self.accept_states:
			for s in dfa_states:
				if k in s:
					dfa_final.append(s)
			
		return DFA(tuple(dfa_states), self.alphabet, dfa_transition, dfa_start, dfa_final)


def test_example():
	q = ('q1', 'q2', 'q3', 'q4')
	sigma = ('0', '1')
	delta = {('q1','0'):'q1', ('q1', '1'): ['q1', 'q2'], ('q2', '0'): 'q3', ('q2', '1'): 'q3', ('q3', '0'): 'q4', ('q3', '1'): 'q4'}
	q0 = 'q1'
	f = ['q4']
	m = NFA(q, sigma, delta, q0, f)
	print("---Testing 2b---")
	print("---000100---")
	print(m.accept('000100'), True)
	print("---0011---")
	print(m.accept('0011'), False)

	n = NFA.dfa(m)
	print("---Testing 3---")
	print("---000100---")
	print(n.accept('000100'), True)
	print("---0011---")
	print(n.accept('0011'), False)


def main():
	test_example()


if __name__ == '__main__':
	main()