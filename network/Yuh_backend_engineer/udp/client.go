package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("udp", "127.0.0.1:8081")
	if err != nil {
		fmt.Printf("Some error %v", err)
	}
	for {
		fmt.Fprintf(conn, "Hello server")
	}
}
