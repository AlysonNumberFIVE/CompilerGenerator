
import sys

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from grammar_reader import reader
import welder.templates

ENV = Environment(
	loader=FileSystemLoader(next(iter(welder.templates.__path__)))
)
ENV.globals.update(zip=zip)


def generate_grammar(grammar: str): 

	terminals, nonterminals, nonterm_list, term_list = \
		reader.parse_grammar_file(grammar)
	for nonterm in nonterm_list:
		print("duplicates are ", nonterm.TEST_Duplicates)

	fd = open('test2.c', 'w')
	content = str()

	template = ENV.get_template("terminal_lib.jinja")
	print(template.render(terminals=term_list))
	content += template.render(terminals=term_list)

	template = ENV.get_template("nonterminal_lib.jinja")
	print(template.render(nonterminals=nonterm_list))
	content += template.render(nonterminals=nonterm_list)

	template = ENV.get_template("functions.jinja")
	print(template.render(nonterminals=nonterm_list))



	fd.write(content)
	fd.close()


grammar = """whileStmt -> while openbrace condition closebrace wBody
forStmt -> for openbrace assign semicolon condition semicolon math closebrace forBody
variable -> var ID equ LITERAL | var ID equ ID | var ID DATATYPE
condition -> CONDITIONAL
math -> MATH
assign -> variable equ LITERAL"""
generate_grammar(grammar)




