"""Houses all code for reading grammar files."""
import os

class Language:
	"""
	The language class represents a single grammar token and all
	it's properties.
	"""

	def __init__(self, grammarName: str="", nonterminal: bool=False,
		terminal: bool=False, derivNum: int=-1, grammarDescription: list=[],
		stringValue: str=""):
		"""
		:param: grammarName: The grammar file name of the individual token.
		:param: nonterminal: A check whetehr this value is a nonterminal.
		:param: terminal: A check whether this grammar is a terminal. 
			TODO(alyson): Remove the terminal/nonterminal and leave a single boolean.
		:param: derivNum: The derivation number of this grammar's rule 
			(only applicable to nonterminals)
		:param: grammarDescription: The derivation of this current grammar name.
			(only applicable to nonterminals).
		:param: stringValue: The string value as seen in the source file of this
			grammar token.
		"""
		self.grammarName = grammarName
		self.nonterminal = nonterminal
		self.terminal = terminal
		self.derivNum = derivNum
		self.grammarDescription = grammarDescription
		self.stringValue = stringValue

		self.TEST_Duplicates = [] 
		self.TEST_Len = len(grammarDescription)

		if self.terminal == self.nonterminal:
			print("Error : token cannot be both a term and a nonterm")
			sys.exit(1)

	def string(self):

		return "grammarName: " + self.grammarName + "\n derivNum: " + str(self.derivNum) \
			+ "\ngrammarDescription: " + str(self.grammarDescription)


def read_file(filename: str) -> str:
	"""Reads the contents of filename.

	:param: filename: The name of the file to be read.
	:return: The contents of the file.
	"""
	try:
		fd = open(filename)
		content = fd.read()
		fd.close()
		return content
	except FileNotFoundError:
		print("Error: Unable to open file ", filename)
		print("Exiting")
		sys.exit(1)


def make_terminal(terminal: str) -> Language:
	"""Makes a base terminal Language node.
	
	:param: terminal: The terminal value.
	:return: Returns the single language object.
	"""
	lang = Language(
		grammarName=terminal,
		terminal=True, derivNum=-1,
		grammarDescription=[] 	
	)

	return lang


def make_productions(rule: str, nonterminals: list) -> list:
	"""Generates a single Language object.

	:param: The single rule to be turned into a language object.
	:param: The list of the language's nonterminals to be used to
		verify that production exists as a nonterm.
	:return: A list of all created language objects.
	"""
	language_list = list()
	production_ruleset = rule.split("->")
	production = production_ruleset[0].strip()
	
	if production not in nonterminals:
		print(f"Error : production rule {production} is not a nonterminal")
		
		return []

	# checking for multiple derivatives
	if "|" in production_ruleset[1]:
		ruleset = production_ruleset[1].split("|")

		deriv_number = 0
		for subrule in ruleset:
			grammar = subrule.split()
			lang = Language(
				grammarName=production,
				nonterminal=True,derivNum=deriv_number,
				grammarDescription=grammar
			)
			deriv_number += 1
			language_list.append(lang)

		return language_list
			
	lang = Language(
		grammarName=production,
		nonterminal=True, derivNum=0,
		grammarDescription=production_ruleset[1].split()
	)
	language_list.append(lang)

	return language_list


def tag_unique_grammar_names(nonterm_list: list):

	for i, nonterm in zip(range(0, len(nonterm_list) - 1), nonterm_list):
		if nonterm.derivNum	> 0:
			nonterm_list[i].grammarName += str(nonterm.derivNum)

	return nonterm_list



def extract_terminals_and_nonterminals(grammar: str):
	"""Extracts and separates all terminals and nonterminals 
	from the grammar.

	Terminals are determined by the tokens that don't
		appear on the LHS of all equations.

	:param: The grammar file as a string.
	:return: A list of all terminals.
	"""
	terminals = list()
	nonterminals = list()

	# get rid of all unecessary tokens.
	stripped_grammar = grammar.replace('|', ' ')

	# gather all nonterminals
	for grammar in stripped_grammar.split("\n"):
		production_ruleset = grammar.split('->')

		production = production_ruleset[0].strip()
		nonterminals.append(production)

	stripped_grammar = stripped_grammar.replace('->', ' ').replace('\n', ' ')

	# gather all terminals
	for token in stripped_grammar.split():
		if token not in nonterminals and token not in terminals:
			terminals.append(token)

	return terminals, nonterminals


def search_nonterm_list(nonterm_list: list, to_find: str) -> list:
	"""This scans through the nonterminal's derivations for tokens
	that have more than 1 derivation and expands them.

	:param: nonterm_list: The list of nonterminals to scan through.
	:param: to_find: The nonterminal to be searched for.
	:return The expanded list of tokens.
	"""
	nonterm_names = list()
	for nonterm in nonterm_list:
		if to_find == nonterm.grammarName:
			if nonterm.derivNum > 0:
				name = to_find + str(nonterm.derivNum)
			else:
				name = to_find
			nonterm_names.append(name)
	return nonterm_names


def expand_production_list(nonterm_list: list, nonterminals: list) -> list:
	"""This finds all the tokens in every nonterminal object that derives tokens
	which, themselves, have multiple derivations and expands these tokens.

	If a nonterminal derives a token "test" and test is a nonterminal that
		has 2 derivations, then "test" will be expanded to "test" and "test1".

	:param: nonterm_list: The list of nonterminals to scan through.
	:param: nonterminals: The list of all nonterminals in the target grammar.
	:return: A nonterm_list with expanded grammar tokens.
	"""

	for i, nonterm in zip(range(0, len(nonterm_list)), nonterm_list):
		for j, token in zip(range(0, len(nonterm.grammarDescription)),\
			nonterm.grammarDescription):
		
			if token in nonterminals:
				derivation_list = search_nonterm_list(nonterm_list, token)
				first = nonterm_list[i].grammarDescription[:j] 
				second = nonterm_list[i].grammarDescription[j:]
				nonterm_list[i].grammarDescription = first + \
					derivation_list + second
				nonterm_list[i].TEST_Duplicates = derivation_list
				break 

	return nonterm_list


def parse_grammar_file(grammar: str) -> Language:
	"""This file parses the grammar file.

	:param: grammar: The entire grammar file in string form.
	"""
	rule_line = grammar.split("\n")
	terminals, nonterminals = extract_terminals_and_nonterminals(grammar)
	nonterm_list = list()
	term_list = list()

	for rule in rule_line:
		nonterm_list += make_productions(rule, nonterminals)

	for terminal in terminals:
		term_list.append(make_terminal(terminal))

	nonterm_list = expand_production_list(nonterm_list, nonterminals)

	nonterm_list = tag_unique_grammar_names(nonterm_list)

	for nonterm in nonterm_list:
		print(nonterm.string())

	return set(terminals), set(nonterminals),\
		nonterm_list, term_list
