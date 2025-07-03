import os

def file_exists(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass
