// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cLen = 1000

func add(a, b []int) []int {
	c := []int{}
	carry := 0
	for i := 0; i < len(a) || i < len(b); i++ {
		c = append(c, carry)
		if i < len(a) {
			c[len(c)-1] += a[i]
		}
		if i < len(b) {
			c[len(c)-1] += b[i]
		}
		carry = c[len(c)-1] / 10
		c[len(c)-1] %= 10
	}

	for carry != 0 {
		c = append(c, carry%10)
		carry /= 10
	}

	return c
}

func main() {
	idx := 2
	fib0, fib1 := []int{1}, []int{1}
	for len(fib1) < cLen {
		fib0, fib1 = fib1, add(fib0, fib1)
		idx++
	}

	fmt.Printf("%d\n", idx)
}
