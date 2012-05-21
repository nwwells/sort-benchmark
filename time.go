package main

import "fmt"
import "math/rand"
import "sort"
import "time"

const MaxLength = 1000000
const MaxLoops = 1000

func main() {
	nums := make([]int, MaxLength)

	for iter := 0; iter < MaxLoops; iter++ {
		for i := range nums {
			nums[i] = rand.Int()
		}
        t0 := time.Now()
		sort.Ints(nums)
        t1 := time.Now()
        delta := t1.Sub(t0)
        fmt.Printf("Elapsed time: %v microseconds\n", delta.Nanoseconds() / 1000)
	}
}
