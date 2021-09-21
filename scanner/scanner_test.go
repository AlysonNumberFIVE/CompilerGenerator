
package main

import (
	"runtime"
	"fmt"
	"testing"
)

// TestIsASCII tests the functionality of isASCII
func TestIsASCII(t *testing.T) {
	if isASCII('a') == false {
		t.Errorf("Error, 'a' is valid ASCII character")
	}

	if isASCII('3') == true {
		t.Errorf("Error, 3 is a number")
	}	
}

// TestHandleVariable tests the usage of handleVariable
func TestHandleVariable(t *testing.T) {
	gSymbolTable = make(map[string]string)

	gSymbolTable["test"] = "exists"
	gSymbolTable["test2"] = "exists too"
	value := handleVariable("{test}")
	fmt.Println("value is ", value)
	if value != "exists" {
		t.Errorf("Error - test variable name exists")
	}
	value = handleVariable("{test2}")
	if value != "exists too" {
		t.Errorf("Error - test2 variable name exists")
	}
	value = handleVariable("42")
	fmt.Println("value is now ", value)
	if value != "42" {
		t.Errorf("Error - value doesn't exist")
	}
	value = handleVariable("hello world, my name is {test} and {test2}")
	fmt.Println("Value is now ", value)
	if value != "hello world, my name is exists and exists too" {
		t.Errorf("Error - incorrect parsing")
	}
}

// TestHandleASCIICode tests the functionality of handleASCIICode
func TestHandleASCIICode(t *testing.T) {
	defaultVars = make(map[string]string)
	defaultVars["TESTWORD"] = "42"
	defaultVars["WORDx"] = "99"
	defaultVars["WORDy"] = "64"

	value := handleASCIICode("%%TESTWORD")
	if value != "42" {
		t.Errorf("Error - default variable %%TESTWORD not set")
	}
	value = handleASCIICode("%%WORDx")
	if value != "99" {
		t.Errorf("Error - default variable %%WORD2 not set")
	}
	value = handleASCIICode("%%WORDyz")
	if value == "64" {
		t.Errorf("Error - default variable %%WORD3 not parsed correctly")
	}
	value = handleASCIICode("hello world")
	if value != "" {
		t.Errorf("Error - incorrect default variable")
	}
}

// TestSkip tests the functoinality of skip()
func TestSkip(t *testing.T) {
	commentString := "# hello world, my name is Alyson"
	if skip(commentString) == false {
		t.Errorf("Error - skipping not working")
	}
	commentString = "#### second commented string"
	if skip(commentString) == false {
		t.Errorf("Error - skipping not working")
	}
	commentString = ""
	if skip(commentString) == false {
		t.Errorf("Error - skipping not working")
	}
}

// TestSetupRegexTargetList tests the usage of setupTargetList when working with setting up
// the regex section.
func TestSetupRegexTargetList(t *testing.T) {
	var testRegexConf string

	initGVars()
	if runtime.GOOS == "windows" {
		testRegexConf = "newline %NEWLINE\r\ntab %TAB\r\nspace [{tab}{newline}]\r\nalpha [a-zA-Z_]\r\ndigit [0-9]\r\nvariable {alpha}({alpha}|{digit})*\r\n"
 	} else {
 		testRegexConf = "newline %NEWLINE\ntab %TAB\nspace [{tab}{newline}]\nalpha [a-zA-Z_]\ndigit [0-9]\nvariable {alpha}({alpha}|{digit})*\n"
 	}
	setupTargetList(testRegexConf, "regex")
	if _, exists := regexList["alpha"]; exists {
		if regexList["alpha"] != "[a-zA-Z_]" {
			t.Errorf("Error - alpha variable not set")
		}
	} else {
		t.Errorf("regex value \"alpha\" doesn't exist")
	}
	if _, exists := regexList["variable"]; exists {
		if regexList["variable"] != "[a-zA-Z_]([a-zA-Z_]|[0-9])*" {
			t.Errorf("Error - variable variable not set")
		}
	} else {
		t.Errorf("regex value \"variable\" doesn't exist")
	}
	if _, exists := regexList["newline"]; exists {
		if regexList["newline"] != "\n" {
			t.Errorf("Error - variable newline not set")
		}
	} else {
		t.Errorf("regex value \"newline\" doesn't exist")
	}
	if _, exists := regexList["digit"]; exists {
		if regexList["digit"] != "[0-9]" {
			t.Errorf("Error - variabe digit not set")
		}
	} else {
		t.Errorf("regex value \"digit\" doesn't exist")
	}
	if _, exists := regexList["asdgaseref"]; exists {
		t.Errorf("Something's gone horribly wrong with regexList")
	}
}

// TestSetupDelimTargetList tests setupTargetList when setting up the 
// delim fields
func TestSetupDelimTargetList(t *testing.T) {
	var testDelimConf string

	initGVars()
	if runtime.GOOS == "windows" {
		testDelimConf = "lcomm  ''' '''.*'''\r\nscomm # #.*%NEWLINE\r\nstring \" \".*\"\r\n"
	} else {
		testDelimConf = "lcomm  ''' '''.*'''\nscomm # #.*%NEWLINE\nstring \" \".*\"\n"		
	}
	setupTargetList(testDelimConf, "delim")
	if _, exists := delimList["lcomm"]; exists {
		if delimList["lcomm"][0] != "'''" || delimList["lcomm"][1] != "'''.*'''" {
			t.Errorf("Error - lcomm delim not set properly")
		} 
	} else {
		t.Errorf("lcomm delim not set")
	}
	if _, exists := delimList["scomm"]; exists {
		if delimList["scomm"][0] != "#" || delimList["scomm"][1] != "#.*%NEWLINE" {
			t.Errorf("Error - scomm delim not set properly")
		}
	} else {
		t.Errorf("scomm delim not set")
	}
	if _, exists := delimList["string"]; exists {
		if delimList["string"][0] != "\"" || delimList["string"][1] != "\".*\"" {
			t.Errorf("Error - string delim not set properly")
		}
	} else {
		t.Errorf("string delim not set")		
	}
}

// TestSetupTokens tests the functionality of setupTokens.
func TestSetupTokens(t *testing.T) {
	var tokens string

	initGVars()
	if runtime.GOOS == "windows" {
		tokens = "@ PTR_DEREF\r\ncontinue CONTINUE\r\n<= LESS_EQU\r\n>= GREATER_EQU\r\n== EQU_EQU"
	} else {
		tokens = "@ PTR_DEREF\ncontinue CONTINUE\n<= LESS_EQU\n>= GREATER_EQU\n== EQU_EQU"
	}
	setupTokens(tokens)
	if _, exists := tokenType["@"]; exists {
		if tokenType["@"] != "PTR_DEREF" {
			t.Errorf("Error - variable \"@\" token not set")
		}
	} else {
		t.Errorf("@ token not set")
	}

}








