// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 28123

func getFacSum(n int) int {
	facSum, tn := 1, n
	for i := 2; i <= n/i; i++ {
		if n%i == 0 {
			toMulti, base := 1, 1
			for n%i == 0 {
				base *= i
				toMulti += base
				n /= i
			}

			facSum *= toMulti
		}
	}

	if n != 1 {
		facSum *= n + 1
	}

	return facSum - tn
}

func isAbund(n int) bool {
	return getFacSum(n) > n
}

func main() {
	mAbund := map[int]int{}
	vAbund := []int{}
	for i := 1; i <= cn; i++ {
		if isAbund(i) {
			mAbund[i] = 0
			vAbund = append(vAbund, i)
		}
	}

	sum := 0
	for i := 1; i <= cn; i++ {
		flag := true
		for j := 0; j < len(vAbund) && vAbund[j] <= i-vAbund[j] && flag; j++ {
			if _, exist := mAbund[i-vAbund[j]]; exist {
				flag = false
			}
		}

		if flag {
			sum += i
		}
	}

	fmt.Printf("%d\n", sum)
}
