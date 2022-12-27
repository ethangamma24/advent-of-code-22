package main

import (
  "bufio"
  "fmt"
  "os"
  "stack/stack.go"
)

func main() {
  lines, _ := os.Open("input.txt")

  scanner := bufio.NewScanner(lines)

  for scanner.Scan() {
    fmt.Printf("%s\n", scanner.Text())
  }


  defer lines.Close()
}
