
package main

import(
	"fmt"
	"io/ioutil"
	"log"
	"strings"
	"os"
	"runtime"
)

var defaultVars 	map[string]string
var gSymbolTable	map[string]string
var newline 		string
var regexList		map[string]string
//var delimList		map[string][]string
var delimList		map[string]string
var tokenType 		map[string]string

// isASCII checkes that a rune is a valid ASCII character.
func isASCII(c rune) bool {
	return (int(c) >= int('a') && int(c) <= int('z')) || (int(c) >= int('A') && int(c) <= int('Z'))  
}

// handlASCIICode converts tokens delimited with '%' in the config file into their
// ASCII equivalents as \t \n aren't carried over as TABs and Newlines respectively
func handleASCIICode(value string) string {
	var checker		strings.Builder
	var toReturn	strings.Builder
//	var tmp			strings.Builder

	flag := false
	for _, c := range value {
		if c == '%' {
			flag = true
		} else if flag == true && isASCII(rune(c)) == true {
			checker.WriteString(string(c))
		} else {
			flag = false
			if _, exists := defaultVars[checker.String()]; exists {
				toReturn.WriteString(defaultVars[checker.String()])
			} else {
				fmt.Printf("Warning : default variable %s doesn't exist\n", checker.String())
				return ""
			}
			checker.Reset()
		}
	}
	if len(checker.String()) > 0 {
		toReturn.WriteString(defaultVars[checker.String()])
	}
	return toReturn.String()
}

// handleVariable handles replacing variables with their contained values
// 
func handleVariable(value string) string {
    var newVal		strings.Builder
    var toReturn	strings.Builder

    flag := false
    for _, c := range value {
        if c == '{' {
        	flag = true
        } else if c == '}' {
            flag = false
            toReturn.WriteString(gSymbolTable[newVal.String()])
            newVal.Reset()
        } else if flag == true {
            newVal.WriteString(string(c))
        } else {
            toReturn.WriteString(string(c))
        }
    }
    return toReturn.String()
}


func skip(segment string) bool {
	if len(segment) == 0 || strings.HasPrefix(segment, "#") == true {
		return true
    }
    return false
}

func readFile(filename string) string {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(content)
}

func setupTargetList(config string, target string) {
	var keyVal		[]string
//	var delimItems 	[]string

	segments := strings.Split(config, newline)
	for _, segment := range segments {
		if skip(segment) == true {
			continue 
		}
		keyVal = strings.Fields(segment)

		if len(keyVal[1]) > 0 && keyVal[1][0] == '%' {
			keyVal[1] = handleASCIICode(keyVal[1])
		}
		gSymbolTable[keyVal[0]] = handleVariable(keyVal[1])
		if target == "regex" {
			regexList[keyVal[0]] = gSymbolTable[keyVal[0]]
		} else if target == "delim" {
			delimList[keyVal[0]] = handleVariable(keyVal[1])
			/*
			delimItems = append(delimItems, handleVariable(keyVal[1]))
			delimItems = append(delimItems, handleVariable(keyVal[2]))
			delimList[keyVal[0]] = delimItems
			delimItems = []string{}*/
		}
	}
}

func setupTokens(config string) {
	var keyVal []string

	segments := strings.Split(config, newline)
	for _, segment := range segments {
		if skip(segment) == true {
			continue 
		}
		keyVal = strings.Fields(segment)
		if len(keyVal[0]) > 1 && keyVal[0][1] == '%' {
			keyVal[0] = handleASCIICode(keyVal[0])
		}
		tokenType[handleVariable(keyVal[0])] = keyVal[1]
	}
}

func unpackConfig(config string) {

	configs := strings.Split(config, "%%")
	setupTargetList(configs[0], "regex")
	setupTargetList(configs[1], "delim")
	setupTokens(configs[2])

	fmt.Println("regex list")
	for k, v := range regexList	{
		fmt.Printf("%s : %s\n", k, v)
	}
	fmt.Println("==============")
	for k, v := range gSymbolTable {
		fmt.Printf("%s : %s\n", k, v)
	}
	fmt.Println("==============")
	for k, v := range delimList {
		fmt.Printf("%s : %s\n", k, v)
	}
	fmt.Println("===============")
	for k, v := range tokenType {
		fmt.Printf("%s : %s\n", k, v)
	}
}


func initConfig() string {
	var thisConfig []string

	content, err := ioutil.ReadFile("config")
	if err != nil {
		fmt.Println("Error : missing config file")
		os.Exit(2)
	}
	options := strings.Split(string(content), newline)
	for _, option := range options {
		thisConfig = strings.Split(option, ":")
		if thisConfig[0] == "spec" {
			return thisConfig[1] // code to be configured should extra config options become a thing.
		}	
	}
	fmt.Println("config not parsed properly")
	os.Exit(3)
	return ""
}
	
func initGVars() {
	defaultVars = make(map[string]string)
	tokenType = make(map[string]string)
	gSymbolTable = make(map[string]string)
//	delimList = make(map[string][]string)
	regexList = make(map[string]string)
	delimList = make(map[string]string)

	defaultVars["NEWLINE"] = "\n"
	defaultVars["TAB"] = "\t"	
	defaultVars["PC"] = "%"

	if runtime.GOOS == "windows" {
		newline = "\r\n"
	} else {
		newline = "\n"
	}
}

func main() {
	initGVars()

	configFile := initConfig()

	config := readFile(configFile)
	fmt.Println(config)
	unpackConfig(config)
	scan(os.Args[1])
}












