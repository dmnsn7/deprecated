// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 600851475143

func main() {
	tn, maxPrimeFac := n, 0
	for i := 2; i <= tn/i; i++ {
		if tn%i == 0 {
			maxPrimeFac = i
			for tn%i == 0 {
				tn /= i
			}
		}
	}
	if tn != 1 {
		maxPrimeFac = tn
	}

	fmt.Printf("%d\n", maxPrimeFac)
}
