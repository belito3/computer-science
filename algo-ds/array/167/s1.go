package main

import "fmt"

func main() {
	s := []int{2, 2, 3, 4, 5, 6, 7}
	target := 10
	fmt.Println(twoSum(s, target))
}

func twoSum(numbers []int, target int) []int {
	// S2: Two points
	// time: O(n)
	// space: O(1)

	head, tail := 0, len(numbers)-1

	for numbers[head]+numbers[tail] != target {
		if numbers[head]+numbers[tail] < target {
			head++
		} else {
			tail--
		}
	}

	head++
	tail++
	return []int{head, tail}
}

func twoSum1(numbers []int, target int) []int {
	// S1: Brute force
	// time: O(n^2)
	// space: O(1)
	idxs := make([]int, 2)
	for i := 0; i < len(numbers)-1; i++ {
		if numbers[i] >= target/2+1 {
			break
		}
		idxs[0] = i + 1
		// find idx2
		for j := i + 1; j < len(numbers); j++ {
			if numbers[j] == target-numbers[i] {
				idxs[1] = j + 1
				return idxs
			}
		}
	}
	return idxs
}
