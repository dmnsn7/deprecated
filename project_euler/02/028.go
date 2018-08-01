// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cN = 1001

func main() {
	v := []int{1, 24, 52, 32}
	for i := 0; i < cN/2; i++ {
		v = []int{v[0] + v[1], v[1] + v[2], v[2] + v[3], v[3]}
	}

	fmt.Printf("%d\n", v[0])
}
