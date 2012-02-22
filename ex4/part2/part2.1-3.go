package main

import (
	"fmt"
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
	
func server(i, o chan int) {
	myVar := 0
	o <- myVar
	for {
//		time.Sleep(1*1e7)
		fmt.Print(".")
		input := <- i 
		myVar += input
		o <- myVar
		fmt.Println("This is servers output", myVar, "it got this as input", input)
		runtime.Gosched()
	} 
//	fmt.Println("This is servers output", myVar)
}
	
func main() {
	i := make(chan int, 1)
	o := make(chan int, 1)
	go server(i, o)
	go client1(i, o)
	go client2(i, o)
	go client3(i, o)
	for {
		runtime.Gosched()
	}
	time.Sleep(1*1e2)
	
}

func client1(i, o chan int) {
	for  j:=0;j<1000;j++{
//		time.Sleep(1*1e7)
		fmt.Print("|")
		serverVar := <- o
		serverVar++
		myVar := 2
		i <-myVar
//		runtime.Gosched()
	}
}

func client2(i, o chan int) {
	for  j:=0;j<1000;j++{
//		time.Sleep(1*1e7)
		fmt.Print("|")
		serverVar := <- o
		serverVar++
		myVar := -1
		i <- myVar
//		runtime.Gosched()
	}
}	

func client3(i, o chan int) {
	for  j:=0;j<1000;j++{
//		time.Sleep(1*1e7)
		fmt.Print("|")
		serverVar := <- o
		myVar := 3
		serverVar++
		i <- myVar
//		runtime.Gosched()
	}
}
