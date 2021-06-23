package main

import (
	"fmt"
	"net"
)

/*
	Test1: run server.go, client.go
	Test2: stateless: interrupt server, client continue run normaly
	
*/
func main() {
	p := make([]byte, 100)
	addr := net.UDPAddr{
		Port: 8081,
		IP: net.ParseIP("127.0.0.1"),
	}	
	ser, err := net.ListenUDP("udp", &addr)
	if err != nil {
		fmt.Printf("Some error %v\n", err)
	}
	for {
		_, remoteaddr, err := ser.ReadFromUDP(p)
		fmt.Printf("%v %s\n", remoteaddr, p)	
		if err != nil {
			fmt.Printf("Some error %v", err)
			continue
		}
	}
}



