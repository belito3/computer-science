package main

import (
	"fmt"
)

func main() {
	s := "III"
	s = "IV"
	s = "IX"
	s = "LVIII"
	s = "MCMXCIV"
	s = "I"
	strs := []string{"I", "V", "X", "L", "C", "D", "M", "XVI", "IX", "LVIII", "MCMXCIV"}
	fmt.Println(romanToInt(s))
	for i := 0; i < len(strs); i++ {
		fmt.Println(strs[i], romanToInt(strs[i]))
	}

}


func romanToInt(s string) int {
	sum := 0
	prev := 0
	for i := 0; i < len(s); i++ {
		num := charToNum(s[i])
		if prev < num {
			sum += num - 2 * prev
		} else {
			sum += num
		}
		prev = num
	}
	return sum
}
func charToNum(c byte) int {
	switch c {
	case 'I': return 1
	case 'V': return 5
	case 'X': return 10
	case 'L': return 50
	case 'C': return 100
	case 'D': return 500
	case 'M': return 1000
	default: return 0
	}
	return 0
}

func romanToInt1(s string) int {
	// Time: O(n)
	// Space: O(1)
	num := 0
	if len(s) == 0 {
		return num
	}

	for i := len(s) - 1; i >= 0; i-- {
		if i == 0 {
			switch s[i] {
			case 'I': num += 1
			case 'V': num += 5
			case 'X': num += 10
			case 'L': num += 50
			case 'C': num += 100
			case 'D': num += 500
			case 'M': num += 1000
			default:
				num += 0
			}
			return num
		}

		j := i - 1
		switch s[i] {
		case 'V':
			if s[j] == 'I' {
				num += 4
				i -= 1
			} else {
				num += 5
			}
		case 'X':
			if s[j] == 'I' {
				num += 9
				i -= 1
			} else {
				num += 10
			}
		case 'L':
			if s[j] == 'X' {
				num += 40
				i -= 1
			} else {
				num += 50
			}
		case 'C':
			if s[j] == 'X' {
				num += 90
				i -= 1
			} else {
				num += 100
			}
		case 'D':
			if s[j] == 'C' {
				num += 400
				i -= 1
			} else {
				num += 500
			}
		case 'M':
			if s[j] == 'C' {
				num += 900
				i -= 1
			} else {
				num += 1000
			}
		case 'I':
			num += 1
		default:
			num += 0

		}
	}
	return num
}
