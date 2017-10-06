import os

def import_pattern_rle(filename):
    with open(filename, 'r') as input_file:
        header = input_file.next()
        print(header)

print(os.getcwd())
import_pattern_rle(os.getcwd() + "/glider.rle")
