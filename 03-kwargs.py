#keywords arguments 
def get_product(**datos):#cuando llamas una funcion y le ponemos ** debemos darle nombre al parametro

    print(datos["id"], datos["name"])

get_product(id="ami", 
            name="23",
            desc=" esto es un celular chulisimo")