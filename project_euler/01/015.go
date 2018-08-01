// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cr = 20
const cc = 20

func getComb(a, b int) int64 {
	comb := int64(1)
	for i := 1; i <= b; i++ {
		comb = comb * int64(a-i+1) / int64(i)
	}

	return comb
}

func main() {
	comb := getComb(cr+cc, cr)

	fmt.Printf("%d\n", comb)
}
