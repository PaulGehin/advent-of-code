from utils import run_year, get_year

if __name__ == '__main__':
    for year in range(2020, get_year()):
        run_year(year, check=True)
