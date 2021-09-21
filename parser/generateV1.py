
import sys

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from grammar_reader import reader
import welder.templates

ENV = Environment(
	loader=FileSystemLoader(next(iter(welder.templates.__path__)))
)


def generate_grammar(grammar: str): 

	terminals, nonterminals, nonterm_list, term_list = \
		reader.parse_grammar_file(grammar)

	template = ENV.get_template("terminal_lib.jinja")
	print(template.render(terminals=term_list))

	template = ENV.get_template("nonterminal_lib.jinja")
	print(template.render(nonterminals=nonterm_list))

	


grammar = """whileStmt -> while openbrace condition closebrace wBody
forStmt -> for openbrace assign semicolon condition semicolon math closebrace forBody
variable -> var ID equ LITERAL | var ID equ ID | var ID DATATYPE
condition -> CONDITIONAL
math -> MATH
assign -> variable equ LITERAL"""
generate_grammar(grammar)




