package gigasecond

import "time"

const testVersion = 4

const giga = 1000000000

// API function.  It uses a type from the Go standard library.
func AddGigasecond(t time.Time) time.Time {
	return t.Add(time.Duration(giga * time.Second))
}
