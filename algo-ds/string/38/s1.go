package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	// Native compression algorithm

	for i := 1; i < 6; i += 1 {
		fmt.Printf("i = %v: %v\n", i, countAndSay(i))
	}
	fmt.Println(countAndSay(2))
}

// Go strings are immutable, so whenever we attempt to update a string within a loop we are actually creating a new string on every iteration.
// For this problem we only require to append/write to the string while we are working with it, so there's a helper from the Go standard library that comes handy: strings.Builder.
// You can take a look at its code at https://golang.org/src/strings/builder.go
func countAndSay(n int) string {
	// Sliding window 
	// Time: O(n^2) = 1 + 2 + ... +n
	// Space: O(n^2)
	if n == 1 {
		return "1"
	}


	str1 := countAndSay(n - 1)
	l := len(str1)
	var str2 strings.Builder
	cnt := 1

	for i := 1; i < l; i++ {
		if str1[i] == str1[i-1] {
			cnt += 1
		} else {
			str2.WriteString(strconv.Itoa(cnt))
			str2.WriteByte(str1[i-1])
			cnt = 1
		}
	}
	str2.WriteString(strconv.Itoa(cnt)) 
	str2.WriteByte(str1[l-1])


	return str2.String()
}
