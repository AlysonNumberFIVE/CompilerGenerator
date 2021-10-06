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
}

// initArgs initializes an empty arguments structure.
func initArgs() *arguments {
	return &arguments{
		interpreter: false,
	}
}

func verifyArgs(argv *arguments) *arguments {
	if argv.interpreter == true {
		fmt.Println("Prompt not implemented")
		if len(argv.files) > 0 {
			fmt.Println("Note: Cannot run file interactively")
		}
		os.Exit(1)
	}

	if len(argv.specfile) == 0 {
		argv.specfile = "config"
	}

	if len(argv.files) == 0 {
		fmt.Println("No files inputted")
		os.Exit(1)
	}

	fmt.Println("Arguments verified:")
	fmt.Println("files ", argv.files)
	fmt.Println("spec ", argv.specfile)
	return argv
}

// cmdArgs separates source files from command line arguments.
func cmdArgs(args []string) *arguments {
	argv := initArgs()

	if len(args) < 1 {
		fmt.Println("Error : No arguments provided")
		fmt.Println("Usage: ./scanner [args]")
		os.Exit(1)
	}

	i := 1
	for i < len(args) {
		if strings.HasPrefix(args[i], "-") {
			if (args[i] == "--spec" || args[i] == "-s") && i+1 < len(args) {
				argv.specfile = args[i+1]
				i += 1
			} else if args[i] == "--prompt" || args[i] == "-p" {
				argv.interpreter = true
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

func main() {
	argv := []string{"./scanner", "-s"}
	cmdArgs(argv)
}
