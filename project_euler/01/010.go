// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 2000000

func primeSieve(n int) []int {
	var prime []int
	isPrime := make([]bool, n)
	for i := 0; i < n; i++ {
		isPrime[i] = true
	}
	for i := 2; i < n; i++ {
		if isPrime[i] == true {
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
	sum := int64(0)
	for i := 0; i < len(prime); i++ {
		sum += int64(prime[i])
	}

	fmt.Printf("%d\n", sum)
}
