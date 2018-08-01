// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 20

func gcd(a, b int64) int64 {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func lcm(a, b int64) int64 {
	return a / gcd(a, b) * b
}

func main() {
	ans := int64(1)
	for i := 1; i <= n; i++ {
		ans = lcm(ans, int64(i))
	}

	fmt.Printf("%d\n", ans)
}
