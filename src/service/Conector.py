import mysql.connector

class Conector:
    
    conexion = None
    cursor = None
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='mysql8002.site4now.net',
                user='aaca99_ventas',
                password='ventas123',
                database='db_aaca99_ventas',
            )
            if self.conexion.is_connected():
                self.cursor = self.conexion.cursor()
            else:
                print("Error: No se pudo establecer la conexión a la base de datos.")
            
            # print( 'conector: ' * self.conexion )
            # print( 'cursor: ' * self.cursor )
        
        except mysql.connector.Error as e:
            print("Error de conexión: ", e)
        
    def execute_query(self, query: str, parametros = ()):
        try:
            self.cursor.execute(query, parametros)
            filas = self.cursor.fetchall()

            columnas = [col[0] for col in self.cursor.description]

            data = []
            for fila in filas:
                objeto = {columnas[i]: fila[i] for i in range(len(fila))}
                data.append(objeto)

            return data
        except mysql.connector.Error as e:
            print("Error ejecutando la consulta: ", e)
            return None
    
    def execute_non_query(self, query: str, parametros):
        try:
            self.cursor.execute(query, parametros)
            self.conexion.commit()
            filas_afectadas = self.cursor.rowcount
            return filas_afectadas
        
        except mysql.connector.Error as e:
            print("Error ejecutando la consulta: ", e)
            return 0
    
    def get_id(self, tabla: str):
        try:
            query = f"SELECT MAX(id) FROM {tabla}"
            self.cursor.execute(query)
            fila = self.cursor.fetchone()

            if fila and fila[0] is not None:
                return fila[0] + 1
            else:
                return 1
            
        except mysql.connector.Error as e:
            print("Error obteniendo el id: ", e)
            return None
        
    def __del__(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
