package leap

const (
	testVersion   = 3
	rule_4_year   = 4
	rule_100_year = 100
	rule_400_year = 400
)

func IsLeapYear(year int) bool {
	if year%rule_4_year == 0 {
		if year%rule_100_year == 0 {
			if year%rule_400_year == 0 {
				return true
			} else {
				return false
			}
		} else {
			return true
		}
	} else {
		return false
	}
}
