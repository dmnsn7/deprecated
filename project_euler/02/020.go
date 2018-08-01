// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 100

func multiply(a []int, b int) []int {
	multi := []int{}
	carry := 0
	for i := 0; i < len(a); i++ {
		num := a[i]*b + carry
		multi = append(multi, num%10)
		carry = num / 10
	}

	for carry != 0 {
		multi = append(multi, carry%10)
		carry /= 10
	}

	return multi
}

func main() {
	fac := []int{1}
	for i := 1; i <= n; i++ {
		fac = multiply(fac, i)
	}

	sum := 0
	for i := 0; i < len(fac); i++ {
		sum += fac[i]
	}

	fmt.Printf("%d\n", sum)
}
