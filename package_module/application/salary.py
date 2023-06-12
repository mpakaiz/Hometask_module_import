from my_datetime import get_current_date
from rich import print

def calculate_salary():
    d = get_current_date()
    print(f'[italic red]calulate_salary has been executed on {d}[/italic red]')

if __name__ == '__main__':
    calculate_salary()
