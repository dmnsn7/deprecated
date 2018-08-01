// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const sum = 1000

func main() {
	for i := 1; i <= sum; i++ {
		for j := i; i+j <= sum && sum-i-j >= j; j++ {
			k := sum - i - j
			if i*i+j*j == k*k {
				multi := i * j * k
				fmt.Printf("%d\n", multi)
			}
		}
	}
}
