// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 200000
const k = 10001

func primeSieve(n int) []int {
	prime := []int{}
	isPrime := make([]bool, n)
	for i := 0; i < n; i++ {
		isPrime[i] = true
	}
	for i := 2; i < n; i++ {
		if isPrime[i] {
			prime = append(prime, i)
		}
		for j := 0; j < len(prime) && prime[j]*i < n; j++ {
			isPrime[prime[j]*i] = false
			if i%prime[j] == 0 {
				break
			}
		}
	}

	return prime
}

func main() {
	prime := primeSieve(n)

	kthPrime := prime[k-1]

	fmt.Printf("%d\n", kthPrime)
}
