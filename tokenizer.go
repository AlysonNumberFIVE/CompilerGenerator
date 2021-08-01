
package main

import (
	"fmt"
)

type token struct {
	line 		int
	name		string
	datatype	string
}

type tokenList struct {
	tList 		[]*token
	height 		int
}

func initTokenList() *tokenList {
	return &tokenList{}
}

var tokens *tokenList

func (s *tokenList)pushToken(name string, datatype string) {
	item := &token{
		line: 0,
		name: name,
		datatype: datatype,
	}
	s.tList = append(s.tList, item)
	s.height++ 
}

func addDelimToken(value string, eval string) {
	fmt.Println("eval is ", eval)
	var index int

	index = 0
	for index < len(delimList) {
		for key, dtype := range tokenType {
			if key == eval {
				if evalRegex(value, key) == true {
					tokens.pushToken(value, dtype)
					return 
				}
			}
		}
		index++	
	}
}

func addToken(value string, datatype string) {
	if len(datatype) > 0 && len(value) > 0 {
		tokens.pushToken(value, datatype)
		return 
	}
	if _, exists := tokenType[value]; exists {
		tokens.pushToken(value, tokenType[value])
		return 
	}
	for _, pattern := range regexList {
		for key, dtype := range tokenType {
			if key == pattern {
				if evalRegex(value, key) == true {
					tokens.pushToken(value, dtype)
					break
				}
			}
		}  
	}
}

func (s *tokenList)listTokens() {
	for _, token := range s.tList {
		if len(token.name) == 0 {
			continue
		}
		fmt.Printf("name : %s  type : %s\n", token.name, token.datatype)
	}
}
