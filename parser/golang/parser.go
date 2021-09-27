
package main

import (
	"fmt"
	"strings"
)

type rule struct {
	name 	string
	ntype 	string
	next 	*rule

	recipe 	[]string
	follow 	[]string
}

var allRules map[string][]rules

func newRule(name string, recipe []string, follow []string) *rule {
	return &rule{
		name: name,
		recipe: recipe,
		follow: follow,
	}
}

func generateRules(grammar string) {

	rules := strings.Split(grammar, "\n")

}

func main() {

}





