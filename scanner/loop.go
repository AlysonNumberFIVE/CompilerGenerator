
package main 

import (
	"fmt"
	"strings"
	"io/ioutil"
	"regexp"
	"log"

	stack "github.com/AlysonBee/CompilerGenerator/stack"
)

var dval 		string
var delim 		bool
var content		string
var index 		int
var stck 		*stack.Stack

// nextChar advances the index into the source file while returning the current token
func nextChar() string {
	if index < len(content) {
		c := string(content[index])
		index++
		return c
	}
	fmt.Println("EOF")	
	return ""
}

// rollBack restores the index position and value of the last valid/accepted token.
func rollBack() (string, int) { 
	if stck.Height > 0 {
		value := stck.Pop()
		return value.State, value.Pos
	}
	return "", index
}

// evalRegex evaluates if a regex passes or not. A wrapper function for Go FindStringIndex.
func evalRegex(currTok string, pattern string) bool {
	match, _ := regexp.Compile(pattern)
	test := match.FindStringIndex(currTok)
	if len(test) > 0 {
		tmp := currTok[test[0]:test[1]]
		if tmp == currTok {
			return true
		}
	}
	return false
}

// vaildPrefix helps determine if currTok is a complete regex and, if not,
// helps determine if it is at least a prefix to a longer regex to prevent premature
// tokenization failure if it is a prefix.
func validPrefix(currTok string) int {
	for pattern := range delimList {
		if evalRegex(currTok, pattern) == true {
			return 1
		}
	}
	for pattern := range delimList {
		if strings.HasPrefix(pattern, currTok) == true {
			fmt.Printf("%s %s\n", pattern, currTok)
			return 0
		}
	}
	for _, pattern := range regexList {
		if evalRegex(currTok, pattern) == true {
			return 1
		}
	}
	return -1
}

// scanDelimList is a helper function for singleToken and is to determine if a
// token is the first part to a delimited token.
func scanDelimList(currToken string) bool {
	for k := range delimList {
		if k == currToken || evalRegex(currToken, k) == true {
			return true
		}
	}
	return false
}

// singleToken is used to tokenize single tokens that aren't part of the delimited list
func singleToken() {
	var tmp 	string
	var currTok strings.Builder 
	var c 		string
	var checker int

	for {
		c = nextChar()
		if len(c) == 0 {
			tmp, index = rollBack()
			break 
		}
		currTok.WriteString(c)
		checker = validPrefix(currTok.String())
		if checker == 1 {
			stck.Push(index, currTok.String())
		} else if checker == -1 {
			tmp, index = rollBack()
			currTok.Reset()
			currTok.WriteString(tmp)
			break
		}
	}
	stck.Clear()
	if scanDelimList(currTok.String()) == true {
		stck.Push(index, currTok.String())
		delim = true
		return 
	}
	addToken(currTok.String(), "")
}

// determinePattern determines which regex pattern findPattern falls under and
// returns it. used in HandleDelim to determine which delim regex is to be applied 
func determinePattern(findPattern string) string {
	for pattern, ver := range delimList {
		if pattern == findPattern {
			return ver
		}
	}
	return ""
}

// handleDelim is responsible for handling the tokenizing of delimiter based tokens
func handleDelim() {
	var totalTok strings.Builder
	var c 		 string
	var pattern	 string

	pattern, index = rollBack()
	eval := determinePattern(pattern)
	totalTok.WriteString(pattern)
	for {
		c = nextChar()
		if len(c) == 0 {
			break 
		}
		totalTok.WriteString(c)
		if evalRegex(totalTok.String(), eval) == true {
			break
		}
	}
	addDelimToken(totalTok.String(), eval)
	delim = false
}

// initScanner initializes scanner specific variables; the source code file(s),
// an empty token list and empty accepting state stack
func initScanner(filename string) {
	tmp, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	tokens = initTokenList()
	content = string(tmp)
	stck = stack.InitStack()
	index = 0
}

// scan is the main loop that passes over the source code file input
func scan(filename string) {
	initScanner(filename)
	for {
		if index >= len(content) {
			break
		}
		singleToken()
	
		if delim == true {
			handleDelim()
		}
	}
	tokens.listTokens()
}

