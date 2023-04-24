fn is_palindrome(x int) bool {
	if x < 0 {
		return false	
	}
    mut reverse_number := 0
    mut original_number := x

    for original_number != 0 {
        reverse_number = reverse_number * 10 + original_number % 10
        original_number /= 10
	}
    if reverse_number == x {
		return true
	}
	return false
}

fn roman_to_int(s string) int {
    roman_to_decimal := {
		'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
	}

    mut result := 0

    for index, value in s {
        if index + 1 < s.len && roman_to_decimal[value.ascii_str()] < roman_to_decimal[s[index + 1].ascii_str()] {
			result -= roman_to_decimal[value.ascii_str()]
		} else {
			result += roman_to_decimal[value.ascii_str()]
		}
            
	}
    return result
}

fn main() {
	assert is_palindrome(121) == true
	assert is_palindrome(10) == false
	assert is_palindrome(-66) == false

	assert roman_to_int('III') == 3
	assert roman_to_int('LVIII') == 58
	assert roman_to_int('MCMXCVI') == 1996
}