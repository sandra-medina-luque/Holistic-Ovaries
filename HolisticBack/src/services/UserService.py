from src.database.db_mysql import get_connection
from src.models.userModel import User
from werkzeug.security import generate_password_hash

class UserService():

    @classmethod
    def get_user(cls):
        try:
            connection=get_connection()
           
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM user')
                result= cursor.fetchall()
                list_user=[User.convert_from_BD(row) for row in result]
                connection.close()
                return list_user
                
        except Exception as ex: 
            print(ex)



    @classmethod
    def post_user(cls, user: User):
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                
                passwordunic = user.password
                user_type = user.user_type
                email=user.email
                print("por buen camino")
                password = generate_password_hash (passwordunic,  'pbkdf2:sha256', 30)
                cursor.callproc("InsertUser", ( password, user_type, email))
                connection.commit()
                connection.close()
                return 'Usuario agregado correctamente'
               
        except Exception as ex: 
            print(ex)

    @classmethod
    def delete_user(cls, id_user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc("DeleteUser", (id_user,))
                connection.commit()
            connection.close()
            return 'Usuario eliminado correctamente'
        except Exception as ex:
            print(ex)

    @classmethod
    def delete_userByEmail(cls, email):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute("DELETE FROM user WHERE email='{0}'".format(email))                           
                connection.commit()
                connection.close()
                return 0
        except Exception as ex:
                print(ex)
                connection.close()
        return 'Usuario eliminado correctamente'
      
    @classmethod
    def put_user(cls, id_user, user: User):
        try:
             connection = get_connection()
             with connection.cursor() as cursor:
              password = user.password
              user_type = user.user_type
              email=user.email
              
              cursor.callproc("UpdateUser", (id_user, password, user_type, email))
              connection.commit()
             connection.close()
             return 'Usuario actualizado correctamente'
        except Exception as ex:
               print(ex)
     
   
    