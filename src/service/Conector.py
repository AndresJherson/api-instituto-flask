import pyodbc

class Conector:
    
    conexion = None
    cursor = None
    
    def __init__(self):
        try:
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=sql8020.site4now.net;'
                'DATABASE=db_aaca99_ventas;'
                'UID=db_aaca99_ventas_admin;'
                'PWD=ventas123;'
            )
            self.cursor = self.conexion.cursor()
            
        except pyodbc.Error as e:
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
        except pyodbc.Error as e:
            print("Error ejecutando la consulta: ", e)
            return None
    
    def execute_non_query(self, query: str, parametros):
        try:
            self.cursor.execute(query, parametros)
            self.conexion.commit()
            filas_afectadas = self.cursor.rowcount
            return filas_afectadas
        
        except pyodbc.Error as e:
            print("Error ejecutando la consulta: ", e)
            return 0
    
    def get_id(self, tabla: str):
        try:
            query = f"SELECT ISNULL( MAX(id), 0 ) + 1 FROM {tabla}"
            self.cursor.execute(query)
            fila = self.cursor.fetchone()

            return fila[0] if fila else 1
            
        except pyodbc.Error as e:
            print("Error obteniendo el id: ", e)
            return None
        
    def __del__(self):
        self.cursor.close()
        self.conexion.close()
