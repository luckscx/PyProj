"""
Process SQuEaL queries from the keyboard and print the results.
"""

import db_io
import squeal


def main():
    """ () -> NoneType

    Ask for queries from the keyboard; stop when empty line is received. For
    each query, process it and use db_io.print_csv to print the results.
    """
    # Write your main function body here.
    
    #Reads the database in the current directory.
    d=db_io.read_database()
    
    #Reads SQuEaL queries from the keyboard until a blank line is entered. 
    #After running the query, continue with the next input prompt.
    while True:    
        query = input("input query:")
        if query == "":
            break
        table = squeal.do_query(d,query)
        db_io.print_csv(table)    
        
    

if __name__ == '__main__':
    main()