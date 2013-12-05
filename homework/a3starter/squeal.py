
""" Module squeal: table and database manipulation functions.

The meanings of "table" and "database" are as described in db_io.py.
"""


def do_query(d_database,query):
    """
    (dictionary of the databease,string) -> dictionary of table by query
    
    do one query.include split the commd and do processes,
    ingore to verify that the query has the correct syntax
    just to judge if there is 'where' token query
    after every proc(from,where,select) we get a new table
    return the table at last
    
    this is the top function and the only function called by main()
    in this file
    """
    tokens = query.split()
    
    
    table = proc_from(d_database,tokens[3])
    if len(tokens) >=  6:          #means has 'where' token  in query
        
        #in case there are space in colname such as a.category = 'Actor-Leading Role'
        #make them in to together
        for piece in tokens[6:]:
            tokens[5] = tokens[5]+' '+piece
            
        table = proc_where(table,tokens[5])
    table = proc_select(table,tokens[1])    
    
    return table
    

def cartesian_product(table1,table2):
    """
    (table, table) -> table
    
    Return a new table that is the cartesian product of the 
    two arguments which are both SQuEaL tables.
    """
    table_cross = {}
    size1 = len(list(table1.values())[0])
    size2 = len(list(table2.values())[0])
    
    for col_name,items in table1.items():
        table_cross[col_name] = []
        for item in items:
            for i in range(size2):
                table_cross[col_name].append(item)
                
    for col_name,items in table2.items():
        table_cross[col_name] = []
        for i in range(size1):
            for item in items:
                table_cross[col_name].append(item)
                
    return table_cross


#----------------------------------------------------------------------
def proc_from(d_database,table_names):
    """
    (table,string)->string
    
    get the cartesian_product of all table which list at
    'from' token
    """
    
    table_names = table_names.split(',')
    
    #base table
    table = d_database[table_names[0]]
    
    for table_name in table_names[1:]:
        table = cartesian_product(table,d_database[table_name])
    
    return table

#----------------------------------------------------------------------
def proc_where(table,constraints):
    """
    (table,string)->table
    
    process any constraints in the where clause
    filter the table row as constraint one by one
    """

    constraints = constraints.split(',')
    
    result = one_filter(table,constraints[0])
    for constraint in constraints[1:]:
        result = one_filter(result,constraint)            
    return result

#----------------------------------------------------------------------
def proc_select(table,col_names):
    """
    (table,string)->table
    
    keep only those columns that were listed after the select.
    if select * then return table
    """
    
    if col_names == '*':
        return table
    else:
        col_names = col_names.split(',')
        result = {}
        for key,item in table.items():
            if key in col_names:
                result[key] = item
        return result


#----------------------------------------------------------------------
def one_filter(table,constraint):
    """
    (table,string)->table
    
    process one constraint. analytic constraint string  format 
    """
    
    #get index of row which satisfy the constraint     
    if '=' in constraint:
        col_names = constraint.split("=")
        true_index = equal_index(table,col_names[0],col_names[1])
    elif '>' in constraint:
        col_names = constraint.split(">")
        true_index = greater_index(table,col_names[0],col_names[1])
      
    #init result table
    result = {}
    for key in table.keys():
        result[key] = []
    
    #append row which satisfy the constraint   
    for index in true_index:
        for key in table.keys():
            result[key].append(table[key][index])  
    return result


    
#----------------------------------------------------------------------
def equal_index(table,col_name1,col_name2):
    """
    (table,string,string)->list
    
    check table row and find satisfy col_name1 = col_name2 or 
    column_name1 = 'value'  condition
    return a list of row index
    """
    true_index = []
    
    items_1 = table[col_name1]
    
    if col_name2 in table:     #second name is a colname
        items_2 = table[col_name2]
        for index,item in enumerate(items_1):
            if item == items_2[index]:
                true_index.append(index)
    else:                       #second name is a value    
        value = rid_quot(col_name2)
        for index,item in enumerate(items_1):
            if item == value:
                true_index.append(index)
    return true_index

#----------------------------------------------------------------------
def greater_index(table,col_name1,col_name2):
    """
    (table,string,string)->list
    
    check table row and find satisfy col_name1>col_name2  or
    column_name1>'value'  condition
    return a list of row index
    """
    true_index = []
    
    items_1 = table[col_name1]
    
    if col_name2 in table:     #second name is a colname
        items_2 = table[col_name2]
        for index,item in enumerate(items_1):
            if item > items_2[index]:
                true_index.append(index)  
    else:                     #second name is a value   
        value = rid_quot(col_name2)
        for index,item in enumerate(items_1):
            if float(item) > float(value):
                true_index.append(index)
    return true_index


#----------------------------------------------------------------------
def rid_quot(col_name2):
    """
    (string)->string
    
    just remove the "'" both side of the string
    """
    col_name2 = col_name2.replace("'","")  
    return col_name2