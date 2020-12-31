package main

import "fmt"

func main() {
    test := []string{"hello", "ll", "aaaaaa", "bba", "", "a", "a", "a", ""}

    for i := 0; i < len(test); i += 2 {
        fmt.Printf("s1=%v  s2=%v  i=%v\n", test[i], test[i+1], strStr(test[i], test[i+1]))
    }
}

func strStr(haystack string, needle string) int {
    if needle == "" {
        return 0
    }

    for i, j := 0, 0; j < len(haystack); {
        //fmt.Println("j = ", j, string(haystack[j]))
        //fmt.Println("i = ", i, string(needle[i])) 
        if needle[i] == haystack[j] {
            if i == len(needle) - 1 {
                return j - i
            }
            i += 1
        } else {
            i = 0
        }
        j += 1
    }

    return -1
}
