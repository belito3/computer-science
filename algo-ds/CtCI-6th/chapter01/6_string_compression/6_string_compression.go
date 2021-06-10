package main

import (
	"strings"
	"fmt"
)

func main() {
	input := []string{"aabvccdddd"}
	for _, in := range(input) {
		fmt.Printf("in = %s  rs = %s \n", in, strCompression(in)) 
	}

}

func strCompression(str string) string {
	// Time: O(n)
	// Space: worst case O(n)
	if len(str) == 0 {
		return str
	}
	
	cnt := 0
	var rs strings.Builder
	
	for i := 0; i < len(str); i++ {
		cnt++
		if i == len(str) - 1 || str[i] != str[i+1] {
			rs.WriteByte(str[i])
			rs.WriteString(fmt.Sprint(cnt))
			cnt = 0
		}	
	}		
	
	
	if rs.Len() < len(str) {
		return str
	}
	return rs.String()
}
