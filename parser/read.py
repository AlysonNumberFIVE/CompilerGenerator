
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
		print("Error: file not found")
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

	print("================ obj")
	for obj in rule_objs:
		obj.print()	

	print("=============== tags")
	for tag in scope_tags:
		print(tag)

	print("=============== rec")
	for rec in recovery_list:
		print(rec)

	print("=============== nonterm")
	for nonterm in nonterminals:
		print(nonterm)


	print("all rules\n")
	for rule in all_rules:
		print("rul ", rule)

	return rule_objs, scope_tags, recovery_list, nonterminals, all_rules
	
grammar = """
whileStmt 		-> while openbrace condition closebrace

forStmt 		-> for openbrace variable SEMICOLON condition SEMICOLON math closebrace 
				| for condition
				| for openbrace closebrace

variable 		-> var ID equ LITERAL 
				| var ID equ ID 
				| var param 
				| ID equ LITERAL 
				| var ID equ mapping 
				| ID equ mappingAssign

deref 			-> ID DOT ID

condition 		-> CONDITIONAL

math 			-> MATH

ptrDeref 		-> openbrace ID STAR ID closebrace

forBody 		-> openbracket fBody closebracket

assign 			-> variable equ LITERAL

dictionAssign 	-> ID COLON ID COMMA 
				| ID COLON LITERAL COMMA 
				| ID COLON mappingAssign COMMA 
				| dictionAssign COMMA 
				| dictionAssign ID COLON LITERAL 
				| dictionAssign dictionAssign

mappingAssign 	-> openbracket dictionAssign closebracket 
				| openbracket closebracket

mapping 		-> map openblock ID closeblock DATATYPE 
				| map openblock DATATYPE closeblock DATATYPE

ellipse 		-> DOT DOT DOT

param 			-> ID DATATYPE 
				| ID openblock closeblock DATATYPE
				| ellipse ID DATATYPE
commaParamList 	-> COMMA param

paramList 		->  paramList commaParamList 
				| param commaParamList

fStmt 			-> func ID openbrace paramList closebrace
				| func ID openbrace param closebrace 
				| func ptrDeref ID openbrace closebrace

fCall 			-> ID openbrace fParamList
				| ID openbrace ID fParamList 
				| ID openbrace LITERAL fParamList 
				| deref openbrace fParamList 
				| deref openbrace ID fParamList 
				| deref openbrace LITERAL fParamList

fParamList 		-> COMMA ID closebrace 
				| COMMA ID fParamList 
				| COMMA LITERAL fParamList 
				| COMMA LITERAL closebrace 
				| closebrace

struc 			-> type ID struct openbracket strVars closebracket 
				| type ID struct openbracket param closebracket

strVars 		-> param param 
				| strVars param

typeCast 		-> DATATYPE openbrace ID closebrace 
				| DATATYPE openbrace LITERAL closebrace"""

recovery = """
func
var
for
while
"""

read_grammar_file("test_grammar.gmr")
"""
setup_grammar(grammar)
setup_nonterminals(grammar)
setup_recovery_list(recovery)
"""