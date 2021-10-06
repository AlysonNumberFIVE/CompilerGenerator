
package main

import(
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
	"os"
	"runtime"

	stack "github.com/AlysonBee/CompilerGenerator/stack"
)

var defaultVars 	map[string]string
var gSymbolTable	map[string]string
var newline 		string
var regexList		map[string]string
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
				return value
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

// skip skips over empty commented out lines.
func skip(segment string) bool {
	if len(segment) == 0 || strings.HasPrefix(segment, "#") == true {
		return true
    }
    return false
}

// readFile reads the contents of the source file.
func readFile(filename string) string {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(content)
}

// setupTargetList sets up the delim and regex tables from the spec file
func setupTargetList(config string, target string) {
	var keyVal		[]string

	segments := strings.Split(config, newline)
	for _, segment := range segments {
		if skip(segment) == true {
			continue 
		}
		keyVal = strings.Fields(segment)
		
		keyVal[1] = handleVariable(keyVal[1])
		if len(keyVal[1]) > 0 && keyVal[1][0] == '%' {
			keyVal[1] = handleASCIICode(keyVal[1])
		}
		gSymbolTable[keyVal[0]] = keyVal[1]
		if target == "regex" {
			regexList[keyVal[0]] = gSymbolTable[keyVal[0]]
		} else if target == "delim" {
			delimList[keyVal[0]] = keyVal[1]
		}
	}
}

// setupTokens sets up the token type tables from the spec files
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

// unpackSpec unpacks the spec files into the three tables
func unpackSpec(config string) {
	configs := strings.Split(config, "%%")
	setupTargetList(configs[0], "regex")
	setupTargetList(configs[1], "delim")
	setupTokens(configs[2])
}

// cmdFlags sets up the config from the command line.
func cmdFlags() string {
	configFile := flag.String("config", "specfiles\\c.spec", "The config file that points to a spec to use")

	flag.Parse()
	fmt.Println("config is ", *configFile)
	return *configFile
}

// initConfig
func initConfig() string {
	var thisConfig []string

	if len(os.Args) > 1 && strings.HasPrefix(os.Args[1], "-") {
		return cmdFlags()
	}

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

// initGVars initializes all global variables
func initGVars() {
	defaultVars = make(map[string]string)
	tokenType = make(map[string]string)
	gSymbolTable = make(map[string]string)
	regexList = make(map[string]string)
	delimList = make(map[string]string)

	defaultVars["NEWLINE"] = "\n"
	defaultVars["TAB"] = "\t"	
	defaultVars["PC"] = "%"
	defaultVars["LBRC"] = "{"
	defaultVars["RBRC"] = "}"

	if runtime.GOOS == "windows" {
		newline = "\r\n"
	} else {
		newline = "\n"
	}
}

func files(fileList []string) []string {
	var allFiles []string

	i := 1
	for i < len(fileList) {
		allFiles = append(allFiles, fileList[i])
		i++
	}

	return allFiles
}

func main() {

	if len(os.Args) == 1 {
		fmt.Println("Error: No input source files provided")
		fmt.Println("Usage: compiler [source file(s)]")
		fmt.Println("Note: multi-file support coming soon")
		os.Exit(1)
	}

	initGVars()

	configFile := initConfig()
	fmt.Println("configFile ", configFile)
	tokens = initTokenList()
	stck = stack.InitStack()

	config := readFile(configFile)
	unpackSpec(config)

	allFiles := files(os.Args)

	for _, file := range allFiles {
		scan(file)
	}
	tokens.listTokens()
}

