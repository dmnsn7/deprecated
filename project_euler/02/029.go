// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cA = 100
const cB = 100

type pair struct {
	fisrt  int
	second int
}

func main() {
	isVisited := map[pair]int{}
	cnt := (cA - 1) * (cB - 1)
	for i := 2; i <= cA; i++ {
		for j := 2; j <= cB; j++ {
			ti, minDiv := i, 1
			for k := 2; k <= ti/k; k++ {
				if ti%k == 0 {
					minDiv *= k
					for ti%k == 0 {
						ti /= k
					}
				}
			}

			tti, level := i, 0
			for minDiv != 1 && tti%minDiv == 0 {
				tti /= minDiv
				level++
			}

			if tti != 1 {
				isVisited[pair{i, j}] = 0
			} else if _, exist := isVisited[pair{minDiv, level * j}]; !exist {
				isVisited[pair{minDiv, level * j}] = 0
			} else {
				cnt--
			}
		}
	}

	fmt.Printf("%d\n", cnt)
}
