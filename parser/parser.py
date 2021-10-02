
import read
import json

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


class Errors:

	def __init__(self, error_token: str, line: int, file:str):
		self.error_token = error_token
		self.line = line
		self.file = file

	def string(self):
		print("Syntax error : ", self.file,":", self.line,
			" invalid syntax ", self.error_token) 


class Node:

	def __init__(self, _type: str, scope:str,
			depth: int, recipe: list):
		self.type = _type
		self.scope = scope
		self.depth = depth

		self.recipe = recipe

	def string(self):
		print("type   ", self.type)
		print("scope  ", self.scope)
		print("depth  ", self.depth)

		print("recipe ", self.recipe)
		print("\n")


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

	for objs in rule_objs:
		print(objs.recipe)

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
	for prefix in all_prefixes:
		flag = True
		i = 0
		_prefix = prefix.split()
		while i < len(current_list) and i < len(_prefix):	
			
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


def check_nonterminals(current_list: list, nonterminals: list):

	if len(current_list) == 1:
		if current_list[0] in nonterminals:
			return True 
	return False


def search(current_list: list, rule_objs: object,
		nonterminals: list) -> list:
	print("search current_list is ", current_list)
	
	if check_nonterminals(current_list, nonterminals) is True:
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
			
				return tokens, True

	return [], False


def error_recovery(recovery_list: list, i: int, source_list: list):
	flag = False

	while i < len(source_list):

		source = source_list[i].split(":")
		if source[0] in recovery_list:
			flag = True
			break
		i += 1

	if flag == True:
		return i, True

	return i, False


def lookahead(current_list: list, next_token: str, all_prefixes: list):

	current_list.append(next_token)
	print(current_list)
	if prefix_checker(current_list, all_prefixes) is True:
		return False
	return True


def save_nonterminals(grammar: str):

	nonterminals = list()
	lines = grammar.split("\n")
	for line in lines:
		production_rule	= line.split("->")
		nonterminals.append(production_rule[0].strip())

	return nonterminals


def source_code_scanner(source_code: str, rule_objs: object, all_prefixes: list,
	recovery_list: list, scope_tags: list, nonterminals: list):

	nodes = list()
	errors = list()
	scope_list = list()
	
	depth = 0
	i = 0
	source_tokens = list()
	source_list = source_code.split('\n')
	current_list = list()
	recovery = True
	prev = str()
	source = list()
	sblock = str()

	while i < len(source_list):

		if len(source_list[i]) == 0:
			i += 1
			continue

		source = source_list[i].split(':')
		current_list.append(source[1])
		source_tokens.append(source[0])
	
		if (len(current_list) == 1 and source[1] in scope_tags):
			if source[1] == scope_tags[0]:
				sblock = prev
				scope_list.append(sblock)
				depth += 1
			elif source[1] == scope_tags[1]:
				sblock = scope_list.pop()
				depth -= 1
			i += 1
			current_list = list()
			continue 
	
		while True:
			current_list, f = reduce(current_list, rule_objs)
			if f is False:
				break

		recover = prefix_checker(current_list, all_prefixes)		

		if recover is False:
				
			if source[1] in recovery_list and len(current_list) > 1: 
				err = Errors(
					source[0],
					source[2],
					source[3]
				)
				errors.append(err)
				current_list = list()
				i += 1
				continue

		rule, f = search(current_list, rule_objs, nonterminals)

		if f == True and i + 1 < len(source_list):
			source = source_list[i + 1].split(":")
			prev = current_list[0]
			if lookahead(current_list, source[1], all_prefixes) is False:
				f = False
				current_list.pop()				
				i += 1
				continue


		if f == True:


			if len(scope_list) == 0:
				sblock = ""

			new_node = Node(
				current_list[0],
				sblock,
				depth,
				source_tokens
			)

			nodes.append(new_node)
			source_tokens = list()
			current_list = list()

		i += 1


	if len(current_list) > 1:
		errors.append(
			Errors(source[0], source[2], source[3])
		)

	if depth != 0:
		errors.append(
			Errors("mismatched blocks", -1, "tmp_file")
		)

	return nodes, errors


def write_json_file(tokens: list):
	file_buffer = open("source.ast", "w")
	file_buffer.write("{")

	for i, token in zip(range(0, len(tokens) - 1), tokens):
		file_buffer.write(json.dumps(token.__dict__, indent=4))
		if i == len(tokens) - 2:
			break
		file_buffer.write(",\n")

	file_buffer.write("}")
	file_buffer.close()


if __name__ == '__main__':

	source = read.read_file("source_files\\source1.tk")

	rule_objs, scope_tags, recovery_list, nonterminals, all_rules = \
		read.read_grammar_file("grammar_files\\test_grammar.gmr")

	tokens, errors = source_code_scanner(source, rule_objs, all_rules, recovery_list,
		scope_tags, nonterminals)

	write_json_file(tokens)

	for token in tokens:
		token.string()

	if len(errors) > 0:
		for err in errors:
			err.string()

