package main

import "fmt"

func main() {
	s := [][]byte{{'h', 'e', 'l', 'l', 'o'},
		     {'H', 'a', 'n', 'n', 'a', 'h'},
		     {}, {'a'}, {'a', 'b'}}
	for _, str := range(s) {
		fmt.Printf("before: %c\n", str)
		reverseString(str)
		fmt.Printf("after: %c\n", str)
	}

}

func reverseString(s []byte) {
	l := len(s)
	if l == 0 {
		return
	}

	for i := 0; i < l/2; i++ {
		s[i] = s[i] + s[l-i-1]
		s[l-i-1] = s[i] - s[l-i-1]
		s[i] = s[i] - s[l-i-1]
	}
}

func reverseString1(s []byte) {
	l := len(s)
	if l == 0 {
		return
	}
	n := l / 2
	var tmp byte
	for i := 0; i < n; i++ {
		tmp = s[i]
		s[i] = s[l-i-1]
		s[l-i-1] = tmp
	}
}
