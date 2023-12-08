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
    * [Install](#install)
    * [Upgrade](#upgrade)
  * [Usage](#usage)
  * [Parameters](#parameters)
    * [factors_calculator](#factorscalculator-)
    * [interest_rate_calculator](#interestratecalculator-)
  * [Examples](#examples)
    * [Example 1](#example-1)
    * [Example 2](#example-2)
  * [Supported Factors](#supported-factors)
    * [`P`](#p)
    * [`F`](#f)
    * [`A`](#a)
<!-- TOC -->

## Installation

### Install

Use python package manager (pip) to install.

```bash
pip install fincalc
```

### Upgrade

Use python package manager (pip) to upgrade.

```bash
pip install fincalc --upgrade
```

## Usage

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()
result = FC.factors_calculator('200(P/A,8.25%,3)')
print(result)
```

## Parameters

### factors_calculator 

```python
factors_calculator(equation: str, rfp: int = 5)
```

- `equation` : User input equation.
- `rfp` : Round Floating Points. Defaults to 5.

### interest_rate_calculator 

```python
interest_rate_calculator(equation: str, rfp: int = 5, interest_rate_range: tuple = (-10, 100))
```

- `equation` : User input equation.
- `rfp` : Round Floating Points. Defaults to 5.
- `interest_rate_range` : Interest Rate Range. Defaults to (-10, 100).

## Examples

### Example 1

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()
result = FC.factors_calculator('200(P/A,8.25%,3)')
print(result)
```

---

### Example 2

```python
from fincalc import FinancialCalculator

FC = FinancialCalculator()
result = FC.interest_rate_calculator('-60000+12000*(p/a,i,25)+3000(p/f,i,25)')
print(result)
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

