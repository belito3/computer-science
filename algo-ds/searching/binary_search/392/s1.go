package main

import "fmt"

func main(){
    s := "aaaaaa"
    t := "bbaaaa"

    fmt.Printf("s = %v, t = %v : %v", s, t, isSubsequence(s, t))
}

func isSubsequence(s string, t string) bool {
    cnt := 0
    j := 0

    for i := 0; i < len(s); i++ {
        for k := j; k < len(t); k++ {
            if s[i] == t[k] {
                fmt.Println(k)
                cnt++
                j = k + 1
                break
            }
        }
    }

    return cnt == len(s) 
}
