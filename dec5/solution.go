package main

import (
  "bufio"
  "fmt"
//  "log"
  "os"
)

func main() {
  lines, _ := os.Open("input.txt")

  scanner := bufio.NewScanner(lines)

  for scanner.Scan() {
    fmt.Printf("%s\n", scanner.Text())
  }


  defer lines.Close()
}
