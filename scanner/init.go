package main

import (
	"fmt"
	"log"
	"os"
)

func writeContent(outfile string, outf string) {
	f, err := os.OpenFile(outfile, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0755)
	if err != nil {
		log.Fatal(err)
	}
	f.WriteString(outf)
	if err := f.Close(); err != nil {
		log.Fatal(err)
	}
}

func initSpecFile(outfile string) {
	outf := `
# Classifier

alphabet		[_a-zA-Z]
digit			[0-9]
number			{digit}+
newline			%NEWLINE
word			{alphabet}({alphabet}|{digit})*
symbols			[-+/\*&!\|=><:^;,]
lbrace 			%LBRC
rbrace 			%RBRC
equ             ([+-/=*!&\|]|((>)?>)|((<)?<))?=
left            (<)?<
right           (>)?>
brackets        [\[\]\(\)]
comment 		//.*{newline}
mcomment		/\*.*\*/
float           [0-9]+((\.[0-9]*)|e((\+|-)?[0-9]+))
hex             0[xX][a-fA-Z0-9]+
string			".*"
char 			'[(\')(\t)(\n)]|(.*)'	

%%

# Delim tokens come here

%%

# And token types here
`
	// check for file's existence
	if _, err := os.Stat(outfile); err == nil {
		var response string
		fmt.Printf("Warning: File exists, overwrite? [y/N]:")
		for {
			_, err := fmt.Scanln(&response)

			if err != nil || (response != "y" && response != "Y" && response != "n" && response != "N") {
				fmt.Printf("Please press either Y or N: ")
				continue
			} else if response == "n" || response == "N" {
				fmt.Println("Aborting")
				os.Exit(1)
			}

			break
		}
	}
	writeContent(outfile, outf)
	fmt.Println("New specfile initialized : ", outfile)
}
