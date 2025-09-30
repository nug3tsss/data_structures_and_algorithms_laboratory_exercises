def CelsiusToFarenheitAboveZeroC():
    celsius = [-5, 0, 10, 25, 30, -2, 15, 35]
    fahrenheit = [((x * 1.8) + 32) for x in celsius if x > 0]

    print(f"Celsius: {celsius}")
    print(f"Fahrenheit (>0°C only): {fahrenheit}")

def EvaluateValidGrades():
    raw_grades = ['85', 'invalid', '92', '78', '', '95', 'not_a_grade', '88']
    grade_results = ["Pass" if int(x) >= 80 else "Fail" for x in raw_grades if x.isdigit()]

    print(f"Raw grades: {raw_grades}")
    print(f"Grade results: {grade_results}")

def ReverseLongWords():
    original_text = "The quick brown fox jumps over the lazy dog"
    reversed_long_words = [x[::-1] for x in original_text.split() if len(x) > 4]

    print(f"Original: {original_text}")
    print(f"Reversed long words: {reversed_long_words}")

def ValidEmailAddDom():
    emails = ['user@gmail.com', 'invalid-email', 'test@yahoo.com', 'bad@', 'admin@company.org', 'no-at-sign.com']
    valid_domains = [x.split("@")[1] for x in emails if "@" in x and x.split("@")[1] and "." in x.split("@")[1]]

    print(f"Valid domains: {valid_domains}")

def EvenPerfectSquares():
    import math
    even_perfect_squares = [x for x in range(1, 101) if x % 2 == 0 and math.isqrt(x) ** 2 == x]
    print(f"Even perfect squares (1-100): {even_perfect_squares}")

CelsiusToFarenheitAboveZeroC()
EvaluateValidGrades()
ReverseLongWords()
ValidEmailAddDom()
EvenPerfectSquares()