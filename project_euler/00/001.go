// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 1000

func main() {
	low3, high3 := 3, (n-1)/3*3
	low5, high5 := 5, (n-1)/5*5
	low15, high15 := 15, (n-1)/15*15

	sum3 := (low3 + high3) * ((high3-low3)/3 + 1) / 2
	sum5 := (low5 + high5) * ((high5-low5)/5 + 1) / 2
	sum15 := (low15 + high15) * ((high15-low15)/15 + 1) / 2

	ans := sum3 + sum5 - sum15

	fmt.Printf("%d\n", ans)
}
