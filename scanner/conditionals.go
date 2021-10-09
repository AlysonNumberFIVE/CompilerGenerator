package main

import (
	"fmt"
	"strings"
)


var	startTokens = []string{"if", "("}
var endTokens = []string{")", "{"}
/*
// token is a struct for each token. line value to be preserved for multi-source file support.
type token struct {
        line            int
        name            string
        datatype        string
        filename        string
}

// tokenList is a list that holds all tokens in the source file.
type tokenList struct {
        tList           []*token
        height          int
}

// initTokenList initializes a token list struct
func initTokenList() *tokenList {
        return &tokenList{}
}

// global tokens list
var tokens *tokenList

// push token adds a token to the overall token list
func (s *tokenList)pushToken(name string, datatype string, line int, filename string) {
        item := &token{
                line: line,
                name: name,
                datatype: datatype,
                filename: filename,
        }
        s.tList = append(s.tList, item)
        s.height++
}
*/
type conditionalStack struct {
	height 		int
	tokenStack	[]string
	flag 		bool
}

func initConditionalStack() *conditionalStack {
	return &conditionalStack{
		height: 0,
		flag: false,
	}
}

func (c *conditionalStack)print() {
	for _, token := range c.tokenStack {
		fmt.Println("token is ", token)
	}
}

func (c *conditionalStack)pushConditional(token string) {
	c.height++
	c.tokenStack = append(c.tokenStack, token)
	if c.flag == false {
		c.flag = true
	} else {
		c.flag = false
	}
}

func (c *conditionalStack)replace(token string) {
	c.tokenStack[c.height] = token
}

func (c *conditionalStack)toString() string {
	var buffer strings.Builder

	for _, token := range c.tokenStack {
		buffer.WriteString(token)
		buffer.WriteString(" ")
	}
	return buffer.String()
}

func (c *conditionalStack)clearConditional() {
	c.height = 0
	c.tokenStack = []string{}
	c.flag = false
}

func checkEnd(end []string, tokens *tokenList, counter int) bool {
	i := 0

	for i < len(endTokens) {
		if counter == len(tokens.tList) {
			return false
		}
		if endTokens[i] != tokens.tList[counter].name {
			return false
		}
		i++
		counter++
	}
	return true
}

func determineConditional(tokens *tokenList, i int) (int, string) {
	c := initConditionalStack()
	isNot := false

	for i < len(tokens.tList) {
		token := tokens.tList[i]

		fmt.Println("c ", token.name)
		if checkEnd(endTokens, tokens, i) {
			fmt.Println("End tokens")
			break
		}

		if token.datatype == "NOT" {
			isNot = true
			c.tokenStack = append(c.tokenStack, token.name)
		} else if token.datatype == "CONDITION" {
			if c.flag == true && isNot == false {
				c.pushConditional(token.name)
			} 
		} else if token.datatype == "NUMBER" || token.datatype == "ID" {
			if c.flag == false {
				fmt.Println("Pushing ", token.name)
				c.pushConditional(token.name)
			} else {
				c.clearConditional()
				c.pushConditional(token.name)
			}
		} else {
			c.tokenStack = append(c.tokenStack, token.name)
		}

		i++
	}
	fmt.Println("flag is ", c.flag)
	if c.flag == true {
		c.print()
	} 
	return i + len(endTokens), c.toString()
}

func checkStart(startTokens []string, tokens *tokenList, counter int) bool {
	i := 0

	for i < len(startTokens) {
		if counter >= len(tokens.tList) {
			return false
		}
		if startTokens[i] != tokens.tList[counter].name {
			return false
		}
		i++
		counter++
	}
	return true
}

func reshapeList(tokens *tokenList, start int, end int, conditionString string) *tokenList {
	firstHalf := tokens.tList[:start]
	secondHalf := tokens.tList[end:]

	var newList []*token
	for _, f := range firstHalf {
		newList = append(newList, f)
	}
	newList = append(newList, &token{-1, conditionString, "CONDITIONAL",  "TEST"})

	for _, s := range secondHalf {
		newList = append(newList, s)
	}
	fmt.Println("conditionString ", conditionString)
	tokens.tList = newList
	for _, t := range tokens.tList {
		fmt.Println("t ", t.name)
	}
	return tokens
}


func collapseTour(t *tokenList) * tokenList{
	// generic conditional markers

	listing := []string{
	// "if ( - ) {",
		"while ( - ) {",
	//	"for ( - ) {",
	}
	var conditionString string

	for i := range tokens.tList {
		for _, line := range listing {
			startEnd := strings.Split(line, " - ")
			startTokens = strings.Fields(startEnd[0])
			endTokens = strings.Fields(startEnd[1])
		
			if checkStart(startTokens, t, i) {
				i += len(startTokens)

				firstHalf := i
				i, conditionString = determineConditional(t, i)

				secondHalf := i - len(endTokens)
				fmt.Println("first is ", firstHalf)
				fmt.Println("second is ", secondHalf)
				t = reshapeList(t, firstHalf, secondHalf, conditionString)
			}
		}
	}
	t.listTokens()
	return t
}

/*
func main() {

	tokens := initTokenList()
	// 1 && 2 < 4
	
	tokens.pushToken("1", "NUMBER", -1, "TEST")
	tokens.pushToken("42", "NUMBER", -1, "TEST")
	tokens.pushToken("&&", "CONDITION", -1, "TEST")
	tokens.pushToken("2", "NUMBER", -1, "TEST")
	tokens.pushToken("<", "CONDITION", -1, "TEST")
//	tokens.pushToken("4", "NUMBER", -1, "TEST")

	determineConditional(tokens, "{")

	fmt.Println("+===============")
	// 4 && 8 < 88 > 24 + 47 + !)42)
	tokens = initTokenList()
	
	tokens.pushToken("if", "IF", -1, "TEST")
	tokens.pushToken("(", "OPENBRACE", -1, "TEST")
	
	tokens.pushToken("4", "NUMBER", -1, "TEST")
	tokens.pushToken("&&", "CONDITION", -1, "TEST")
	tokens.pushToken("8", "NUMBER", -1, "TEST")
	tokens.pushToken("<", "CONDITION", -1, "TEST")
	tokens.pushToken("&&", "NUMBER", -1, "TEST")
	tokens.pushToken(">", "CONDITION", -1, "TEST")
	tokens.pushToken("24", "NUMBER", -1, "TEST")
	tokens.pushToken("+", "CONDITION", -1, "TEST")
	tokens.pushToken("47", "NUMBER", -1, "TEST")
	tokens.pushToken("+", "CONDITION", -1, "TEST")
	tokens.pushToken("!", "NOT", -1, "TEST")
	tokens.pushToken(")", "CLOSEBRACE", -1, "TEST")
	tokens.pushToken("42", "NUMBER", -1, "TEST")

	tokens.pushToken(")", "CLOSEBRACE", -1, "TEST")
	tokens.pushToken("{", "OPENCURLY", -1, "TEST")
	tokens.pushToken("i", "ID", -1, "TEST")
	tokens.pushToken("=", "EQU", -1, "TEST")
	collapseTour(tokens)
//	determineConditional(tokens, "{")	

}*/




