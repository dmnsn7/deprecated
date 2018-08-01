// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 10000

func getFacSum(n int) int {
	facSum, tn := 1, n
	for i := 2; i <= tn/i; i++ {
		if tn%i == 0 {
			toMulti, base := 1, 1
			for tn%i == 0 {
				base *= i
				toMulti += base
				tn /= i
			}
			facSum *= toMulti
		}
	}

	if tn != 1 {
		facSum *= tn + 1
	}

	return facSum - n
}

func isAmic(n int) bool {
	return getFacSum(n) != n && getFacSum((getFacSum(n))) == n
}

func main() {
	amicSum := 0
	for i := 2; i < cn; i++ {
		if isAmic(i) {
			amicSum += i
		}
	}

	fmt.Printf("%d\n", amicSum)
}
