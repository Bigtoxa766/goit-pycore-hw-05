from tabulate import tabulate
from pathlib import Path
from functools import wraps
import sys

core_path = Path('D:\Woolf\PythonProjects\goit-pycore-hw-05')
logfile_path = core_path / 'logfile.log'

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            return "File not found"
        except KeyError:
            return 'Uknown command'
        except:
            return 'Something went wrong'
    
        

    return inner

def parse_log_line(line: str) -> dict:
    log_line_component = {}
    components = line.split(' ', 3)
    
    if len(components) == 4:
        log_line_component['date'] = components[0]
        log_line_component['time'] = components[1]
        log_line_component['level'] = components[2]
        log_line_component['message'] = components[3]
   
    return log_line_component 

@input_error
def load_logs(file_path: str) -> list:
    log_list = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for log_file_line in file:
            parsed_line = parse_log_line(log_file_line.strip())
            if parsed_line:
                log_list.append(parsed_line)
            
    return log_list

logs = load_logs(logfile_path)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log.get('level') == level, logs))

def count_logs_by_level(logs: list) -> dict:
    log_count = {}

    for log in logs:
        level = log.get('level')

        if level in log_count:
            log_count[level] += 1
        else:
            log_count[level] = 1

    return log_count

log_counts = count_logs_by_level(logs)

def parse_input(user_input):
    logfile_path, *args = user_input.split()
    logfile_path = Path(logfile_path.strip())
    return logfile_path, *args

@input_error
def display_log_counts(counts: dict):
    while True:
        if len(sys.argv) > 1:
            user_input = Path(sys.argv[1])
        else:
            user_input = Path(input("Enter log file path: "))

        if str(user_input).lower() in ["close", "exit"]:
            print("Good bye!")
            break

        logs = load_logs(logfile_path)
        level = input("Enter log level (or press Enter to display all logs): ").strip().upper()
        
        if level in ["CLOSE", "EXIT"]:
            print("Good bye!")
            break

        if level:
            filtered_logs = filter_logs_by_level(logs, level)
            print(tabulate(filtered_logs, headers="keys"))
        else:
            print(tabulate(logs, headers="keys"))

        updated_counts = count_logs_by_level(logs)
        for lvl, count in updated_counts.items():
            if lvl in counts:
                counts[lvl] += count
            else:
                counts[lvl] = count
        
        log_counts_table = [(lvl, count) for lvl, count in counts.items()]
        print(tabulate(log_counts_table, headers=["Level", "Count"]))

if __name__ == "__main__":
    initial_counts = {}
    display_log_counts(initial_counts)
