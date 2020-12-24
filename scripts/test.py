import os


def run_test_pipeline():
    pipeline = [
        {
            'name': 'Unit Test',
            'title': 'Running Unit Test using Pytest',
            'command': lambda : os.system('pytest -vv --durations=0')
        },
        {
            'name': 'Typing Checker',
            'title': 'Running Typing Checker',
            'command': lambda : os.system('mypy -p tsp_ga')
        }
    ]
    
    for each in pipeline:
        print(each.get('title'))
        each.get('command')()
        print("=" * os.get_terminal_size().__getattribute__('columns'))
