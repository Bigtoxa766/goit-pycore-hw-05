import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'-?\d+(\.\d+)?'
    numbers = re.finditer(pattern, text)

    for num in numbers:
        yield float(num.group())


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def sum_profit(text: str, func: Callable):
    take_numbers_from_text = func(text) 
    total= 0

    for numbers in take_numbers_from_text:
        total += numbers

    return total
    
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")