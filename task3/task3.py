import json
import sys

def main():

    values_file, tests_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(values_file, 'r') as file:
        values = json.load(file)['values']
        
    with open(tests_file, 'r') as file:
        tests = json.load(file)['tests']

    value_dict = {str(item['id']): item['value'] for item in values}

    def fill_values(data):
        if isinstance(data, dict):

            if 'id' in data:
                test_id = str(data['id'])
                if test_id in value_dict:
                    data['value'] = value_dict[test_id]
            
            for dict_key in data:
                if isinstance(data[dict_key], (dict, list)):
                    fill_values(data[dict_key])
                    
        elif isinstance(data, list):
            for item in data:
                fill_values(item)

    fill_values(tests)


    with open(report_file, 'w') as file:
        json.dump(tests, file, indent=2)
    
    print(f"Файл {report_file} создан")

main()

# Для использования: python task3.py <values.json> <tests.json> <report.json>