func isAnagram(s string, t string) bool {
	frequenciesS := make(map[rune]int)
	frequenciesT := make(map[rune]int)
	for _, value := range []rune(s) {
		frequenciesS[value] += 1
	}

	for _, value := range []rune(t) {
		frequenciesT[value] += 1
	}

	if len(frequenciesS) != len(frequenciesT) {
		return false
	}

	for keyS, valueS := range frequenciesS {
		valueT, exists := frequenciesT[keyS]
		if !exists {
			return false
		} else if valueS != valueT {
			return false
		}
	}

	return true
}
