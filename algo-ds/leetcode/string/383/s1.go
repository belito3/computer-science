package main

import (
    "fmt"
)

func main() {
    input := []string{"aa", "aab", "", "", "a", "b", "aa", "ab", "a", "", "a", "ab", "aab", "baa"}
    for i := 0; i < len(input); i += 2 {
        fmt.Printf("input = %s %s - rs = %v\n", input[i], input[i+1], canConstruct(input[i], input[i+1]))
    }
}

func canConstruct(ransomNote string, magazine string) bool {
    // s2: Hash table
    // Time: O(m+n)
    // Space: O(1)

    // init mapping with 0 values
    m := make([]int, 26)

    for i := 0; i < len(magazine); i++ {
        m[magazine[i] - 'a']++
    }

    for j := 0; j < len(ransomNote); j++ {
        m[ransomNote[j] - 'a']--
        if m[ransomNote[j] - 'a'] < 0 {
            return false
        }
    }
    return true
}

func canConstruct1(ransomNote string, magazine string) bool {
    // S1: brute force: interative
    // Time: O(n*m)
    // Space: O(m)
    if len(ransomNote) > len(magazine) {
        return false
    }

    r := []byte(magazine)

    for i := 0; i < len(ransomNote); i++ {
        valid := false
        for j := 0; j < len(r); j++ {
            if ransomNote[i] == r[j] {
                valid = true
                // remove element j from r
                r = append(r[:j], r[j+1:]...)
                break
            }
        }
        if !valid {
            return false
        }
    }
    return true
}
