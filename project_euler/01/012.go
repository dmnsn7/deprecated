// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 20000
const cm = 500

func getFacCnt(n int) int {
	facCnt := 1
	for i := 2; i <= n/i; i++ {
		if n%i == 0 {
			toMulti := 0
			for n%i == 0 {
				n /= i
				toMulti++
			}

			facCnt *= toMulti + 1
		}
	}

	if n != 1 {
		facCnt *= 2
	}

	return facCnt
}

func main() {
	for i := 1; i <= cn; i++ {
		sum := i * (i + 1) / 2
		if getFacCnt(sum) > cm {
			fmt.Printf("%d\n", sum)
			break
		}
	}
}
