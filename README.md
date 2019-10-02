# SQL_Table_Extractor
Uses BCP to iterate over a text file of table names, extract, and compress them to local machine.

1. Connect to an MWI virtual machine and ensure that Python 3.6.7 is installed
  a. Check Python version by opening a command prompt and entering:

  ```python
  python –version
  ```

  b. Python 3.6.7 can be installed at https://www.python.org/downloads/release/python-367/
  c. While installing, ensure “Add to PATH” is checked

2. Create and save a text file containing a list of archival table names (e.g. SROISH) you wish to extract, each of which should be on its own line

3. Download the attached table_archive_extractor.py script and save it to your machine

4. Open up a command prompt and enter the following command:

  ```python
  python [path of script] [path of text file]
  ```

5. The script will iterate over the tables, extract them to C:\BCP as text files, and save compressed versions to C:\Compressed BCP
