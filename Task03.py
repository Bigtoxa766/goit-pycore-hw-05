from pathlib import Path

core_path = Path('D:\Woolf\PythonProjects\goit-pycore-hw-05')
logfile_path = core_path / 'logfile.log'

def parse_log_line(line: str) -> dict:
    log_line_component = {}
    components = line.split(' ', 3)
    
    if len(components) == 4:
        log_line_component['date'] = components[0]
        log_line_component['time'] = components[1]
        log_line_component['level'] = components[2]
        log_line_component['message'] = components[3]
   
    return log_line_component 

def load_logs(file_path: str) -> list:
    log_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            log_file_line = file.readline()

            if log_file_line == '':
                break

            parsed_line = parse_log_line(log_file_line)
            log_list.append(parsed_line)
            
    return log_list

logs = load_logs(logfile_path)

def filter_logs_by_level(logs: list, level: str) -> list:

    filtred_logs = list(filter(lambda log: log.get('level') == level, logs))
    print(filtred_logs)

filter_logs_by_level(logs, 'ERROR')