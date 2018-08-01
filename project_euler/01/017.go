// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const n = 1000

var zeroToNineteen = []string{
	"", "one", "two", "three", "four",
	"five", "six", "seven", "eight", "nine",
	"ten", "eleven", "twelve", "thirteen", "fourteen",
	"fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
}

var zeroToNinety = []string{
	"", "", "twenty", "thirty", "forty",
	"fifty", "sixty", "seventy", "eighty", "ninety",
}

const hundred = "hundred"
const and = "and"
const thousand = "thousand"

func getCnt(n int) int {
	if n <= 19 {
		return len(zeroToNineteen[n])
	} else if n <= 99 {
		return len(zeroToNinety[n/10]) + len(zeroToNineteen[n%10])
	} else if n <= 999 {
		ret := len(zeroToNineteen[n/100]) + len(hundred)
		if n%100 != 0 {
			ret += len(and) + getCnt(n%100)
		}
		return ret
	}
	return len(zeroToNineteen[1]) + len(thousand)
}

func main() {
	sum := 0
	for i := 1; i <= 1000; i++ {
		sum += getCnt(i)
	}

	fmt.Printf("%d\n", sum)
}
