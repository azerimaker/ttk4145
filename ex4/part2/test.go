package main

import (
	"runtime"
	"time"
)
/* Informal proof: A send on a channel happens before the corresponding receive
   Unless it is an unbuffered channel, where a receive happens before the send
   completes. So since we are using a buffered channel, once enough data to fill
   the buffer has been put on the channel, no more send operations are permitted
   before there is at least one receive, freeing up space. 
   See http://golang.org/doc/go_mem.html 
   
   In C, we would have used a mutex; set a flag that had to be clear before the
   process could continue to run. And clear the flag of the processes in the right order. 
*/
	
func server(serverInputChannel, serverOutputChannel chan int) {
	outputValue := 0
	serverOutputChannel <- outputValue
	for {
		time.Sleep(1*1e9)
		inputValue := <- serverInputChannel 
		outputValue += inputValue
		serverOutputChannel <- outputValue
		runtime.Gosched()
	} 
}
	
func main() {
	serverInputChannel := make(chan int, 1)	// buffered channel
	serverOutputChannel := make(chan int)		
	go server(serverInputChannel, serverOutputChannel)
	go client1(serverInputChannel)
	go client2(serverInputChannel)
	go client3(serverInputChannel)
	go read(serverOutputChannel)
	
	for {
		runtime.Gosched() // run forever, but yield CPU to other threads
	}
	
}

func client1(serverInputChannel chan int) {
	for  j:=0;j<1000;j++{
		myVar := 2
		serverInputChannel <-myVar
	}
}

func client2(serverInputChannel chan int) {
	for  j:=0;j<1000;j++{
		myVar := -1
		serverInputChannel <- myVar
	}
}	

func client3(serverInputChannel chan int) {
	for  j:=0;j<1000;j++{
		myVar := 3
		serverInputChannel <- myVar
	}
}

func read(serverOutputChannel chan int) {
	for {
		out := <- serverOutputChannel
		print(out," ")
		time.Sleep(1*1e9)
	}
}
