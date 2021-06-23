// https://www.spoj.com/problems/ACODE/
package main

import "fmt"

func main() {
    input := []string{"12", "226", "2206", "3306", "0", "01", "1201234", "120123", "1111111111", "123123"}
    for _, i := range input {
        fmt.Printf("i = %v, rs = %v\n", i, numDecodings(i))
    }
}

func numDecodings(s string) int {
    // Solution: DP
    // Time: 0(n)
    // Space: 0(1)
    /*
        Call f[i] is the number of possible decoding for input string with length i (i = 1,2,3..n)
        We compute number s[i-1]s[i]: sum = s[i-1]* 10 + i 
        if 10 <= sum <= 26:
            + s[i] == '0' (ex: s = xx10, xx20, ...) --> f[i] = f[i-2]
            + s[i] != '0' (ex: s = xx12, xx21, ...) --> f[i] = f[i-1] + f[i-2] (formula from problem 70. Climbing Stairs)
        else if sum > 26 or sum < 10:
            + s[i] == '0' (ex: s = xx00, xx40..) --> invalid character return 0
            + s[i] != '0' (ex: s = xx33, xx09..) -> f[i] = f[i-1]

         Because we just find f[i], we can use two vars prev, curr store f[i-2] and f[i-1] respectively
    */
    if s[0] == '0' { // invalid character: 0, 06, 0006
        return 0
    }
    l := len(s)
    prev := 1
    curr := 1
    for i := 1; i < l; i++ {
        sum := (s[i-1] - '0') * 10 + (s[i] - '0')
        if sum >= 10 && sum <= 26 {
            if s[i] == '0' {
                temp := curr // temp = f[i-1]
                curr = prev  // f[i] = f[i-2]
                prev = temp  // move prev from f[i-2] to f[i-1] 
            } else { // f[i] = f[i-1] + f[i-2]
                temp := curr + prev
                prev = curr
                curr = temp
            }
        } else {
            if s[i] == '0' {
                return 0
            } else { // f[i] = f[i-1]
                curr = curr
                prev = curr
            }
        }
    }
    return curr
}


