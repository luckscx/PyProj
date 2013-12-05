"""Module db_io: functions for I/O on tables and databases.

A table file has a .csv extension.

We define "table" to mean this:

    dict of {str: list of str}

Each key is a column name from the table and each value is the list of strings
in that column from top row to bottom row.

We define "database" to mean this:

    dict of {str: table}

Each key is the name of the .csv file without the extension.  Each value is
the corresponding table as defined above.
"""

import glob
import os


def print_csv(table):
    """ (table) -> NoneType

    Print a representation of table in the same format as a table file.
    """

    columns = list(table.keys())
    print(','.join(columns))

    # All columns are the same length; figure out the number of rows.
    num_rows = len(table[columns[0]])

    # Print each row in the table.
    for i in range(num_rows):

        # Build a list of the values in row i.
        curr_row = []
        for column_name in columns:
            curr_row.append(table[column_name][i])

        print(','.join(curr_row))


# Write your read_table and read_database functions below.
# Use glob.glob('*.csv') to return a list of csv filenames from
#   the current directory.

def read_table(f_in):
    """
     (file open for reading) -> dictionary
     
    The parameter is a table file that has been opened for reading.
    function read all lines in file and turn it to a dictionary of
    proper format
    """
    
    lines= [line.strip() for line in f_in.readlines()]

    col_names=list(lines[0].split(','))    
    
    d={}
    for col_name in col_names:
        d[col_name]=[]
    for line in lines[1:]:
        data=line.split(',')
        for i,col_name in enumerate(col_names):
            d[col_name].append(data[i])
    return d

        
#----------------------------------------------------------------------
def read_database():
    """
    () -> database
    
    The database on which this function operates consists of all 
    of the table files in the current directory. These table 
    files all have an extension of .csv. This function reads each 
    table file and returns a database (a dictionary of the proper format).
    """
    d_database={}
    filenames=glob.glob('*.csv')
    for filename in filenames:
        try:
            f_in=open(filename,'r')    
        except:
            print("fille open error")
            return False
        table_name=os.path.splitext(filename)[0]
        d_table=read_table(f_in)
        d_database[table_name]=d_table
    return d_database
            
