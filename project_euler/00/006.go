// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 100

func main() {
	sum1 := n * (n + 1) / 2
	sum2 := n * (n + 1) * (2*n + 1) / 6
	ans := sum1*sum1 - sum2

	fmt.Printf("%d\n", ans)
}
