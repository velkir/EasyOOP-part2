arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]

def arabic_to_roman(number):
  roman_number = ""
  n_digits = len(str(number))
  for idx, digit in enumerate(str(number), start=1):
    digit = int(digit)
    if digit in [1, 4, 5, 9]:
      base_symbol = digit*10**(n_digits-idx)
      roman_number += roman[arabic.index(base_symbol)]
    elif digit in [2, 3]:
      base_symbol = 1 * 10 ** (n_digits - idx)
      roman_number += roman[arabic.index(base_symbol)]*(digit)
    elif digit in [6, 7, 8]:
      base_symbol = 5 * 10 ** (n_digits - idx)
      roman_number += roman[arabic.index(base_symbol)]
      additional_symbols = 1 * 10 ** (n_digits - idx)
      roman_number += roman[arabic.index(additional_symbols)]*(digit-5)

  return roman_number

print(arabic_to_roman(1500))