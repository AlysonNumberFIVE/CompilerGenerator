
package main 

import (
	"fmt"
	"strings"
	"io/ioutil"
	"regexp"
	"log"
)

type acceptingState struct {
	pos		int
	state 	string
}

type stack struct {
	item []*acceptingState
	height int
}

var dval 		string
var delim 		bool
var content		string
var index 		int
var stck 		*stack

func initStack() *stack {
	return &stack{
		height: 0,
	}
}

func (s *stack)push(pos int, currSstate string) {
	item := &acceptingState{
		pos: pos,
		state: currSstate,
	}
	s.item = append(s.item, item)
	s.height++
}

func (s *stack)pop() *acceptingState{
	if s.height == 0 {
		return nil
	}
	s.height--
	toReturn := s.item[s.height]
	s.item = s.item[:s.height]
	return toReturn
}

func (s *stack)clear() {
	s.item = []*acceptingState{}
	s.height = 0
}

func (s *stack)print() {
	for _, c := range s.item {
		fmt.Printf("%d -> %s\n", c.pos, c.state)
	}
}

func nextChar() string {
	if index < len(content) {
		c := string(content[index])
		index++
		return c
	}
	fmt.Println("EOF")	
	return ""
}

func rollBack() (string, int) { 
	if stck.height > 0 {
		value := stck.pop()
		return value.state, value.pos
	}
	return "", index
}

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

func regexPrefix(pattern string, currTok string) bool {
	match, _ := regexp.Compile(pattern)
	test := match.FindStringIndex(currTok)
	if len(test) > 0 {
		if test[0] == 0 && test[1] > 0 {
			return true
		}
	}
	return false
}

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

func scanDelimList(currToken string) bool {
	for k := range delimList {
		if k == currToken || evalRegex(currToken, k) == true {
			return true
		}
	}
	return false
}

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
			stck.push(index, currTok.String())
		} else if checker == -1 {
			tmp, index = rollBack()
			currTok.Reset()
			currTok.WriteString(tmp)
			break
		}
	}
	stck.clear()
	if scanDelimList(currTok.String()) == true {
		stck.push(index, currTok.String())
		delim = true
		return 
	}
	addToken(currTok.String(), "")
}

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
	stck = initStack()
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

