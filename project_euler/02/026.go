// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cD = 1000

func getRecycleSize(n int) int {
	remainder, idx := 1, 1
	visited := map[int]int{}

	for _, exist := visited[remainder]; !exist; {
		visited[remainder] = idx
		idx++
		for remainder != 0 && remainder < n {
			remainder *= 10
		}

		remainder %= n
		_, exist = visited[remainder]
	}

	if remainder != 0 {
		return idx - visited[remainder]
	}
	return 0
}

func main() {
	maxRecycleSize, target := 0, 1
	for i := 1; i < cD; i++ {
		if getRecycleSize(i) > maxRecycleSize {
			maxRecycleSize, target = getRecycleSize(i), i
		}
	}

	fmt.Printf("%d\n", target)
}
