// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const d = 4000000

func main() {
	fib := []int{1, 2}
	for fib[len(fib)-2]+fib[len(fib)-1] <= d {
		fib = append(fib, fib[len(fib)-2]+fib[len(fib)-1])
	}

	sum := 0
	for i := 0; i < len(fib); i++ {
		if fib[i]%2 == 0 {
			sum += fib[i]
		}
	}

	fmt.Printf("%d\n", sum)
}
