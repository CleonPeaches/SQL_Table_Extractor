'''
Pyhton 3.6.7 required
'''

import os
import subprocess
import gzip
import shutil
import sys

def parse_table_names():
    if len(sys.argv) == 0:
        input('No input file detected. Press [Enter] to exit...')
        sys.exit(0)
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except:
        print('Error in reading text file. Make sure text file consists only of table names, each on its own line.')
        sys.exit(0)

'''Iterate over table names to create powershell commands'''
def create_commands(table_names):
    commands = []
    for table in table_names:
        commands.append(''.join(['BCP \"Select * from Archive.IBS.', table, '\" queryout C:\\BCP\\raw-cna-mwia-dc1-',
            table, '_Archive-interval_20180420_20190827_dumpedon_20190827-', table,
            '_Archive_20190827_1.txt -S BI-PRTR -T -r \"\\r\" -t \",\" -c -C 65001'])   
    )
    return commands

'''Execute all commands'''
def execute_commands(commands):
    for command in commands:
        subprocess.run(command)

'''Compress new files to .gz format'''
def compress_files():
    for filename in os.listdir('C:\\BCP'):
        if filename.endswith('.txt'):
            with open('C:\\BCP\\' + filename, 'rb') as file_in, gzip.open('C:\\Compressed BCP\\' + str(filename[:-4]) + '.gz', 'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)


def main():
    table_names = parse_table_names()
    commands = create_commands(table_names)
    execute_commands(commands)
    compress_files()

if __name__ == '__main__':
    main()


