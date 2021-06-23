package main

import "fmt"


func main(){
    for i := 1; i <= 25; i++ {
        fmt.Printf("%v : %v\n", i, isPerfectSquare(i))
    }
}

func isPerfectSquare(num int) bool {
    h := 0
    t := num

    for t >= h {
        m := (h + t) / 2

        if m*m == num {
            return true
        } else if m*m < num {
            h = m + 1
        } else {
            t = m - 1
        }
    } 
    return false
}
