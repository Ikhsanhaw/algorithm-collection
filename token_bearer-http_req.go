package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// Init
	url := "https://httpbin.org/bearer"
	var bearer = "Bearer 19041997"
	var jsonStr = []byte(`{"name":"Marie Curie"}`)

	req, err := http.NewRequest("GET", url, bytes.NewBuffer(jsonStr))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Add("Authorization", bearer)

	// Client HTTP Post
	client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
	defer resp.Body.Close()
	
	// HTTP Response
	data, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(data))
	
}
