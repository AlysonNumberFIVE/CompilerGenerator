/*
** This file is autogenerated. Edit at your own peril.
*/

#include <stdlib.h>
#include <string.h>

typedef struct s_error {
        void *none;
}       errormsg;

typedef struct s_metaData {
	char 	*name;
	int 	line;

	char	*error;
}	metaData;



// Struct for s_while
typedef struct	s_while {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_while;

t_while *init_term_while() {
	t_while *new_term = (t_while *)malloc(sizeof(t_while));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_openbrace
typedef struct	s_openbrace {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_openbrace;

t_openbrace *init_term_openbrace() {
	t_openbrace *new_term = (t_openbrace *)malloc(sizeof(t_openbrace));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_closebrace
typedef struct	s_closebrace {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_closebrace;

t_closebrace *init_term_closebrace() {
	t_closebrace *new_term = (t_closebrace *)malloc(sizeof(t_closebrace));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_wBody
typedef struct	s_wBody {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_wBody;

t_wBody *init_term_wBody() {
	t_wBody *new_term = (t_wBody *)malloc(sizeof(t_wBody));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_for
typedef struct	s_for {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_for;

t_for *init_term_for() {
	t_for *new_term = (t_for *)malloc(sizeof(t_for));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_semicolon
typedef struct	s_semicolon {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_semicolon;

t_semicolon *init_term_semicolon() {
	t_semicolon *new_term = (t_semicolon *)malloc(sizeof(t_semicolon));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_forBody
typedef struct	s_forBody {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_forBody;

t_forBody *init_term_forBody() {
	t_forBody *new_term = (t_forBody *)malloc(sizeof(t_forBody));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_var
typedef struct	s_var {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_var;

t_var *init_term_var() {
	t_var *new_term = (t_var *)malloc(sizeof(t_var));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_ID
typedef struct	s_ID {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_ID;

t_ID *init_term_ID() {
	t_ID *new_term = (t_ID *)malloc(sizeof(t_ID));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_equ
typedef struct	s_equ {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_equ;

t_equ *init_term_equ() {
	t_equ *new_term = (t_equ *)malloc(sizeof(t_equ));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_LITERAL
typedef struct	s_LITERAL {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_LITERAL;

t_LITERAL *init_term_LITERAL() {
	t_LITERAL *new_term = (t_LITERAL *)malloc(sizeof(t_LITERAL));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_DATATYPE
typedef struct	s_DATATYPE {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_DATATYPE;

t_DATATYPE *init_term_DATATYPE() {
	t_DATATYPE *new_term = (t_DATATYPE *)malloc(sizeof(t_DATATYPE));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_CONDITIONAL
typedef struct	s_CONDITIONAL {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_CONDITIONAL;

t_CONDITIONAL *init_term_CONDITIONAL() {
	t_CONDITIONAL *new_term = (t_CONDITIONAL *)malloc(sizeof(t_CONDITIONAL));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


// Struct for s_MATH
typedef struct	s_MATH {
	char 		*name;
	metaData 	*metadata;
	int 		deriv_number;
	void		*prev;
	errormsg 	*error;
}	t_MATH;

t_MATH *init_term_MATH() {
	t_MATH *new_term = (t_MATH *)malloc(sizeof(t_MATH));

	new_term->name = strdup("");
	new_term->metadata = (metaData *)malloc(sizeof(metaData));
	new_term->deriv_number = -1;
	new_term->error = (errormsg *)malloc(sizeof(errormsg));
	return (new_term);
}


#include <stdlib.h>
#include <stdio.h>

typedef struct	s_info 
{
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
}	t_info;

	
typedef struct s_whileStmt {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_while *_while0;
	struct s_openbrace *_openbrace1;
	struct s_condition *_condition2;
	struct s_condition *_condition3;
	struct s_closebrace *_closebrace4;
}	t_whileStmt;
	
typedef struct s_forStmt {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_for *_for0;
	struct s_openbrace *_openbrace1;
	struct s_assign *_assign2;
	struct s_assign *_assign3;
	struct s_semicolon *_semicolon4;
	struct s_condition *_condition5;
	struct s_semicolon *_semicolon6;
	struct s_math *_math7;
	struct s_closebrace *_closebrace8;
}	t_forStmt;
	
typedef struct s_variable {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_var *_var0;
	struct s_ID *_ID1;
	struct s_equ *_equ2;
	struct s_LITERAL *_LITERAL3;
}	t_variable;
	
typedef struct s_variable1 {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_var *_var0;
	struct s_ID *_ID1;
	struct s_equ *_equ2;
	struct s_ID *_ID3;
}	t_variable1;
	
typedef struct s_variable2 {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_var *_var0;
	struct s_ID *_ID1;
	struct s_DATATYPE *_DATATYPE2;
}	t_variable2;
	
typedef struct s_condition {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_CONDITIONAL *_CONDITIONAL0;
}	t_condition;
	
typedef struct s_math {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_MATH *_MATH0;
}	t_math;
	
typedef struct s_assign {
	char 		*name;
	metaData	*metadata;
	int 		deriv_number;
	void		*prev;
	void		*next;
	errormsg	*error;
	struct s_variable *_variable0;
	struct s_variable1 *_variable11;
	struct s_variable2 *_variable22;
}	t_assign;




void 	*init_nonterm_whileStmt () {
	t_whileStmt *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_while0 = (struct s_while*)malloc(sizeof(struct s_while));
	new_ptr->_openbrace1 = (struct s_openbrace*)malloc(sizeof(struct s_openbrace));
	new_ptr->_condition2 = (struct s_condition*)malloc(sizeof(struct s_condition));
	new_ptr->_condition3 = (struct s_condition*)malloc(sizeof(struct s_condition));
	new_ptr->_closebrace4 = (struct s_closebrace*)malloc(sizeof(struct s_closebrace));
	return (new_ptr);
}

void 	*init_nonterm_forStmt () {
	t_forStmt *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_for0 = (struct s_for*)malloc(sizeof(struct s_for));
	new_ptr->_openbrace1 = (struct s_openbrace*)malloc(sizeof(struct s_openbrace));
	new_ptr->_assign2 = (struct s_assign*)malloc(sizeof(struct s_assign));
	new_ptr->_assign3 = (struct s_assign*)malloc(sizeof(struct s_assign));
	new_ptr->_semicolon4 = (struct s_semicolon*)malloc(sizeof(struct s_semicolon));
	new_ptr->_condition5 = (struct s_condition*)malloc(sizeof(struct s_condition));
	new_ptr->_semicolon6 = (struct s_semicolon*)malloc(sizeof(struct s_semicolon));
	new_ptr->_math7 = (struct s_math*)malloc(sizeof(struct s_math));
	new_ptr->_closebrace8 = (struct s_closebrace*)malloc(sizeof(struct s_closebrace));
	return (new_ptr);
}

void 	*init_nonterm_variable () {
	t_variable *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_var0 = (struct s_var*)malloc(sizeof(struct s_var));
	new_ptr->_ID1 = (struct s_ID*)malloc(sizeof(struct s_ID));
	new_ptr->_equ2 = (struct s_equ*)malloc(sizeof(struct s_equ));
	new_ptr->_LITERAL3 = (struct s_LITERAL*)malloc(sizeof(struct s_LITERAL));
	return (new_ptr);
}

void 	*init_nonterm_variable1 () {
	t_variable1 *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_var0 = (struct s_var*)malloc(sizeof(struct s_var));
	new_ptr->_ID1 = (struct s_ID*)malloc(sizeof(struct s_ID));
	new_ptr->_equ2 = (struct s_equ*)malloc(sizeof(struct s_equ));
	new_ptr->_ID3 = (struct s_ID*)malloc(sizeof(struct s_ID));
	return (new_ptr);
}

void 	*init_nonterm_variable2 () {
	t_variable2 *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_var0 = (struct s_var*)malloc(sizeof(struct s_var));
	new_ptr->_ID1 = (struct s_ID*)malloc(sizeof(struct s_ID));
	new_ptr->_DATATYPE2 = (struct s_DATATYPE*)malloc(sizeof(struct s_DATATYPE));
	return (new_ptr);
}

void 	*init_nonterm_condition () {
	t_condition *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_CONDITIONAL0 = (struct s_CONDITIONAL*)malloc(sizeof(struct s_CONDITIONAL));
	return (new_ptr);
}

void 	*init_nonterm_math () {
	t_math *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_MATH0 = (struct s_MATH*)malloc(sizeof(struct s_MATH));
	return (new_ptr);
}

void 	*init_nonterm_assign () {
	t_assign *new_ptr;

	new_ptr->name = strdup("");
	new_ptr->metadata = (metaData *)malloc(sizeof(metaData));
	new_ptr->error = (errormsg *)malloc(sizeof(errormsg));
	new_ptr->_variable0 = (struct s_variable*)malloc(sizeof(struct s_variable));
	new_ptr->_variable11 = (struct s_variable1*)malloc(sizeof(struct s_variable1));
	new_ptr->_variable22 = (struct s_variable2*)malloc(sizeof(struct s_variable2));
	return (new_ptr);
}
