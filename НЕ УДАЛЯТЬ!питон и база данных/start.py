# import psycopg2

# try:
#     connection = psycopg2.connect(
#         host = "localhost",
#         dbname = "payments",
#         user = "postgres",
#         password = "0770757702")
#     print("Успешно подключено")
#     cursor = connection.cursor()

   
    
#     # query = f"SELECT * FROM operations WHERE whom_to_send = {id} ;"
#     # cursor.execute(query)
#     # operations = cursor.fetchall()

#     # for operation in operations:
#     #     print(operation)
#     x = input()
#     query = f"select * from operations as o left join users as u ON o.whom_to_send = u.id where u.fullname like '%{x}%'; "
#     cursor.execute(query)
#     operations = cursor.fetchall()

#     for operation in operations:
#          print(operation)


# except Exception as e:
#     print("Возникла ошибка")
#     print(e)    
# except:
#     print("Возникла ошибка")
# finally:
#     if connection:
#         connection.close()


