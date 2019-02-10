//  Source https://golang.org/doc/articles/wiki/
package main

import (
    "fmt"
    "log"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Print("Olleh")
    fmt.Fprintf(w, "Hi there, I hate %s!", r.URL.Path[1:])
}

func main() {
    fmt.Print("Hello")
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}