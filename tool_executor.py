from print import select, insert, update, delete

def execute_query(query_type):
    if query_type == "select":
        select()
    elif query_type == "insert":
        insert()
    elif query_type == "update":
        update()
    elif query_type == "delete":
        delete()
    else:
        print("Invalid query type")