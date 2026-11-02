func hasDuplicate(nums []int) bool {
	var alreadyAppeared map[int]bool
	alreadyAppeared = make(map[int]bool)
	for _, val := range nums {
		_, exists := alreadyAppeared[val]
		if exists {
			return true
		}

		alreadyAppeared[val] = true
	}

	return false
}
