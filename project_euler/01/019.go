// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const yearBegin = 1900
const yearEnd = 2000

var monthDay = []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

func isLeap(year int) bool {
	return year%400 == 0 || year%100 != 0 && year%4 == 0
}

func main() {
	year, month, week := yearBegin, 0, 1
	cnt := 0
	for year <= yearEnd {
		if year >= yearBegin+1 && week == 0 {
			cnt++
		}
		if month == 1 && isLeap(year) {
			week = (week + monthDay[month] + 1) % 7
		} else {
			week = (week + monthDay[month]) % 7
		}
		if month == 11 {
			year++
			month = 0
		} else {
			month++
		}
	}

	fmt.Printf("%d\n", cnt)
}
