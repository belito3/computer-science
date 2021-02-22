package main

import "fmt"

func main() {
    word1 := "s"
    word2 := "saturday"

    fmt.Printf("word1 = %s word2 = %s rs = %d\n", word1, word2, minDistance(word1, word2))
}

func minDistance(word1 string, word2 string) int {
    // Overlapping substructure - memoization (top-down)
    m := len(word1)
    n := len(word2)

    // d[i][j] is minimum edit distance of word1[:i+1] and word2[:j+1]  
    d := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        d[i] = make([]int, n+1)
    }

    for i := 0; i <= m; i++ {
        for j := 0; j <= n; j++ {
            d[i][j] = -1
        }
    }

    return ed(word1, word2, m, n, d)
}

func ed(word1 string, word2 string, m int, n int, d [][]int) int {
    if m == 0 {
        d[m][n] = n
        return n
    }

    if n == 0 {
        d[m][n] = m
        return m
    }

    if word1[m-1] == word2[n-1] {
        if d[m][n] == -1 {
            d[m][n] = ed(word1, word2, m-1, n-1, d)
            return d[m][n]
        }
        return d[m][n]
    }


    if d[m][n-1] == -1 { // insert 
        d[m][n-1] = ed(word1, word2, m, n - 1, d)
    }

    if d[m-1][n-1] == -1 {
        d[m-1][n-1] = ed(word1, word2, m-1, n - 1, d)
    }

    if d[m-1][n] == -1 {
        d[m-1][n] = ed(word1, word2, m - 1, n, d)
    }

    d[m][n] = 1 + min(min(d[m][n-1], d[m-1][n-1]), d[m-1][n])
    return d[m][n]
}


func minDistance1(word1 string, word2 string) int {
    // S1: recursive
    // Time: in worst O(2^(m*n))
    m := len(word1)
    n := len(word2)

    return editDistance(word1, word2, m - 1, n - 1)
}

func editDistance(word1 string, word2 string, m int, n int) int {
    // if first word is empty, the only option is to insert all character of second word string to first
    if m == 0 {
        return n + 1
    }
    // if second word is empty, the only option is remove all character of first word
    if n == 0 {
        return m + 1
    }

    if word1[m] == word2[n] {
        return editDistance(word1, word2, m-1, n-1)
    }

    return 1 + min(min(editDistance(word1, word2, m, n-1), // insert to last word1
                    editDistance(word1, word2, m-1, n-1)), // replace last word1
                    editDistance(word1, word2, m-1, n)) // remove last word1
}

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}
