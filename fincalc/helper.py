import re


def format_string(string: str) -> str:
    """
    This function changes string to standard format

    Args:
        string (str): User input string

    Returns:
        (str): Standard format of string
    """
    string = string.lower()
    changes = {' ': '',
               '\n': '',
               '%': '',
               '+-': '-',
               '+(-': '-(',
               '-(+': '-(',
               ')(': ')*(',
               '0(': '0*(',
               ')0': ')*0',
               '1(': '1*(',
               ')1': ')*1',
               '2(': '2*(',
               ')2': ')*2',
               '3(': '3*(',
               ')3': ')*3',
               '4(': '4*(',
               ')4': ')*4',
               '5(': '5*(',
               ')5': ')*5',
               '6(': '6*(',
               ')6': ')*6',
               '7(': '7*(',
               ')7': ')*7',
               '8(': '8*(',
               ')8': ')*8',
               '9(': '9*(',
               ')9': ')*9',
               }
    for old, new in changes.items():
        string = string.replace(old, new)
    return string


def inner_factor(string: str) -> str:
    """
    This function finds the inner parenthesis of a string

    Args:
        string (str): Main string

    Returns:
        str: The first inner parenthesis
    """
    pattern = r'\([^()]+\)'
    result = re.findall(pattern, string)
    try:
        return result[0]
    except:
        return '=' + string


def calculate_factor(string: str, rfp: int, factors) -> str:
    """
    This function calculates the inner factor of a string and replaces it with its value

    Args:
        string (str): Main string
        rfp (int): Round Floating Points. Defaults to rfp
        factors (dict): Dictionary of factors

    Returns:
        str: Main string with inner factor replaced
        Error (str): Returns 'Invalid Factor' when can't evaluate input
    """
    factor = inner_factor(string)

    if factor.startswith('='):
        return factor

    if factor.count(',') == 2:
        j = None
        f, i, n = factor[1:-1].split(',')
        i, n = float(i) / 100, float(n)
    elif factor.count(',') == 3:
        f, i, j, n = factor[1:-1].split(',')
        i, j, n = float(i) / 100, float(j) / 100, float(n)
    else:
        try:
            return string.replace(factor, str(eval(factor)))
        except:
            return 'Invalid Factor'

    result = None

    if f == 'f/p':
        result = round((1 + i) ** n, rfp)
    elif f == 'p/f':
        result = round((1 / (1 + i)) ** n, rfp)
    elif f == 'a/f':
        result = round((i / ((1 + i) ** n - 1)), rfp)
    elif f == 'a/p':
        result = round(((i * ((1 + i) ** n)) / ((1 + i) ** n - 1)), rfp)
    elif f == 'f/a':
        if j is None:
            result = round((((1 + i) ** n - 1) / i), rfp)
        elif j == i:
            result = round((n * ((1 + j) ** (n - 1))), rfp)
        elif j != i:
            result = round(((((1 + i) ** n) - ((1 + j) ** n)) / (i - j)), rfp)
    elif f == 'p/a':
        if j is None:
            result = round((((1 + i) ** n - 1) / (i * ((1 + i) ** n))), rfp)
        elif j == i:
            result = round((n / (1 + i)), rfp)
        elif j != i:
            result = round(((1 - ((1 + j) ** n) * ((1 + i) ** ((-1) * n))) / (i - j)), rfp)
    elif f == 'p/g':
        result = round((((1 + i) ** n - 1) / ((i ** 2) * ((1 + i) ** n))) - (n / (i * (1 + i) ** n)), rfp)
    elif f == 'f/g':
        result = round((((1 + i) ** n - 1) / (i ** 2)) - (n / i), rfp)
    elif f == 'a/g':
        result = round((1 / i) - (n / ((1 + i) ** n - 1)), rfp)

    if result is not None:
        factors[factor] = result
    return string.replace(factor, str(result))


def calculate_factor_i(string: str, rfp: int, factors: list) -> float:
    """
    This function finds the inner factor of a string and replaces it with its value

    Args:
        string (str): Main string
        rfp (int): Round Floating Points. Defaults to rfp
        factors (dict): Dictionary of factors

    Returns:
        str: Main string with inner factor replaced
        Error (str): Returns 'Invalid Factor' when can't evaluate input
    """

    def find_factor(text: str, factors) -> str:
        factor = inner_factor(text)

        if factor.startswith('='):
            return factor

        try:
            f, i, n = factor[1:-1].split(',')
        except:
            try:
                return text.replace(factor, str(eval(factor)))
            except:
                return 'Invalid Factor'

        factors.append(factor)

        text = text[text.find(factor):]  # remove until factor
        text = text.replace(factor, '')  # remove factor
        return text

    while True:
        string = find_factor(string, factors)
        if string.startswith('='):
            try:
                return round(float(eval(string[1:])), rfp)
            except:
                return 'Invalid Input'


def calculator(string: str, rfp: int, factors) -> float:
    """
    This function is used to solve the equation

    Args:
        string (str): Main string with changes
        rfp (int): Round Floating Points. Defaults to rfp
        factors (dict): Dictionary of factors

    Returns:
        float: The solution of the equation
        Error (str): Returns 'Invalid Input' when can't evaluate input
    """
    while True:
        string = calculate_factor(string, rfp, factors)
        if string.startswith('='):
            try:
                return round(float(eval(string[1:])), rfp)
            except:
                return 'Invalid Input'


def calculator_i(string: str, rfp: int, interest_rate_range: tuple) -> float:
    """
    This function is used to solve the equation

    Args:
        string (str): Main string with changes
        rfp (int): Round Floating Points. Defaults to rfp
        interest_rate_range (tuple): minimum and maximum interest rate range

    Returns:
        float: The solution of the equation
        Error (str): Returns 'Invalid Input' when can't evaluate input
    """

    interest_rate_dict = {}

    lb, ub = interest_rate_range
    for i in range(lb * 100, ub * 100):
        i /= 100
        if i == 0:
            continue
        val = float(eval(string.replace('i', f'{i / 100}')))
        interest_rate_dict[val] = i

    closest_to_zero = min(interest_rate_dict.keys(), key=abs)

    return round(interest_rate_dict[closest_to_zero], rfp)  # , closest_to_zero


def string_factor(factor):
    f, i, n = factor[1:-1].split(',')
    n = float(n)
    factors = {
        'f/p': f'(1+i)**{n}',
        'p/f': f'(1/(1+i))**{n}',
        'a/f': f'(i/((1+i)**{n}-1))',
        'a/p': f'((i*((1+i)**{n}))/((1+i)**{n}-1))',
        'f/a': f'(((1+i)**{n}-1)/i)',
        'p/a': f'(((1+i)**{n}-1)/(i*((1+i)**{n})))',
        'p/g': f'(((1+i)**{n}-1)/((i**2)*((1+i)**{n}))) - ({n}/(i*(1+i)**{n}))',
        'f/g': f'(((1+i)**{n}-1)/(i**2))-({n}/i)',
        'a/g': f'(1/i)-({n}/((1+i)**{n}-1))',
    }
    return factors[f]


def output_format(string: str) -> str:
    """
    This function converts output to standard format

    Args:
        string (str): Main string with changes

    Returns:
        (str): Replaced string
    """
    string = string.replace('+', ' + ')
    string = string.replace('-', ' - ')
    string = string.strip()
    if string.startswith('- '):
        string = f'-{string[2:]}'
    string = string.upper()
    string = string.replace('I', 'i')
    return string
