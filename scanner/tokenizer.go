
package main

import (
	"os"
	"fmt"
	"log"
	"strings"
	"strconv"
)

// token is a struct for each token. line value to be preserved for multi-source file support.
type token struct {
	line 		int
	name		string
	datatype	string
	filename 	string
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

// addDelimToken adds tokens in the delim list to the token list
func addDelimToken(value string, eval string, line int, filename string) {
	var index int

	index = 0
	for index < len(delimList) {
		for key, dtype := range tokenType {
			if key == eval {
				if evalRegex(value, key) == true {
					tokens.pushToken(value, dtype, line, filename)
					return 
				}
			}
		}
		index++	
	}
}

// addToken adds a token to the token list
func addToken(value string, datatype string, line int, filename string) {
	if len(datatype) > 0 && len(value) > 0 {
		tokens.pushToken(value, datatype, line, filename)
		return 
	}
	if _, exists := tokenType[value]; exists {
		tokens.pushToken(value, tokenType[value], line, filename)
		return 
	}
	for _, pattern := range regexList {
		for key, dtype := range tokenType {
			if key == pattern {
				if evalRegex(value, key) == true {
					tokens.pushToken(value, dtype, line, filename)
					break
				}
			}
		}  
	}
}

// writeFile writes the content of content to a token file.
func writeFile(content string) {
	f, err := os.Create("genericTokenFile.tk")
	if err != nil {
		log.Fatal(err)
	}

	_, err = f.WriteString(content)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("file written!")
}

// ListTokens prints a list of all saved tokens
func (s *tokenList)listTokens() {
	var fileBuffer strings.Builder

	for _, token := range s.tList {
		if len(token.name) == 0 {
			continue
		}
		fileBuffer.WriteString(token.name)
		fileBuffer.WriteString(":")
		fileBuffer.WriteString(token.datatype)
		fileBuffer.WriteString(":")
		fileBuffer.WriteString(strconv.Itoa(token.line))
		fileBuffer.WriteString(":")
		fileBuffer.WriteString(token.filename)
		fileBuffer.WriteString("\n")
		fmt.Printf("name : %s  type : %s  line: %d  filename: %s\n",
			token.name, token.datatype, token.line, token.filename)
	}
	writeFile(fileBuffer.String())
}





