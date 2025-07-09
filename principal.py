#tienda online llamada Pybooks, vende notebooks
import libreria as lb
productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175hd": ["Lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8gb", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8gb", "DD", "1T", "Intel Core i7","Nvidia GTX1050"],
    "123FHD": ["Lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["Lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}
stock = {
    "8475HD": {"marca": "HP", "precio": 1500000, "stock": 15},
    "2175hd": {"marca": "Lenovo", "precio": 1000000, "stock": 10},
    "JjfFHD": {"marca": "Asus", "precio": 1650000, "stock": 12},
    "fgdxFHD": {"marca": "HP", "precio": 220000, "stock": 2},
    "GF75HD": {"marca": "Asus", "precio": 125000, "stock": 21},
    "123FHD": {"marca": "lenovo", "precio": 1920000, "stock": 13},
    "342FHD": {"marca": "lenovo", "precio": 2500000, "stock": 11},
    "UWU131HD": {"marca": "Dell", "precio": 330000, "stock": 27},
}

while True:
    print("╔════════════════════════════╗")
    print("║           Pybooks          ║")
    print("║----------------------------║")
    print("║       Menú Principal       ║")
    print("║----------------------------║")
    print("║1. Stock Marca              ║")
    print("║2. Busqueda por precio      ║")
    print("║3. Actualizar precio        ║")
    print("║4. Salir                    ║")
    print("╚════════════════════════════╝")
    op = input("Ingrese una opción (1-4): ")
    if op == "1":
        marca =  input("Ingrese marca a consultar: ")
        lb.stock_marca(marca, productos, stock)
    elif op == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except:
                print("No hay notbooks en ese rango de precios")
                continue
        lb.busqueda_precio(p_min, p_max, productos, stock)
    elif op == "3":
        while True:
            id_ = input("Ingrese Identificador del producto: ")
            if id_ not in stock:
                print("El modelo no existe")
                continue
            precio_actual = stock[id_]["precio"]
            print(f"Precio actual del producto {id_}: ${precio_actual}")
            try:
                precio_nuevo = int(input("Ingrese nuevo precio: "))
            except:
                print("Precio no válido")
                continue
            seguir = input("¿Desea actualizar el precio? (Si/No): ").lower()
            if seguir == "si":
                lb.actualizar_precio(id_, precio_nuevo, stock)
                print("Precio actualizado correctamente.")
            else:
                print("Actualización cancelada.")
            break

            
    elif op == "4":
        print("\nPrograma Finalizado")
    else:
        print("Debe seleccionar una opción válida")