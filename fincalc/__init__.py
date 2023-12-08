from .helper import format_string, calculator, output_format, string_factor, calculate_factor_i, calculator_i


class FinancialCalculator:
    @staticmethod
    def factors_calculator(equation: str, rfp: int = 5):
        """
        This is the main function which calculates the solution of the equation

        Args:
            equation (str): User input equation
            rfp (int, optional): Round Floating Points. Defaults to 5.

        Returns:
            equation (str): '4500*(a/p,8,8)+...'
            factors (dict): {'(a/p,8,8)': 0.17401, ...}
            answer (str): '4500*0.17401+...'
            result (float): 381.85773
        """
        factors = {}
        equation = format_string(equation)
        answer = equation
        result = calculator(equation, rfp, factors)
        for Factor, Factor_Value in factors.items():
            answer = answer.replace(Factor, str(Factor_Value))
        return output_format(equation), factors, output_format(answer), result

    @staticmethod
    def interest_rate_calculator(equation: str, rfp: int = 5, interest_rate_range: tuple = (-10, 100)):
        """
        This is the main function which calculates the solution of the equation

        Args:
            equation (str): User input equation
            rfp (int, optional): Round Floating Points. Defaults to 5.
            interest_rate_range (tuple, optional): Interest Rate Range. Defaults to (-10, 100).

        Returns:
            answer (str): '4500*0.17401+...'
            factors (list): ['(a/p,i,8)', ...]
            result (float): 381.85773
        """
        factors = []
        equation = format_string(equation)
        answer = equation
        calculate_factor_i(equation, rfp, factors)
        for Factor in factors:
            answer = answer.replace(Factor, string_factor(Factor))
        result = calculator_i(answer, rfp, interest_rate_range)
        factors = list(map(output_format, factors))
        return output_format(equation), factors, result
