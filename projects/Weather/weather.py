"""Finds the min, max, and average values Ft. Lauderdale airport in Ft. Lauderale, FL station number 74783012849."""

__author__ = "730322626"

import sys
from typing import List, Dict
from csv import DictReader

READ_MODE: str = "r"


def main() -> None: 
    """Entrypoint of the program run as module."""
    args: Dict[str, str] = read_args()
    result_list: List[float] = convert_to_list(args['FILE'], args['COLUMN'])
    min_max_avg(args, result_list)


def read_args() -> Dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "FILE": sys.argv[1],
        "COLUMN": sys.argv[2],
        "OPERATION": sys.argv[3]
    }
    

def convert_to_list(file_path: str, column: str) -> List[float]:
    """Converts str data to float data and puts it in a usable list."""
    file_handle = open(file_path, READ_MODE, encoding="utf8") 
    csv_reader = DictReader(file_handle)
    results_list: List[float] = []
    for line in csv_reader:
        if line['REPORT_TYPE'] == "SOD  ":
            if column in line:
                try:
                    results_list.append(float(line[column]))
                except ValueError:
                    ...
            else:
                print("Invalid column: " + column)
                exit()
    print(results_list)
    return results_list


def min_max_avg(dictionary: Dict[str, str], final_list: List[float]) -> float:
    """Finds the minimum or maximum or average values of a given column."""
    if (dictionary['OPERATION']) == "min":
        min_value: float = min(final_list)
        print(min_value)
    elif (dictionary['OPERATION']) == "max":
        max_value: float = max(final_list)
        print(max_value)
    elif (dictionary['OPERATION']) == "avg":
        mean: float = (sum(final_list) / len(final_list))
        print(mean)          
    else:
        print("Invalid operation: " + dictionary['OPERATION'])
        exit()


if __name__ == "__main__":
    main()