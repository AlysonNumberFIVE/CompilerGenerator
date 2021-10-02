
import sys

GRAMMAR 	= 0
SCOPE_TAGS 	= 1
RECOVERY 	= 2


class RuleObject:

	def __init__(self, rule_name: str, recipe:  list):
		self.name = rule_name
		self.recipe = recipe
		self.follow = list()

	def print(self):

		print('name: ', self.name)
		print("recipe: ")
		for recipe in self.recipe:
			print('\t', recipe)
	
		if len(self.follow) > 0:
			for follow in self.follow:
				print('\t', follow)
			

def setup_nonterminals(grammar: str):
	nonterminals = list()
	grammar_rules = grammar.split("\n")
	for gmr in grammar_rules:
		if "->" in gmr:
			production_rule = gmr.split("->")
			nonterminals.append(production_rule[0].strip())

	return nonterminals


def setup_lists(words: str):
	placement_list = list()
	tokens = words.split("\n")

	for token in tokens:
		if len(token) == 0 or token[0] == '#':
			continue 

		placement_list.append(token)

	return placement_list


def setup_grammar(grammar: str):
	rules_objs = list()
	current_obj = None

	grammar_rules = grammar.split("\n")
	for gmr in grammar_rules:
		if len(gmr) == 0 or gmr[0] == '#':
			continue 

		if "->" in gmr:
			if current_obj is not None:
				rules_objs.append(current_obj)
			nonterminal_rule = gmr.split("->")
			if "|" in nonterminal_rule[1]:
				objs = RuleObject(nonterminal_rule[0].strip(), nonterminal_rule[1].split("|"))
			else:
				objs = RuleObject(nonterminal_rule[0].strip(), [nonterminal_rule[1]])
			current_obj = objs
	
		elif "|" in gmr:
			rule = gmr.strip()
			current_obj.recipe += rule.split("|")[1:]

	rules_objs.append(current_obj)
	return rules_objs


def unpack_grammar_spec(grammar: str):
	segments = grammar.split("%%")

	rule_objs = setup_grammar(segments[GRAMMAR])
	scope_tags = setup_lists(segments[SCOPE_TAGS])
	recovery_list = setup_lists(segments[RECOVERY])
	nonterminals = setup_nonterminals(segments[GRAMMAR])
	return rule_objs, scope_tags, recovery_list, nonterminals


def read_file(grammar_file: str):
	try:
		fd = open(grammar_file)
		content = fd.read()
		return content
	except FileNotFoundError:
		print(f"Error: {grammar_file} file not found")
		sys.exit(1)


def create_existing_rules(grammar: str):

	all_rules = list()
	for gmr in grammar.split("\n"):
		
		if "->" in gmr:
			production_rule = gmr.split("->")

			if "|" in production_rule[1]:
				subrules = production_rule[1].split("|")

				for sub in subrules:
					all_rules.append(sub)
			else:
				all_rules.append(production_rule[1])

		elif "|" in gmr:
			rule = gmr.strip()
			rules = rule.split("|")[1:]
			for r in rules:
				all_rules.append(r)

	return all_rules


def read_grammar_file(grammar_file: str):

	grammar = read_file(grammar_file)
	rule_objs, scope_tags, recovery_list, nonterminals = \
		unpack_grammar_spec(grammar)

	all_rules = create_existing_rules(grammar)

	return rule_objs, scope_tags, recovery_list, nonterminals, all_rules
	