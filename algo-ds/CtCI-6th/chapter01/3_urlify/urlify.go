package main

import "fmt"

func main() {
	// Input: "Mr John Smith    ", 13
	// Ouput: "Mr%20John%20Smith"	
	s := []string{"Mr John Smith    "} 
	l := []int{13}
	for i := range s {
		fmt.Printf("input = %s, ouput = %s\n", s[i], replaceSpace(s[i], l[i]))
	}
}


func replaceSpace(str string, length int) string {
	
}

func replaceSpace1(str string, length int) string {
	// Use other string 
	// Time: O(length)
	// Space: O(lengh + 2*num_space)
	var out string

	for i := 0; i < length; i++ {
		if str[i] == ' ' {
			out += "%20"	
		} else {
			out += string(str[i])
		} 
	}
	return out
}
