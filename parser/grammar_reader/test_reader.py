
import reader
import pytest

class ExtractTerminalAndNonterminalTestCases(object):
	
	def __init__(self, testcase: str, expected_nonterms: list,
		expected_terms: list):
		self.testcase = testcase
		self.expected_nonterms = expected_nonterms
		self.expected_terms = expected_terms

def test_extract_terminals_and_nonterminals():

	testcases = list()
	testcases.append(
		ExtractTerminalAndNonterminalTestCases(
			testcase="""whileStmt -> while ( condition ) wBody
forStmt -> for ( assign ; condition ; math ) forBody
variable -> var ID = LITERAL | var ID = ID | var ID DATATYPE
condition -> CONDITIONAL
math -> MATH
assign -> variable = LITERAL""",
			expected_nonterms=["whileStmt", "forStmt", "variable",
	 			"condition", "math", "assign", "condition"],
			expected_terms=["while", "(", ")", "wBody",
				"for", ";", "forBody",
				"var", "ID", "=", "LITERAL", "DATATYPE",
				"CONDITIONAL", "MATH"]
		)
	)
	testcases.append(
		ExtractTerminalAndNonterminalTestCases(
			testcase='''doStmt -> do { fBody } while ( condition )''',
			expected_nonterms=["doStmt"],
			expected_terms = ["do", "{", "fBody", "}", "while", "(", "condition", ")"]
		)
	)
	testcases.append(
		ExtractTerminalAndNonterminalTestCases(
			testcase='''fBody -> variable ;
variable -> dataVar
dataVar -> DATATYPE ID''',
			expected_terms=["DATATYPE", "ID", ";"],
			expected_nonterms=["dataVar", "fBody", "variable"]
		)
	)

	for tc in testcases:
		actual_terms, actual_nonterms = \
			reader.extract_terminals_and_nonterminals(tc.testcase)

		for term in actual_terms:
			assert term in tc.expected_terms

		for nonterm in actual_nonterms:
			assert nonterm in tc.expected_nonterms

		assert sorted(actual_terms) == sorted(tc.expected_terms)


class MakeProductionsTestCases(object):

	def __init__(self, rule: str, nonterminals: list,
		expected: list):
		self.rule = rule
		self.nonterminals = nonterminals
		self.expected = expected


def assert_language_object(expected: reader.Language,
							actual: reader.Language) -> bool:
	



def test_make_production():

	testcases = list()
	testcases.append(
		MakeProductionsTestCases(
			rule="whileStmt -> ( condition ) wBody",
			nonterminals=["whileStmt"],
			expected=[
				Language(
					grammarName="whileStmt",
					nonterminal=True,
					derivNum=0, 
					grammarDescription=["(", "condition", ")", "wBody"]
				)
			]
		)
	)

	for tc in testcases:
		actual = reader.make_production()


