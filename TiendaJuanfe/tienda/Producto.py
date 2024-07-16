


categorias = {}
productos = {}

def crear_categoria():
    id = int(input("Id"))
    nombre_cat = input("Nombre Categoria")
    categorias[id] = nombre_cat

def crear_producto():
    id = int(input("Id Producto"))
    nombre_prod = input("Nombre producto")
    precio = float(input("Precio"))
    cantidad = int(input("Cantidad"))
    categoria = buscar_categoria()
    productos[id] = nombre_prod, precio, cantidad , categoria


def buscar_categoria():
    listar_categorias()
    id = int(input("Seleccione una categoria"))
    categoria = categorias.get(id)
    return categoria

def listar_categorias():
    for cat in categorias.items():
        print(cat)


def listar_productos():
    for producto in productos.items():
        print(producto)


crear_categoria()
crear_categoria()
crear_producto()
listar_productos()