# Financial Calculator

[![PyPI](https://img.shields.io/pypi/v/fincalc?label=PyPI&logo=pypi&logoColor=FFE873)](https://pypi.org/project/fincalc)
[![Downloads](https://static.pepy.tech/badge/fincalc)](https://pepy.tech/project/fincalc)
[![GitHub - License](https://img.shields.io/github/license/mahyar-amiri/django-comment-system?label=License&color=blue)](LICENSE)

A Python Library for Calculating Financial Equations.

## Table of Contents

<!-- TOC -->
* [Financial Calculator](#financial-calculator)
  * [Table of Contents](#table-of-contents)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Functions](#functions)
    * [calculate_factors](#calculate_factors)
    * [interest_rate_calculator](#interest_rate_calculator-)
  * [Examples](#examples)
    * [Example 1](#example-1)
    * [Example 2](#example-2)
  * [Supported Factors](#supported-factors)
    * [`P`](#p)
    * [`F`](#f)
    * [`A`](#a)
<!-- TOC -->

## Installation

Use python package manager (pip) to install the latest version.

```bash
pip install -U fincalc
```

## Usage

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()
```

## Functions

### calculate_factors

```python
calculate_factors(equation: str, rfp: int = 5) -> dict
```

- `equation` : User input equation.
- `rfp` : Round Floating Points. Defaults to 5.

### interest_rate_calculator 

```python
calculate_ror(equation: str, rfp: int = 5, interest_rate_range: tuple = (-10, 100)) -> dict
```

- `equation` : User input equation.
- `rfp` : Round Floating Points. Defaults to 5.
- `interest_rate_range` : Interest Rate Range. Defaults to (-10, 100).

## Examples

### Example 1

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()

result = FC.calculate_factors('1500*(P/A,12,3)*(P/F,12,6) + 200*(P/A,12,8,4)')
print(result)

# output
# {
#   'equation': '1500*(P/A,12,3)*(P/F,12,6) + 200*(P/A,12,8,4)',
#   'factors': {'(p/a,12,3)': 2.40183, '(p/f,12,6)': 0.50663, '(p/a,12,8,4)': 3.38462},
#   'answer': '1500*2.40183*0.50663 + 200*3.38462',
#   'result': 2502.1827
# }
```

---

### Example 2

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()

result = FC.calculate_ror('-60000 + 12000*(P/A,i,25) + 3000*(P/F,i,25)')
print(result)

# output
# {
#   'equation': '-60000 + 12000*(P/A,i,25) + 3000*(P/F,i,25)',
#   'factors': ['(P/A,i,25)', '(P/F,i,25)'],
#   'result': 19.79
# }
```

---

## Supported Factors

### `P`

- [x] (P/F,i%,n)
- [x] (P/A,i%,n)
- [x] (P/A,i%,j%,n)
- [x] (P/G,i%,n)

### `F`

- [x] (F/P,i%,n)
- [x] (F/A,i%,n)
- [x] (F/A,i%,j%,n)
- [x] (F/G,i%,n)

### `A`
 
- [x] (A/P,i%,n)
- [x] (A/F,i%,n)
- [x] (A/G,i%,n)
