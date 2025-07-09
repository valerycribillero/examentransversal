def stock_marca(marca, productos, stock):
    total = 0
    marca = marca.lower()
    for id_, datos in productos.items():
        if datos[0].lower() == marca:
            total += stock[id_]["stock"]
    print(f"El stock total para {marca.capitalize()} es: {total}")

def busqueda_precio(p_min, p_max, productos, stock):
    resultado = []
    for id_, datos in productos.items():
        if id_ in stock:
            precio = stock[id_]["precio"]
            cantidad = stock[id_]["stock"]
            if p_min <= precio <= p_max and cantidad > 0:
                info_completa = [id_] + datos + [f"${precio}", f"stock: {cantidad}"]
                resultado.append(info_completa)
    if resultado:
        print("\nLos productos dentro del rango de precio son:")
        for producto in resultado:
            print(" - ", producto)
    else:
        print("No hay notebooks en ese rango de precio.")


def actualizar_precio(id_, precio, stock):
    if id_ in stock:
        stock[id_]["precio"] = precio
        return True
    else:
        return False
