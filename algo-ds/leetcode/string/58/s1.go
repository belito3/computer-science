package main

import (
	"fmt"
)

func main() {
	arr := []string{"hello world", " ", "a ", "a  ", "a"}
	for _, str := range(arr) {
		fmt.Printf("str = %v, arr = %v\n", str, lengthOfLastWord(str))
	}
	fmt.Println(lengthOfLastWord("a "))
}

func lengthOfLastWord(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}

	l := 0
	for i := n - 1; i >= 0; i-- {
		if s[i] == ' ' {
			if l > 0 {
				return l
			}
		} else {
			l += 1
		}
	}
	return l
}
