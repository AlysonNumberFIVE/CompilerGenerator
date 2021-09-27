


class RuleObject:

	def __init__(self, rule_name: str):
		self.name = rule_name
		self.recipe = list()
		self.follow = list()

	def print(self):

		print('name: ', self.name)
		print("recipe: ")
		for recipe in self.recipe:
			print('\t', recipe)
		if len(self.follow) > 0:
			for follow in self.follow:
				print('\t', follow)


class Node:

	def __init__(self, name: str, _type: str, recipe: list):
		self.name = name
		self.type = _type
		self.next = None

		self.recipe = recipe



def create_grammar(grammar: str):
	rule_objs = list()

	rule_list = grammar.split("\n")
	for rule_line in rule_list:

		production_rule = rule_line.split('->')
		obj = RuleObject(production_rule[0].strip())

		if '|' in production_rule[1]:
			sub_rules = production_rule[1].split('|')

			obj.recipe += sub_rules
		else:
			obj.recipe.append(production_rule[1])

		rule_objs.append(obj)
		obj.print()

	return rule_objs


def create_existing_rules(grammar: str) -> list:

	all_rules = list()
	for grmr in grammar.split("\n"):
		production_rule = grmr.split("->")
		if "|" in production_rule[1]:
			sub_rules = production_rule[1].split("|")

			for sub in sub_rules:
				all_rules.append(sub)
		else:
			all_rules.append(production_rule[1])

	return all_rules


def prefix_checker(current_list: list, all_prefixes: list):

	match = False
	print("current list is now : ", current_list)
	for prefix in all_prefixes:
		flag = None
		i = 0
		_prefix = prefix.split()
	
		while i < len(current_list) and i < len(_prefix):	
			#print('curr is ', current_list[i], ' and prefix is ',_prefix[i])
			
			if current_list[i] != _prefix[i]:
				flag = False
			i += 1

		if flag == True:
			return True
	print("False>>>>")
	return False


def reduce(current_list: list, rule_objs: object):
	i = 0
	list_len =  len(current_list)

	while i < list_len:

		sub_list = current_list[i:list_len] 
		for rule in rule_objs:

			recipes = rule.recipe
			for recipe in recipes:

				tokens = recipe.split()

				if len(sub_list) == len(tokens):
					trigger = True
					j = 0
					while j < len(tokens) - 1:

						if sub_list[j] != tokens[j]:
							trigger = False
							break

						j += 1
					if trigger == False:
						continue 
					if tokens == sub_list:

						first = current_list[0:i]
						first.append(rule.name)
						return first, True

		i += 1
	return current_list, False


def search(current_list: list, rule_objs: object) -> list:

	for rule in rule_objs:

		recipes = rule.recipe
		for recipe in recipes:

			tokens = recipe.split()
			if len(current_list) == len(tokens) - 1:
				trigger = True
				i = 0
				while i < len(tokens) - 1:

					if current_list[i] != tokens[i]:
						trigger = False
						break

					i += 1
				if trigger == False:
					continue 
				print('True')
				return tokens, True

	return [], False


def error_recovery(recovery_list: list, i: int, source_list: list):
	flag = False

	while i < len(source_list):

		print("source_Code is ", source_list[i])
		source = source_list[i].split(":")
		if source[0] in recovery_list:
			flag = True
			break
		i += 1

	if flag == True:
		return i, True

	return i, False


def source_code_scanner(source_code: str, rule_objs: object, grammar: str,
	recovery_list: list):

	i = 0
	source_list = source_code.split('\n')
	current_list = list()
	curr_grammar = None
	all_prefixes = create_existing_rules(grammar)
	recovery = True

	while i < len(source_list):
		source = source_list[i].split(':')
		current_list.append(source[1])

		while True:
			current_list, f = reduce(current_list, rule_objs)
			if f is False:
				break

		recover = prefix_checker(current_list, all_prefixes)
	
		if recover is False:
		
			if source[1] in recovery_list:
				print("Syntax error") 
				current_list = list()
				i += 1
				continue 



		rule, f = search(current_list, rule_objs)

		if f == True:
			for r in rule:
				print("r is ", r)

			#curr_grammar = Node(source[0], source[1])

			current_list = list()
	

		i += 1


grammar = """whileStmt -> while openbrace condition closebrace wBody
forStmt -> for openbrace assign semicolon condition semicolon math closebrace forBody
variable -> var ID equ LITERAL fBody | var ID equ ID fBody | var param fBody |ID equ LITERAL fBody 
condition -> CONDITIONAL
math -> MATH
forBody -> openbracket fBody closebracket
assign -> variable equ LITERAL fBody
param -> ID DATATYPE
commaParamList -> COMMA ID DATATYPE
paramList -> param commaParamList
fStmt -> func ID openbrace paramList closebrace fBody	
fBody -> openbracket wBody closebracket | openbracket forStmt closebracket | openbracket whileStmt closebracket | openbracket closebracket
wBody -> variable"""

recovery_list = ["func", "var", "while", "for", "openbracket"]


"""
var hello = "hello"

func main(argc int, argv []string)
{
	var hell string
}

"""
source = """var:var
hello:ID
=:equ
"hello":LITERAL
func:func
main:ID
):closebrace
argc:ID
int:DATATYPE
,:COMMA
argv:ID
[]string:DATATYPE
):closebrace
{:openbracket
var:var
{:openbracket
}:closebracket
hell:ID
string:DATATYPE
}:closebracket"""

rule_objs = create_grammar(grammar)

all_rules = create_existing_rules(grammar)

source_code_scanner(source, rule_objs, grammar, recovery_list)








