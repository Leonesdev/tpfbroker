from services.usuario_service import UsuarioService
from services.inversion_service import InversionService

def main():
    usuario_service = UsuarioService()
    inversion_service = InversionService()
    
    while True:
        print("\nMenu:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Realizar inversión")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            # Lógica para registrar usuario
            nombre = input("Ingrese su nombre: ")
            email = input("Ingrese su email: ")
            usuario_service.registrar_usuario(nombre, email)
        elif opcion == '2':
            # Lógica para iniciar sesión
            email = input("Ingrese su email: ")
            usuario_service.iniciar_sesion(email)
        elif opcion == '3':
            # Lógica para realizar inversión
            monto = float(input("Ingrese el monto a invertir: "))
            inversion_service.realizar_inversion(monto)
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
