// Source https://golang.org/doc/articles/wiki/
package main

import (
    "fmt"
    "log"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Printf("\n===========\nNew Request\n===========\n")
    fmt.Printf("- Method: %s\n", r.Method)
    fmt.Printf("- URL: %s\n", r.URL)
    fmt.Printf("- Header %s\n", r.Header)
    fmt.Printf("- Body: %s\n", r.Body)
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}