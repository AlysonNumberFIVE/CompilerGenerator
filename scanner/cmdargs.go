package main

import (
	"fmt"
	"os"
	"strings"
)

// arguments serves as a struct that organizes the different cmd args passed in
// when executed.
type arguments struct {
	specfile string // specfile is a shortcut to using a specific spec. If this field is nil
	// the config file is used instead.
	interpreter bool     // interperter will fire up the shell (not implemented)
	files       []string // files are a list of the files passed into the scanner.
	init        string   // init creates a blank spec file with Classifiers set.
}

// initArgs initializes an empty arguments structure.
func initArgs() *arguments {
	return &arguments{
		interpreter: false,
	}
}

func help() {
	fmt.Println("Scanner : created by AlysonOrSomething")
	fmt.Println("Usage : ./scan [optional Flags] [program files]")
	fmt.Println("Flags :")
	fmt.Println("\t-s | --spec [specfile] : specify a specfile to use from the command line")
	fmt.Println("\t-i | --init [filename] : initialize a specfile template to use (auto classifiers already set)")
	fmt.Println("\t-p | --prompt : Initializes an interactive shell, allowing you to test \n\ttokens from a spec you're testing (coming soon)")
	fmt.Println("\t-h | --help : print this screen.")
	os.Exit(1)
}

// verifyArgs sanity checks the flags passed in by the command line,
func verifyArgs(argv *arguments) *arguments {
	if len(argv.init) > 0 {
		initSpecFile(argv.init)
		os.Exit(1)
	}

	if argv.interpreter {
		fmt.Println("Prompt not implemented")
		if len(argv.files) > 0 {
			fmt.Println("Note: Cannot run file interactively")
		}
		os.Exit(1)
	}

	if len(argv.files) == 0 {
		fmt.Println("No files inputted")
		os.Exit(1)
	}
	return argv
}

// cmdArgs separates source files from command line arguments.
func cmdArgs(args []string) *arguments {
	argv := initArgs()

	if len(args) < 2 {
		fmt.Println("Error : No arguments provided")
		help()
	}

	i := 1
	for i < len(args) {
		if strings.HasPrefix(args[i], "-") {

			// TODO: Convert this to a swtich statement.
			if (args[i] == "--spec" || args[i] == "-s") && i+1 < len(args) {
				argv.specfile = args[i+1]
				i += 1
			} else if args[i] == "-h" || args[i] == "--help" {
				help()
			} else if (args[i] == "--init" || args[i] == "-i") && i+1 < len(args) {
				argv.init = args[i+1]
				i += 1
				break
			} else if args[i] == "--prompt" || args[i] == "-p" {
				argv.interpreter = true
				break
			} else {
				fmt.Println("Error: invalid flag", args[i])
				os.Exit(1)
			}
		} else {
			argv.files = append(argv.files, args[i])
		}
		i++
	}
	return verifyArgs(argv)
}
