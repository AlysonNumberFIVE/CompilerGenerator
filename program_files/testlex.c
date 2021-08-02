size_t  read_count = 0;
size_t  line = 0;
t_hashtable *table = NULL;
char	*current_file;

t_token     *scan(char *buffer, t_hashtable *table)
{
    size_t  i;
    size_t  buff_size;
    char    *temp;

    buff_size = strlen(buffer);
    for (i = read_count; i < buff_size; i++)
    {
        if (buffer[i] == ' ' || buffer[i] == '\t') continue;
        else if (buffer[i] == '\n') line++;
        else break;
    }
    read_count = i; 
    // handle comments
    if (buffer[read_count] == '/' && (buffer[read_count + 1] == '/' || buffer[read_count + 1] == '*'))
        return (skip_comments(buffer, read_count));
    
    // handle header/includes 
    if (buffer[read_count] == '<' && isalpha(buffer[read_count + 1]))
        return (header_found(buffer, read_count));
    
    // handle all tokens of double character (i.e ==, >=, !=, || ...)
    if (buffer[read_count] == '<') return (double_token(buffer, read_count, table, "LESS"));
    if (buffer[read_count] == '&') return (double_token(buffer, read_count, table, "BINTAND"));
    if (buffer[read_count] == '|') return (double_token(buffer, read_count, table, "BITOR"));
    if (buffer[read_count] == '=') return (double_token(buffer, read_count, table, "ASSIGN"));
    if (buffer[read_count] == '!') return (double_token(buffer, read_count, table, "NOT"));
    if (buffer[read_count] == '>') return (double_token(buffer, read_count, table, "GREATER"));
    if (buffer[read_count] == '%') return (double_token(buffer, read_count, table, "MOD"));
    if (buffer[read_count] == '+') return (double_token(buffer, read_count, table, "PLUS"));
    if (buffer[read_count] == '-') return (double_token(buffer, read_count, table, "MINUS"));
    if (buffer[read_count] == '/') return (double_token(buffer, read_count, table, "DIV"));
    if (buffer[read_count] == '*') return (double_token(buffer, read_count, table, "MULTI"));
    if (buffer[read_count] == '^') return (double_token(buffer, read_count, table, "XOR"));
    
    // handle IDs and Digits
    if (isalpha(buffer[read_count]) || buffer[read_count] == '_') 
        return (id_found(buffer, read_count));
    if (isdigit(buffer[read_count])) return (number_found(buffer, read_count));
    
    // handle preprocessor macros
    if (buffer[read_count] == '#') return (macro_found(buffer, read_count));

    // handle literals/strings
    if (buffer[read_count] == '\"') return (literal_found(buffer, read_count));
    
    // handle single characters
    if (buffer[read_count] == '\'') return (character_found(buffer, read_count));

    // handlie all single tokens.
    if (buffer[read_count] == '.') return (ellipse_found(buffer, read_count, "DOT"));
    if (buffer[read_count] == ';') return (single_token(buffer, read_count, "SEMICOLON"));
    if (buffer[read_count] == '(') return (single_token(buffer, read_count, "OPENBRACKET"));
    if (buffer[read_count] == ')') return (single_token(buffer, read_count, "CLOSEBRACKET")); 
    if (buffer[read_count] == '{') return (single_token(buffer, read_count, "OPENBRACE"));
    if (buffer[read_count] == '}') return (single_token(buffer, read_count, "CLOSEBRACE"));
    if (buffer[read_count] == '+') return (single_token(buffer, read_count, "PLUS"));
    if (buffer[read_count] == '-') return (single_token(buffer, read_count, "MINUS"));
    if (buffer[read_count] == '%') return (single_token(buffer, read_count, "MODULO"));
    if (buffer[read_count] == ',') return (single_token(buffer, read_count, "COMMA"));
    if (buffer[read_count] == '/') return (single_token(buffer, read_count, "DIVIDE"));
    if (buffer[read_count] == '*') return (single_token(buffer, read_count, "MULTI"));
    if (buffer[read_count] == '?') return (single_token(buffer, read_count, "QMARK"));
    if (buffer[read_count] == ':') return (single_token(buffer, read_count, "COLON"));
    if (buffer[read_count] == '[') return (single_token(buffer, read_count, "OPENSQUARE"));
    if (buffer[read_count] == ']') return (single_token(buffer, read_count, "CLOSESQUARE"));
    //if (buffer[read_count] == '.') return (single_token(buffer, read_count, "DOT"));
    if (buffer[read_count] == '\\') return (single_token(buffer, read_count, "LINECONT"));
    if (buffer[read_count] == '~') return (single_token(buffer, read_count, "TILDE"));
    if (buffer[read_count] == '^') return (single_token(buffer, read_count, "XOR"));
    if (buffer[read_count] == '?') return (single_token(buffer, read_count, "QUESTIONMARK"));
    if (buffer[read_count] == '@') return (single_token(buffer, read_count, "AT_LOCATION"));
    return (NULL);
}

t_hashtable     *key_token(void)
{
    t_hashtable *table;

    table = create_table(1000);
    ht_insert(table, "+=", "ADD_ASSIGN");
    ht_insert(table, "-=", "SUB_ASSIGN");
    ht_insert(table, "*=", "MUL_ASSIGN");
    ht_insert(table, "/=", "DIV_ASSIGN");
    ht_insert(table, "%=", "MOD_ASSIGN");
    ht_insert(table, "^=", "XOR_ASSIGN");
    ht_insert(table, "|=", "OR_ASSIGN");
    ht_insert(table, ">>", "RIGHT_OP");
    ht_insert(table, "<<", "LEFT_OP");
    ht_insert(table, "<<=", "LEFT_OP_ASSIGN");
    ht_insert(table, ">>=", "RIGHT_OP_ASSIGN");
    ht_insert(table, "&&", "AND");
    ht_insert(table, "||", "OR");
    ht_insert(table, "&=", "AND_ASSIGN");
    ht_insert(table, "<=", "LE_OP");
    ht_insert(table, ">=", "GE_OP");
    ht_insert(table, "==", "EQ_OP");
    ht_insert(table, "++", "INC_OP");
    ht_insert(table, "--", "DEC_OP");
    ht_insert(table, "!=", "NE_OP");;
    ht_insert(table, "...", "ELLIPSE");
    ht_insert(table, "->", "PTR_OP");
    return (table);
}

t_token     *lexer(t_file *next_file)
{
    t_hashtable *table;
    t_token     *list;
    t_token     *temp;
    size_t      size;
    t_file	*file_list;

    list = NULL;
    table = key_token();
    file_list = next_file;
    while (file_list)
    {    
        line = 1;
        read_count = 0;
    	size = strlen(file_list->solidcontent);
	current_file = strdup(file_list->filename); 
	
	while (read_count < size)
    	{
	    temp = scan(file_list->solidcontent, table);
            if (temp)
            {
         	list = push_token(list, temp->name, temp->type, temp->line, file_list->filename);
            	free_token(temp); 
            }
        }
	file_list = file_list->next;
    }
   
    return (list);
}