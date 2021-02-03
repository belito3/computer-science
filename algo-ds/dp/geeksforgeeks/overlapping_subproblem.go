//https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
package main

import "fmt"


func main() {
    for i := 1; i < 10; i++ {
       fmt.Println(sumThreeNum(i))
    }
}


func sumThreeNum(n int) int {
    // S2: Overlappping subproblem. Tabulation (bottom-up)
    // Time: O(n)
    // Space: O(n)
    lookup := make([]int, n+1)
    for i := 0; i <= n; i++ {
        lookup[i] = getNum(lookup, i-1) + getNum(lookup, i-3) + getNum(lookup, i-5)
    }
    return lookup[n]
}

func getNum(lookup []int, i int) int {
    if i < 0 {
        return 0
    }

    if i <= 1 {
        return 1
    }
    return lookup[i]
}

func sumThreeNum1(n int) int {
   // S1: Overlapping subproblem. Memoization (top-down)
   // Time: O(n)  
   // Space: O(n)
   lookup := make([]int, n+1)
   return sumThreeNumMem(n, lookup)
}

func sumThreeNumMem(n int, lookup []int) int {
   if n < 0 {
       return 0
   }

   if n == 0 {
       lookup[0] = 1
       return 1
   }

   if lookup[n] > 0 {
       return lookup[n]
   }
   lookup[n] = sumThreeNumMem(n-1, lookup) + sumThreeNumMem(n-3, lookup) + sumThreeNumMem(n-5, lookup)
   return lookup[n]
}
