
package main

import (
	"fmt"
)

// token is a struct for each token. line value to be preserved for multi-source file support.
type token struct {
	line 		int
	name		string
	datatype	string
}

// tokenList is a list that holds all tokens in the source file.
type tokenList struct {
	tList 		[]*token
	height 		int
}

// initTokenList initializes a token list struct
func initTokenList() *tokenList {
	return &tokenList{}
}

// global tokens list
var tokens *tokenList

// push token adds a token to the overall token list
func (s *tokenList)pushToken(name string, datatype string) {
	item := &token{
		line: 0,
		name: name,
		datatype: datatype,
	}
	s.tList = append(s.tList, item)
	s.height++ 
}

// addDelimToken adds tokens in the delim list to the token list
func addDelimToken(value string, eval string) {
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

// addToken adds a token to the token list
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

// ListTokens prints a list of all saved tokens
func (s *tokenList)listTokens() {
	for _, token := range s.tList {
		if len(token.name) == 0 {
			continue
		}
		fmt.Printf("name : %s  type : %s\n", token.name, token.datatype)
	}
}
