package main

import "fmt"

func main() {
	words := []string{}

	fmt.Println(maxProduct(words))
}

func maxProduct(words []string) int {
	if len(words) == 0 {
		return 0
	}
	var values []int

	// Get value represent of words
	for i := 0; i < len(words); i++ {
		tmp := 0
		for j := 0; j < len(words[i]); j++ {
			tmp |= 1 << (words[i][j] - 'a')
		}
		values = append(values, tmp)
	}

	maxWords := 0
	for i := 0; i < len(words)-1; i++ {
		for j := i + 1; j < len(words); j++ {
			if (values[i]&values[j] == 0) && (len(words[i])*len(words[j]) > maxWords) {
				maxWords = len(words[i]) * len(words[j])
			}
		}
	}

	return maxWords
}
