package stack

import (
	"fmt"
)

// AcceptingState holds the last valid position and token state of the last accepted
// token
type AcceptingState struct {
	Pos		int
	State 	string
}

// Stack adds functionality for a stack of AcceptingState values
type Stack struct {
	Item []*AcceptingState
	Height int
}

// InitSstack initializes the stack
func InitStack() *Stack {
	return &Stack{
		Height: 0,
	}
}

// Push pushes the current accepting state to the top of the stack
func (s *Stack)Push(pos int, currSstate string) {
	item := &AcceptingState{
		Pos: pos,
		State: currSstate,
	}
	s.Item = append(s.Item, item)
	s.Height++
}

// Pop pops the last accepting states off of the stack.
func (s *Stack)Pop() *AcceptingState {
	if s.Height == 0 {
		return nil
	}
	s.Height--
	toReturn := s.Item[s.Height]
	s.Item = s.Item[:s.Height]
	return toReturn
}

// Clear clears the stack
func (s *Stack)Clear() {
	s.Item = []*AcceptingState{}
	s.Height = 0
}

// Print is a helper function for printing out the state of the stack. Used for debugging.
func (s *Stack)Print() {
	for _, c := range s.Item {
		fmt.Printf("%d -> %s\n", c.Pos, c.State)
	}
}