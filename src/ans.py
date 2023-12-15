""" 
Practice Question 6: Recursive Directory Size Calculator

Task:
Create a function calculate_directory_size that computes the total size (in bytes) 
of all files in a directory and its subdirectories. The function should handle any 
exceptions and return the total size. Store this function in a module called directory_size_calculator.py.

Unit Test for Recursive Directory Size Calculator:

Create a file test_directory_size_calculator.py for testing.
"""
import os

def calculate_directory_size(directory_to_check):
    list_files_in_directory = []
    total_sum = 0
    try: 
        list_files_in_directory = os.listdir(directory_to_check)
    except FileNotFoundError:
        raise FileNotFoundError
    
    for indiv_file in list_files_in_directory:
        full_path = os.path.join(directory_to_check, indiv_file)
        print(f'Current path is: {full_path}')
        if os.path.isfile(full_path):
            print(f'Size of current file is: {os.path.getsize(full_path)}')
            total_sum += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            print(
                f"Total size calculated: {calculate_directory_size(full_path)}")
            total_sum += calculate_directory_size(full_path)
        
    return total_sum
    

# added to print and test this out
print(calculate_directory_size('test_folder/other_file_two/other_file_three'))
