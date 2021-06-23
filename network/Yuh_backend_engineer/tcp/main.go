package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strings"
)

/*
	1. Run server: go run server.go
	2. Run client:
		telnet 127.0.0.1 8081
		
*/
// https://www.youtube.com/watch?v=DC5SLPzwiro&list=PLw-L1SGSvTEcBzw9FsP5UFWqrErzS2jE2&index=3
func main() {
	ln, err  := net.Listen("tcp", "127.0.0.1:8081")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Accept connection to port")
	for {
		conn, err := ln.Accept()
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Calling handleConnection")
		go handleConnection(conn)
	}
}


func handleConnection(conn net.Conn) {
	defer conn.Close()
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		message := scanner.Text()
		fmt.Println("Message Received:", message)
		newMessage := strings.ToUpper(message)
		conn.Write([]byte(newMessage + "\n"))		
	}
	
	if err := scanner.Err(); err != nil {
		fmt.Println("error:", err)
	}
}

