from cps337_dfa import DFA

def test_m1():
	q = ('q0', 'q1')
	sigma = ('a', 'b')
	delta = {('q0','a'):'q0', ('q0', 'b'): 'q1', ('q1','a'):'q0', ('q1', 'b'): 'q1'}
	q0 = 'q0'
	f = ['q0']
	m = DFA(q, sigma, delta, q0, f)
	print(m.accept('aba'), True)
	print(m.accept('aa'), True)
	print(m.accept('abb'), False)
	print(m.accept(''), True)


def test_m2():
	q = ('q0', 'q1', 'q2', 'q3')
	sigma = ('a', 'b')
	delta = {('q0','a'):'q1', ('q0', 'b'): 'q2', ('q1','a'):'q1', ('q1', 'b'): 'q3',
	('q2', 'a'): 'q1', ('q2', 'b'): 'q2', ('q3', 'a'): 'q3', ('q3', 'b'): 'q3'}
	q0 = 'q0'
	f = ['q0', 'q1', 'q2']
	m = DFA(q, sigma, delta, q0, f)
	print(m.accept(''), True)
	print(m.accept('aa'), True)
	print(m.accept('abb'), False)
	print(m.accept('bbb'), True)
	print(m.accept('bba'), True)

def test_m3():
	q = ('q0', 'q1', 'q2', 'q3')
	sigma = ('a', 'b')
	delta = {('q0','a'):'q1', ('q0', 'b'): 'q0', ('q1','a'):'q1', ('q1', 'b'): 'q2',
	('q2', 'a'): 'q3', ('q2', 'b'): 'q0', ('q3', 'a'): 'q3', ('q3', 'b'): 'q3'}
	q0 = 'q0'
	f = ['q3']
	m = DFA(q, sigma, delta, q0, f)
	print(m.accept(''), True)
	print(m.accept('aba'), True)
	print(m.accept('abb'), False)
	print(m.accept('bab'), False)
	print(m.accept('baa'), False)
	print(m.accept('aaa'), False)
	print(m.accept('bbb'), False)
	print("---Testing 1c---")
	print("---abb---")
	print(m.accept('abb'), False)
	print("---bbabab---")
	print(m.accept('bbabab'), True)
	
def main():
	test_m1()
	test_m2()
	test_m3()

if __name__ == '__main__':
	main()