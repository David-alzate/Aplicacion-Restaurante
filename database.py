import psycopg2

class Basedatos:
    def __init__(self,url,user,password,):
        self.url = url
        self.user = user
        self.password = password
        

    def conectar(self):
        try:        
             credenciales  ={
                  "dbname": "prueba",
                  "user": self.user,
                  "password": self.password,
                  "host": self.url,
                  "port": 5432
                  }
             conexion = psycopg2.connect(**credenciales)
             if conexion:
                  print("conexion exitosa")
                  return conexion
        except psycopg2.error as e:
            print("Ocurrio un error al conectar", e )

print("prueba")