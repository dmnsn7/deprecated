// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 10
const ck = 1000000

func kthPermutation(n, k int) []int {
	fac := make([]int, n)
	for i := 0; i < n; i++ {
		if i == 0 {
			fac[i] = 1
		} else {
			fac[i] = fac[i-1] * i
		}
	}

	permutation := []int{}
	isUsed := make([]bool, n)
	for i := 0; i < n; i++ {
		isUsed[i] = false
	}

	for i := 0; i < n; i++ {
		kth := k / fac[n-i-1]
		k %= fac[n-i-1]
		for j, cnt := 0, 0; j < n; j++ {
			if !isUsed[j] {
				cnt++
			}
			if cnt == kth+1 {
				permutation = append(permutation, j)
				isUsed[j] = true
				break
			}
		}
	}

	return permutation
}

func main() {
	permutation := kthPermutation(cn, ck-1)
	for i := 0; i < len(permutation); i++ {
		fmt.Printf("%c", permutation[i]+'0')
	}

	fmt.Printf("\n")
}
