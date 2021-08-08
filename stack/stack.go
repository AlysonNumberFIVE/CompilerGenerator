package stack

import (
	"fmt"
)

type AcceptingState struct {
	Pos		int
	State 	string
}

type Stack struct {
	Item []*AcceptingState
	Height int
}

func InitStack() *Stack {
	return &Stack{
		Height: 0,
	}
}

func (s *Stack)Push(pos int, currSstate string) {
	item := &AcceptingState{
		Pos: pos,
		State: currSstate,
	}
	s.Item = append(s.Item, item)
	s.Height++
}

func (s *Stack)Pop() *AcceptingState {
	if s.Height == 0 {
		return nil
	}
	s.Height--
	toReturn := s.Item[s.Height]
	s.Item = s.Item[:s.Height]
	return toReturn
}

func (s *Stack)Clear() {
	s.Item = []*AcceptingState{}
	s.Height = 0
}

func (s *Stack)Print() {
	for _, c := range s.Item {
		fmt.Printf("%d -> %s\n", c.Pos, c.State)
	}
}