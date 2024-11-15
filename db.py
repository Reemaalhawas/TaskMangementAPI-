import mysql.connector


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="TaskMangement"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        raise

   
def delete_task(title, description, deadline):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    sql_delete = " DELETE FROM tasks  WHERE title = %s AND description = %s AND deadline = %s " 
    
    values = (title, description, deadline)
    
    cursor.execute(sql_delete, values)
    
    connection.commit()
    
    
    if cursor.rowcount == 0:
        print("task is not found ")
    else:
        print(f"Task with title '{title}' deleted successfully.")
    
    # Close the connection
    connection.close()
def update_task(task_id = int  , description: Optional[str] = None, status= Optional[str] = None  ,  deadline = ): 
    connection = get_db_connection()
    cursor = connection.cursor()

    updated_section = []  
    values = [] 

    if description:
        updated_section.append("description = %s")
        values.append(description)

    if status:
        updated_section.append("status = %s")
        values.append(status)

    if deadline:
        updated_section.append("deadline = %s")
        values.append(deadline)

    if not updated_section:
        print("No values are updated")


    query = f"UPDATE tasks SET {', '.join(updated_section)} WHERE id = %s"
    values.append(task_id)  

    try:
        cursor.execute(query, values) 
        connection.commit()

        if cursor.rowcount == 0:
            return "Task not found"

        return "Task updated successfully"

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()


 