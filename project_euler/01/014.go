// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 1000000

var dp = [cn]int{}

func f(n int64) int64 {
	if n%2 == 0 {
		return n / 2
	}
	return n*3 + 1
}

func dfs(n int64) int {
	if n == 1 {
		return 1
	} else if n < cn {
		if dp[n] == 0 {
			dp[n] = dfs(f(n)) + 1
		}
		return dp[n]
	}
	return dfs(f(n)) + 1
}

func main() {
	maxLen := 1
	target := 1
	for i := 1; i < cn; i++ {
		len := dfs(int64(i))
		if maxLen < len {
			maxLen = len
			target = i
		}
	}

	fmt.Printf("%d\n", target)
}
