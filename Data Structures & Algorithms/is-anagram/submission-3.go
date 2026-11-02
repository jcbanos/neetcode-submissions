func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	frequenciesS, frequenciesT := make(map[rune]int), make(map[rune]int)

	for _, value := range []rune(s) {
		frequenciesS[value] += 1
	}

	for _, value := range []rune(t) {
		frequenciesT[value] += 1
	}

	for keyS, valueS := range frequenciesS {
		valueT := frequenciesT[keyS]
		if valueS != valueT {
			return false
		}
	}

	return true
}
