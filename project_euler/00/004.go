// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

func isPalin(num int) bool {
	digit := []int{}
	for num != 0 {
		digit = append(digit, num%10)
		num /= 10
	}

	for i := 0; i < len(digit); i++ {
		if digit[i] != digit[len(digit)-i-1] {
			return false
		}
	}

	return true
}

func main() {
	maxPalin := 0
	for i := 100; i < 1000; i++ {
		for j := 100; j < 1000; j++ {
			multi := i * j
			if multi > maxPalin && isPalin(multi) {
				maxPalin = multi
			}
		}
	}

	fmt.Printf("%d\n", maxPalin)
}
