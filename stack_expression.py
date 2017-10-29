value_stack = []
operator_stack = []

query = str(input('Enter expression')) #'1+(2*3)*9'

def evaluate():
	op2 = value_stack.pop()
	op1 = value_stack.pop()
	op = operator_stack.pop()

	if op == '+':
		result = op1 + op2

	elif op == '-':
		result = op1 - op2

	elif op == '*':
		result = op1 * op2

	elif op == '/':
		result = op1 / op2

	elif op == '%':
		result =  op1 % op2

	value_stack.append(result)



for x in query:
	if x == '(':
		continue

	elif x.isdigit():
		value_stack.append(int(x))

	elif x in '+-*/%':
		operator_stack.append(x)

	elif x == ')':
		evaluate()


while operator_stack:
	evaluate()


print(operator_stack, value_stack)
