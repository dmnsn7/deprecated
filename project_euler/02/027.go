// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cA = 1000
const cB = 1000
const cN = 2001000

func primeSieve(n int) (map[int]int, []int) {
	isPrime := make([]bool, n)
	for i := 0; i < n; i++ {
		isPrime[i] = true
	}
	mPrime, vPrime := map[int]int{}, []int{}
	for i := 2; i < n; i++ {
		if isPrime[i] {
			mPrime[i] = 0
			vPrime = append(vPrime, i)
		}
		for j := 0; j < len(vPrime) && vPrime[j]*i < n; j++ {
			isPrime[vPrime[j]*i] = false
			if i%vPrime[j] == 0 {
				break
			}
		}
	}

	return mPrime, vPrime
}

func main() {
	mPrime, _ := primeSieve(cN)

	maxLeng, multi := 0, 0
	for i := -cA + 1; i <= cA-1; i++ {
		for j := -cB + 1; j <= cB-1; j++ {
			leng := -1
			for k := 0; leng == -1; k++ {
				num := k*k + i*k + j
				if _, exist := mPrime[num]; !exist {
					leng = k
				}
			}

			if leng > maxLeng {
				maxLeng = leng
				multi = i * j
			}
		}
	}

	fmt.Printf("%d\n", multi)
}
