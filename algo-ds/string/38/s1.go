package main

import (
	"fmt"
	"strconv"
)

func main() {
	for i := 1; i < 6; i += 1 {
		fmt.Printf("i = %v: %v\n", i, countAndSay(i))
	}
	fmt.Println(countAndSay(2))
}

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	str1 := countAndSay(n - 1)
	l := len(str1)
	str2 := ""
	cnt := 1 
	for i := 1; i < l; i++ {
		if str1[i] == str1[i-1] {
			cnt += 1
		} else {
			str2 += strconv.Itoa(cnt) + string(str1[i-1]) 
		}
	}
	str2 += strconv.Itoa(cnt) + string(str1[l-1])


	return str2
}
