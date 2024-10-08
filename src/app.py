from flask import Flask, jsonify, request
from service.Conector import Conector

app = Flask(__name__)
conector = Conector()


@app.route( '/productos', methods = [ 'GET' ] )
def index():
    data = conector.execute_query( "select * from producto" )
    return jsonify( data )


@app.route( '/productos/<int:id>', methods = [ 'GET' ] )
def getById( id ):
    data = conector.execute_query( "select * from producto where id = %s", ( id, ) )
    return jsonify( data )


@app.route( '/productos', methods = [ 'POST' ] )
def crear_producto():
    nuevo_producto = request.json
    nombre = nuevo_producto['nombre']
    descripcion = nuevo_producto['descripcion']
    precio = nuevo_producto['precio']
    id = conector.get_id( 'producto' )
    print( nuevo_producto )
    print( id )

    filas_afectadas = conector.execute_non_query( "INSERT INTO producto (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)", (id, nombre, descripcion, precio) )

    return jsonify( { "filas_afectadas": filas_afectadas } )


@app.route( '/productos/<int:id>', methods = [ 'PUT' ] )
def actualizar_producto( id ):
    producto_actualizado = request.json
    nombre = producto_actualizado['nombre']
    descripcion = producto_actualizado['descripcion']
    precio = producto_actualizado['precio']
    
    filas_afectadas = conector.execute_non_query("UPDATE producto SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s", (nombre, descripcion, precio, id))
    
    return jsonify( { "filas_afectadas": filas_afectadas } )


@app.route( '/productos/<int:id>', methods = [ 'DELETE' ] )
def eliminar_producto( id ):
    filas_afectadas = conector.execute_non_query("DELETE FROM producto WHERE id = %s", ( id, ))
    
    return jsonify( { "filas_afectadas": filas_afectadas } )


if __name__ == '__main__':
    app.run(debug=True)
