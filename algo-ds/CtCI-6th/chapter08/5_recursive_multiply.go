package main

import "fmt"


func main() {
    a := []int{3, 1, 0, 10}
    b := []int{7, 0, 4, 13}
    for i := 0; i < len(a); i++ {
        m := multiple(a[i], b[i])
        fmt.Printf("a = %v, b = %v, rs = %v \n", a[i], b[i], m) 
    }
    
}


func multiple(a, b int) int {
    // Time: Log2(n)
    // Space: Log2(n)
    shift := 0
    rs := 0
    bigger, smaller := a, b
    if a < b {
        bigger = b
        smaller = a
    } 

    if bigger == 1 {
        return smaller
    }
    if smaller == 0 {
        return bigger
    }

    return cal(bigger, smaller, shift, rs) 
}

func cal(a, b, shift, rs int) int {
    // a bigger, b smaller
    if b == 0 {
        return rs
    } 

    if b & 1 == 1 {
        rs += a << shift
    }

    b = b >> 1
    shift = shift + 1
    rs = cal(a, b, shift, rs)
    return rs
}
