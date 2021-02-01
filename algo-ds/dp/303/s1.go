package main

import "fmt"

func main() {
    input := [][]int{{-2, 0, 3, -5, 2, -1}}
    
    for _, in := range(input) {
        m := []int{0, 0, len(in)-1, len(in)-1, 0, 2, 2, 5, 0, 5}
        arr := Constructor(in)
        fmt.Printf("input = %v\n", in)
        for i := 0; i < len(m); i += 2 {
            fmt.Printf("i = %v j = %v sum = %v\n", m[i], m[i+1], arr.SumRange(m[i], m[i+1]))
        }
    }
}


type NumArray struct {
   sum  []int
}

func Constructor2(nums []int) NumArray {
    // Time: O()
    // Space: O(n)
    /* i <= j, 
        S0 = s(0,0) = 0
        S1 = s0 + num0 -> store num0
        s2 = s1 + num1 -> store num1, num0
        ...
        Sum(i) = Sum(0,i) = S0 + n0 + n1 + ... + ni-1 = Sum(i-1) + n[i-1]
        Sum(j) = Sum(0,j) = S0 + n0 + n1 + ..+ ni-1 + ni + .. + nj-1
        --> Sum[i,j] = ni + .. + nj = Sum(0, j+1) - Sum(0, i)
        saving O(n) space memory

    */
    sum := make([]int, len(nums)+1)
    for i := 0; i < len(nums); i++ {
       sum[i+1] = nums[i] + sum[i]
    }
    return NumArray{sum: sum}
}

func (this *NumArray) SumRange2(i int, j int) int {
    return this.sum[j+1] - this.sum[i]
}
