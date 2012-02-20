package main

import "fmt"

var i = 0;


func main(){
    var a int = 0;
//    set(a);
//    fmt.Println(get());
}

func get() (int){       
    return i;
}

func set(new int){
    i = new;
    fmt.Println(i);
}
