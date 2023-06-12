from my_datetime import get_current_date
from rich import print

def get_employees():
    d = get_current_date()
    print(f'[italic red]get_employees has been executed {d}[/italic red]')

if __name__ == '__main__':
    get_employees()
