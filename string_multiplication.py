def string_multiply(num1, num2):
    integers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    iStrings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = [0] * (len(num1) + len(num2))
    str_result = ''
    #  adding area to add to
    for i in range(-1, -1 * len(num1) - 1, -1):
        for j in range(-1, -1 * len(num2) - 1, -1):
            result[i + j + 1] += integers[num1[i]] * integers[num2[j]]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    #  converting result to string
    for j in result:
        str_result += iStrings[j]

    str_result = str_result.lstrip('0')
    return '0' if (str_result == '') else str_result

