def find_missing_digit(code):
    code = list(code.strip())

    weights = [1, 3] * 6  # 12개의 가중치 (1,3 반복)
    star_index = code.index('*')
    for candidate in range(10):
        temp = code[:]
        temp[star_index] = str(candidate)
        try:
            partial_sum = sum(int(temp[i]) * weights[i] for i in range(12))
            expected_m = (10 - (partial_sum % 10)) % 10
            if int(temp[12]) == expected_m:
                return candidate
        except ValueError:
            continue
    return None

code = input()
missing = find_missing_digit(code)
if missing is not None:
    print(missing)
else:
    print("유효한 숫자를 찾을 수 없습니다.")