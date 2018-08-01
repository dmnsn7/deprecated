// Copyright [2017] <dmnsn7@gmail.com>

package main

import "fmt"
import "sort"

func main() {
	text := ""
	fmt.Scanf("%s", &text)

	names, name := []string{}, ""
	for i := 0; i < len(text); i++ {
		if text[i] == '"' && name != "" {
			names = append(names, name)
			name = ""
		} else if text[i] >= 'A' && text[i] <= 'Z' {
			name += string(text[i])
		}
	}

	sort.Strings(names)
	scoreSum := 0
	for i := 0; i < len(names); i++ {
		for j := 0; j < len(names[i]); j++ {
			scoreSum += int(names[i][j]-'A'+1) * (i + 1)
		}
	}

	fmt.Printf("%d\n", scoreSum)
}
