package main

import (
	"fmt"
	"strings"
)


func main() {
	// Input: "Mr John Smith    ", 13
	// Ouput: "Mr%20John%20Smith"	
	s := []string{"Mr John Smith    "} 
	l := []int{13}
	for i := range s {
		fmt.Printf("input = %s, ouput = %s\n", s[i], replaceSpace(s[i], l[i]))
	}
}


func replaceSpace(str string, trueLength int) string {
	arr := strings.Split(str, "")	
	index := len(str) - 1

	for i := trueLength - 1; i >= 0; i-- {
		if arr[i] == " " {
			arr[index] = "0"	
			arr[index-1] = "2"
			arr[index-2] = "%"
			index -= 3
		} else {
			arr[index] = arr[i]
			index--	
		}
	}
	return strings.Join(arr, "")
}

func replaceSpace2(str string, trueLength int) string {
	// Edit string starting from the end
	// Author: !!!bao baby !!!
	right := len(str)
	arr := strings.Split(str, "")
	for i := trueLength - 1; i >= 0; i-- {
		if arr[i] == " " {
			fmt.Println("i ", i)
			// move str[i+1:trueLength] to str[i+1+right-trueLength:right]
			start := i+1+right-trueLength
			fmt.Println("before ", arr)
			moveList(arr, start, right, trueLength-1)
			fmt.Println("after  ", arr)
			// arr[start:right] = arr[i+1:trueLength] 	
			arr[start-3] = "%"
			arr[start-2] = "2"
			arr[start-1] = "0"
			right = start - 3
			trueLength = i 
		}		
	} 	
	return strings.Join(arr, "")
}

func moveList(arr []string, start, end, index int) {
	fmt.Println(start, end, index)
	for i := end-1; i >= start; i-- {
		//fmt.Println("i: ", i)
		arr[i] = arr[index]	
		index -= 1
	}	
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
