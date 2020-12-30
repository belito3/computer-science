package main

import "fmt"

func main() {
    s := "()"
    s = "()[]{}"
    //s = "(]"
    //s = "([)]"
    //s = "{[]}"
    s = "["
    //s = "]"
    fmt.Println(isValid(s))
}

func isValid(s string) bool {

}

func isValid1(s string) bool {
    // Time: O(n)
    // Space: O(n) in the worst case, we will end up push all brackets onto the stack eg "(((((("
    if len(s) == 0 {
        return false
    }
    stack := []byte{}
    mapping := map[byte]byte{
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for i := 0; i < len(s); i++ {
        if s[i] == '(' || s[i] == '{' || s[i] == '[' {
            // push to stack
            stack = append(stack, s[i])
        } else {
            // pop to stack
            if len(stack) == 0 || stack[len(stack) - 1] != mapping[s[i]]{
                return false
            }
            stack = stack[0 : len(stack) - 1]
        }
    }
    return len(stack) == 0
}
