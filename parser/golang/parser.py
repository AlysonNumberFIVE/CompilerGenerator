


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
	#print("current list is now : ", current_list)
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
					while j < len(tokens):

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


def check_nonterminals(current_list: list):
	nonterminals = ["ellipse", "typeCast", "commafParamList", "fParamList","fCall", "whileStmt", "forStmt", "condition", "math", "forBody", "variable", "paramList", "param", "fStmt", "struc", "strVars"]
	if len(current_list) == 1:
		if current_list[0] in nonterminals:
			return True 
	return False



def search(current_list: list, rule_objs: object) -> list:
	print("search current_list is ", current_list)
	
	if check_nonterminals(current_list) is True:
		print("current_list is ", current_list)
		return current_list ,True

	for rule in rule_objs:

		recipes = rule.recipe
		for recipe in recipes:

			tokens = recipe.split()

			if len(current_list) == len(tokens):
				trigger = True
				i = 0
				
				while i < len(tokens):
					
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

	scope_tags = ["openbracket", "closebracket"]
	depth = 0
	i = 0
	source_list = source_code.split('\n')
	current_list = list()
	curr_grammar = None
	all_prefixes = create_existing_rules(grammar)
	recovery = True

	while i < len(source_list):
		source = source_list[i].split(':')
		current_list.append(source[1])
		"""
		if source[1] in scope_tags:
			if source[1] == scope_tags[0]:
				depth += 1
			elif source[1] == scope_tags[1]:
				depth -= 1
			i += 1

			continue 
		"""

		while True:
			current_list, f = reduce(current_list, rule_objs)
			if f is False:
				break

		recover = prefix_checker(current_list, all_prefixes)
	
		if recover is False:
			
			if source[1] in recovery_list and len(current_list) > 1:
				print("Syntax error detected : ", source[0]) 
				current_list = list()
				print("current_list ", current_list)
				print("recover is ", recover)
				i += 1
				continue




		rule, f = search(current_list, rule_objs)

		if f == True:
			for r in rule:
				print('depth ', depth)
				print("r is ", r)

			#curr_grammar = Node(source[0], source[1])

			current_list = list()
			print("current_list ", current_list)
			print("recover is ", recover)



	

		i += 1


grammar = """whileStmt -> while openbrace condition closebrace
forStmt -> for openbrace variable SEMICOLON condition SEMICOLON math closebrace | for condition | for openbrace closebrace
variable -> var ID equ LITERAL | var ID equ ID | var param | ID equ LITERAL 
condition -> CONDITIONAL
math -> MATH
forBody -> openbracket fBody closebracket
assign -> variable equ LITERAL
ellipse -> DOT DOT DOT 
param -> ID DATATYPE | ID openblock closeblock DATATYPE	| ellipse ID DATATYPE
commaParamList -> COMMA param
paramList ->  paramList commaParamList | param commaParamList
fStmt -> func ID openbrace paramList closebrace	
fCall -> ID openbrace fParamList | ID openbrace ID fParamList | ID openbrace LITERAL fParamList | ID DOT ID openbrace fParamList | ID DOT ID openbrace ID fParamList | ID DOT ID openbrace LITERAL fParamList
fParamList -> COMMA ID closebrace | COMMA ID fParamList | COMMA LITERAL fParamList | COMMA LITERAL closebrace | closebrace
struc -> type ID struct openbracket strVars closebracket | type ID struct openbracket param closebracket
strVars -> param param | strVars param
typeCast -> DATATYPE openbrace ID closebrace | DATATYPE openbrace LITERAL closebrace
fBody -> openbracket wBody closebracket | openbracket forStmt closebracket | openbracket whileStmt closebracket | openbracket closebracket"""


recovery_list = ["func", "var", "for", "while"]
eof_list = ["closebracket"]

"""
Bastard Go - by AlysonSomethingOrOther

func print(...opts []string) {
	unistd.write(1, "Hello World", 12)

}

type test struct {
	item1 string
	item2 int
}

var hello = "hello"

func main(argc int, argv []string, third float, fourth []int)
{
	var test string
	
	print(test1, test2, test2, "test4")

	type test struct {
		item1 string
		item2 int
	}
	var t int

	for () {
		print("INFINITE LOOP")
	}

	for (i = 0; i < 42; i++) {
		print()
	}
}
"""
source = """type:type
test:ID
struct:struct
{:openbracket
item1:ID
string:DATATYPE
item2:ID
int:DATATYPE
item3:ID
int:DATATYPE
item4:ID
string:DATATYPE
}:closebracket
var:var
hello:ID
=:equ
"hello":LITERAL
func:func
main:ID
(:openbrace
argc:ID
int:DATATYPE
,:COMMA
argv:ID
[:openblock
]:closeblock
string:DATATYPE
,:COMMA
third:ID
float:DATATYPE
,:COMMA
fourth:ID
[]int:DATATYPE
):closebrace
var:var
test:ID
string:DATATYPE
print:ID
(:openbrace
):closebrace
var:var
x:ID
int:DATATYPE
print2:ID
(:openbrace
x:ID
,:COMMA
y:ID
,:COMMA
"LITERAL":LITERAL
):closebrace
var:var
test:ID
int:DATATYPE
type:type
test:ID
struct:struct
{:openbracket
item1:ID
string:DATATYPE
item2:ID
int:DATATYPE
var:var
item4:ID
int:DATATYPE
}:closebracket
var:var
t:ID
int:DATATYPE
for:for
(:openbrace
):closebrace
print:ID
(:openbrace
"INFINITE LOOP":LITERAL
):closebrace
int:DATATYPE
(:openbrace
"42":LITERAL
):closebrace
for:for
(:openbrace
i:ID
=:equ
0:LITERAL
;:SEMICOLON
i<42:condition
;:SEMICOLON
i++:math
):closebrace
print:ID
(:openbrace
):closebrace"""

"""for:for
(:openbrace
var:var
i:ID
=:equ
0:LITERAL
;:SEMICOLON
i<42:condition
;:SEMICOLON
i++:math
):closebrace
print:ID
(:openbrace
):closebrace"""

rule_objs = create_grammar(grammar)

all_rules = create_existing_rules(grammar)

source_code_scanner(source, rule_objs, grammar, recovery_list)








