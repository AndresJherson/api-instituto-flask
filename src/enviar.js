const dataTrabajoFinal = {
    dni: "87547814",
    nombre: "Ulises",
    apellido: "Lizandor",
    direccion: "confixcell",
    celular: 51987458154,
    pedidos: [
        {
            nombre: 'pantalla',
            cantidad: 6
        },
        {
            nombre: 'laptop',
            cantidad: 2
        },
    ]
};

const dataTrabajo2 = {
    nombre: "cambo 10kg",
    descripcion: "comida de alta calidad para perros",
    precio: 20.50
}


fetch( "http://localhost:5000/productos/11", {
    method: 'DELETE',
    // headers: {
    //     'Content-Type': 'application/json',
    // },
    // body: JSON.stringify( dataTrabajo2 )
} )
.then( res => res.json().then( data => console.log( data ) ).catch( error => console.log( error ) ) )
.catch( err => console.log( err ) );