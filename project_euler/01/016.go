// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"

const cn = 1000

func multi2(s string) string {
	t := ""
	carry := 0
	for i := 0; i < len(s); i++ {
		digit := carry + int(s[i]-'0')*2
		t += string(digit%10 + '0')
		carry = digit / 10
	}

	if carry != 0 {
		t += string(carry + '0')
	}

	return t
}

func main() {
	num := "1"
	for i := 0; i < cn; i++ {
		num = multi2(num)
	}

	sum := 0
	for i := 0; i < len(num); i++ {
		sum += int(num[i] - '0')
	}

	fmt.Printf("%d\n", sum)
}
