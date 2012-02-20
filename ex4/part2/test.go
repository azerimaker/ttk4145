package main

import "fmt"
import "server"
import "time"

var a = server();
    
func main(){

    go b(serv);
    go c(serv);
    
    for true{time.Sleep(100)}

}

func b(s serv){
    fmt.Println(s.get());
}

func c(s serv){
    s.set(s.get()+1);
}
