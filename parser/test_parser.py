from __future__ import absolute_import

import pytest
	parser


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


class TestParser:

	def __init__(self, source_code:str, tokens:str,
		expected:list, recovery_list:list):
		self.soruce_code = source_code
		self.tokens = tokens
		self.expected = expected
		self.recovery_list = recovery_list


def test_parser():

	testcases = list()
	testcases.append(
		TestParser(
			"""var i string""",
			"var:var\ni:ID\nstring:DATATYPE",
			["var", "i", "string"],
			["var"]
		),
	)

	for t in testcases:
		rules_obj = parser.create_grammar(grammar)

		all_rules = parser.create_existing_rules(grammar)

		actual = parser.source_code_scanner(
			t.tokens,
			rules_obj,
			grammar,
			t.recovery_list
		)

		print(actual)


test_parser()




		





