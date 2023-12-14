from .helper import format_string, calculator, output_format, string_factor, calculate_factor_i, calculator_i, calculate_factor


class FinancialCalculator:
    @staticmethod
    def calculate_factors(equation: str, rfp: int = 5) -> dict:
        """
        This is the main function which calculates the solution of the equation.

        Args:
            equation (str): User input equation.
            rfp (int, optional): Round Floating Points. Defaults to 5.

        Returns:
            equation (str): '1500*(P/A,12,3)*(P/F,12,6) + 200*(P/A,12,8,4)'
            factors (dict): {'(p/a,12,3)': 2.40183, '(p/f,12,6)': 0.50663, '(p/a,12,8,4)': 3.38462}
            answer (str): '1500*2.40183*0.50663 + 200*3.38462'
            result (float): 2502.1827
        """
        factors = {}
        equation = format_string(equation)
        answer = equation
        result = calculator(equation, rfp, factors)
        for Factor, Factor_Value in factors.items():
            answer = answer.replace(Factor, str(Factor_Value))
        return {
            'equation': output_format(equation),
            'factors': factors,
            'answer': output_format(answer),
            'result': result
        }

    @staticmethod
    def calculate_ror(equation: str, rfp: int = 5, interest_rate_range: tuple = (-10, 100)):
        """
        This is the main function which calculates the solution of the equation.

        Args:
            equation (str): User input equation.
            rfp (int, optional): Round Floating Points. Defaults to 5.
            interest_rate_range (tuple, optional): Interest Rate Range. Defaults to (-10, 100).

        Returns:
            equation (str): '-60000 + 12000*(P/A,i,25) + 3000*(P/F,i,25)'
            factors (list): ['(P/A,i,25)', '(P/F,i,25)']
            result (float): 19.79
        """
        factors = []
        equation = format_string(equation)
        answer = equation
        calculate_factor_i(equation, rfp, factors)
        for Factor in factors:
            if 'i' in Factor:
                answer = answer.replace(Factor, string_factor(Factor))
            else:
                valued_factor = calculate_factor(Factor, 5, {})
                answer = answer.replace(Factor, f'({valued_factor})')
        result = calculator_i(answer, rfp, interest_rate_range)
        factors = list(map(output_format, factors))
        return {
            'equation': output_format(equation),
            'factors': factors,
            'result': result
        }
