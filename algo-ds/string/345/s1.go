package main

import (
    "fmt"
)

func main() {
    s := []string{"hello",  "leetcode", "hEllo", "", "hEello"}
    for _, s := range(s) {
        fmt.Printf("str = %s rs = %s\n", s, reverseVowels(s))
    }
}
func reverseVowels(s string) string {
    // Time: O(n)
    // Space: O(n)
    r := []rune(s)
    h, t := 0, len(s) - 1
    for h < t {
        // find  head
        if !isVowel(s[h]) {
            h++
            continue
        }
        // find tail 
        if !isVowel(s[t]) {
            t--
            continue
        }
        // swap r[h] and r[i]
        r[h] = r[h] + r[t]
        r[t] = r[h] - r[t]
        r[h] = r[h] - r[t]
        h++
        t--
    }
    return string(r)
}

func isVowel(c byte) bool {
    if c < 'a' {
        c += 32 // or + 'space'
    }
    return c == 'u' || c == 'e' || c == 'o' || c == 'a' || c == 'i'
}
