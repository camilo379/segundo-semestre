ListaUsuarios = []
ListaContraseñas = []
CuentaCorriente = []
CuentaAhorro = []
DineroASacar = []
class Login():
    def login(self):
        usuario = input("Digite su usuario <<< ")
        if usuario in ListaUsuarios:
            print("Usuario encontrado >>> ")
            contraseña = int(input("Digite su contraseña <<< "))
            if contraseña in ListaContraseñas:
                print("Inicio exitoso >>> ")
                print("Redireccionando a el menu principal >>> ")
            else:
                print("Contraseña Incorrecta >>> ")
        else:
            print("Usuario Incorrecto o no registrado >>> ")
            print("Regresando a el menu principal >>> ")
class Registro:
    def registro(self):
        self.usuarios = input("Digite su nombre de usuario <<< ")
        if self.usuarios in (ListaUsuarios):
            print("Usuario no disponible >>> ")
            self.registro()
        else:
            self.contraseñas = int(input("Digite su contraseña <<< "))
            print("Registrado con exito >>> ")
            ListaUsuarios.append(self.usuarios)
            ListaContraseñas.append(self.contraseñas)
            self.__init__()
class Inicio(Registro,Login):
    def __init__(self):
        print("1 = Inicio >>> ")
        print("2 = Iniciar >>> ")
        print("3 = Cerrar >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            super(Inicio,self).login()
        if desicion == 2:
            super(Inicio,self).registro()
        if desicion == 3:
            exit()
class Main(Inicio):
    def __init__(self):
        super().__init__()
        self.Menu()
    def Menu(self):
        print("1 = Crear cuenta >>> ")
        print("2 = Administrar cuentas")
        print("3 = Salir >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            self.CrearCuenta()
        if desicion == 2:
            self.AdministrarCuenta()
        if desicion == 3:
            self.__init__()
            CuentaAhorro.clear
            CuentaCorriente.clear
    def CrearCuenta(self):
        print("Actualmente solo manejamos 2 tipos de cuentas >>> ")
        print("1 = Cuenta corriente >>> ")
        print("2 = Cuenta de ahorros >>> ")
        desicion = int(input("Digite el tipo de cuenta a crear <<< "))
        if desicion == 1:
            print("Cuenta corriente creada >>> ")
            saldo = float(input("Digite el valor de el primer deposito <<< "))
            CuentaCorriente.append(saldo)
            print("Depositado con exito >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu()
        elif desicion == 2:
            print("Cuenta de ahorros creada >>> ")
            saldo = float(input("Digite el valor de el primer deposito <<< "))
            CuentaAhorro.append(saldo)
            print("Depositado con exito >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu()
        else:
            print("Error >>> ")
            print("Regresando a el menu principal... >>> ")
            self.Menu()
    def MostrarCuenta(self):
        print("1 = Cuenta corriente >>> ")
        print("2 = Cuenta de ahorros >>> ")
        desicion = int(input("Digite una opcion >>> "))
        if desicion == 1:
            print("El saldo total de su cuenta de ahorro es de : $ ",sum(CuentaCorriente))
        elif desicion == 2:
            print("El saldo total de su cuenta corriente es de : $ ",sum(CuentaAhorro))
        else:
            print("Error >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu
    def AdministrarCuenta(self):
        print("1 = Depositar dinero")
        print("2 = Ver saldo")
        print("3 = Retirar saldo")
        print("4 = Regresar")
        desicion = int(input("Digite su desicion"))
        if desicion == 1:
            print("1 = Cuenta corriente")
            print("2 = Cuenta de ahorros")
            desicion = int(input("Seleccione la cuenta"))
            if desicion == 1:
                saldo = float(input("Digite el valor de el deposito <<< "))
                CuentaCorriente.append(saldo)
                self.Menu()
            elif desicion == 2:
                saldo = float(input("Digite el valor de el deposito <<< "))
                CuentaAhorro.append(saldo)
                self.Menu()
            else:
                print("Error >>> ")
                print("Regresando a el menu principal >>> ")
                self.Menu()
        if desicion == 2:
            print("1 = Cuenta de ahorros >>> ")
            print("2 = Cuenta corriente >>> ")
            desicion = int(input("Digite una opcion >>> "))
            if desicion == 1:
                print("El saldo total de su cuenta de ahorro es de : $ ",sum(CuentaAhorro))
                self.Menu()
            elif desicion == 2:
                print("El saldo total de su cuenta corriente es de : $ ",sum(CuentaCorriente))
                self.Menu()
            else:
                print("Error >>> ")
                print("Regresando a el menu principal >>> ")
                self.Menu()
        if desicion == 3:
            print("1 = Cuenta corriente >>> ")
            print("2 = Cuenta de ahorros >>> ")
            desicion = int(input("Digite su desicion <<< "))
            """if desicion == 1:
                salida = float(input("Digite el monto a retirar >>> "))
                DineroASacar.append(salida)
                dinerorestante = dinerorestante-CuentaCorriente
                print(dinerorestante)
                DineroASacar.clear
            if desicion == 2:
                salida = float(input("Digite el monto a retirar >>> "))
                DineroASacar.append(salida)
                dinerorestante = dinerorestante-CuentaAhorro
                print(dinerorestante)
                DineroASacar.clear"""
        if desicion == 4:
            print("Regresando a el menu principal >>> ")
            self.Menu()
ListaUsuarios = []
ListaContraseñas = []
CuentaCorriente = []
CuentaAhorro = []
class Login():
    def login(self):
        usuario = input("Digite su usuario <<< ")
        if usuario in ListaUsuarios:
            print("Usuario encontrado >>> ")
            contraseña = int(input("Digite su contraseña <<< "))
            if contraseña in ListaContraseñas:
                print("Inicio exitoso >>> ")
                print("Redireccionando a el menu principal >>> ")
            else:
                print("Contraseña Incorrecta >>> ")
                self.login()
        else:
            print("Usuario Incorrecto o no registrado >>> ")
            print("Regresando a el menu principal >>> ")
            self.login()
class Registro:
    def registro(self):
        self.usuarios = input("Digite su nombre de usuario <<< ")
        if self.usuarios in (ListaUsuarios):
            print("Usuario no disponible >>> ")
            self.registro()
        else:
            self.contraseñas = int(input("Digite su contraseña <<< "))
            print("Registrado con exito >>> ")
            ListaUsuarios.append(self.usuarios)
            ListaContraseñas.append(self.contraseñas)
            self.__init__()
class Inicio(Registro,Login):
    def __init__(self):
        print("1 = Iniciar >>> ")
        print("2 = Registro >>> ")
        print("3 = Cerrar >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            super(Inicio,self).login()
        if desicion == 2:
            super(Inicio,self).registro()
        if desicion == 3:
            exit()
class Main(Inicio):
    def __init__(self):
        super().__init__()
        self.Menu()
    def Menu(self):
        print("1 = Crear cuenta >>> ")
        print("2 = Administrar cuentas >>>")
        print("3 = Salir >>> ")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            self.CrearCuenta()
        if desicion == 2:
            self.AdministrarCuenta()
        if desicion == 3:
            self.__init__()
            CuentaAhorro.clear()
            CuentaCorriente.clear()
    def CrearCuenta(self):
        print("Actualmente solo manejamos 2 tipos de cuentas >>> ")
        print("1 = Cuenta corriente >>> ")
        print("2 = Cuenta de ahorros >>> ")
        desicion = int(input("Digite el tipo de cuenta a crear <<< "))
        if desicion == 1:
            print("Cuenta corriente creada >>> ")
            saldo = float(input("Digite el valor de el primer deposito <<< "))
            CuentaCorriente.append(saldo)
            print("Depositado con exito >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu()
        elif desicion == 2:
            print("Cuenta de ahorros creada >>> ")
            saldo = float(input("Digite el valor de el primer deposito <<< "))
            CuentaAhorro.append(saldo)
            print("Depositado con exito >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu()
        else:
            print("Error >>> ")
            print("Regresando a el menu principal... >>> ")
            self.Menu()
    def MostrarCuenta(self):
        print("1 = Cuenta corriente >>> ")
        print("2 = Cuenta de ahorros >>> ")
        desicion = int(input("Digite una opcion >>> "))
        if desicion == 1:
            print("El saldo total de su cuenta de ahorro es de : $ ",sum(CuentaCorriente))
        elif desicion == 2:
            print("El saldo total de su cuenta corriente es de : $ ",sum(CuentaAhorro))
        else:
            print("Error >>> ")
            print("Regresando a el menu principal >>> ")
            self.Menu
    def AdministrarCuenta(self):
        print("1 = Depositar dinero >>> ")
        print("2 = Ver saldo >>> ")
        print("3 = Retirar saldo >>> ")
        print("4 = Regresar")
        desicion = int(input("Digite su desicion <<< "))
        if desicion == 1:
            print("1 = Cuenta corriente >>> ")
            print("2 = Cuenta de ahorros >>> ")
            desicion = int(input("Seleccione la cuenta <<< "))
            if desicion == 1:
                saldo = float(input("Digite el valor de el deposito <<< "))
                CuentaCorriente.append(saldo)
                self.Menu()
            elif desicion == 2:
                saldo = float(input("Digite el valor de el deposito <<< "))
                CuentaAhorro.append(saldo)
                self.Menu()
            else:
                print("Error >>> ")
                print("Regresando a el menu principal >>> ")
                self.Menu()
        if desicion == 2:
            print("1 = Cuenta de ahorros >>> ")
            print("2 = Cuenta corriente >>> ")
            desicion = int(input("Digite una opcion >>> "))
            if desicion == 1:
                print("El saldo total de su cuenta de ahorro es de : $ ",sum(CuentaAhorro))
                self.Menu()
            elif desicion == 2:
                print("El saldo total de su cuenta corriente es de : $ ",sum(CuentaCorriente))
                self.Menu()
            else:
                print("Error >>> ")
                print("Regresando a el menu principal >>> ")
                self.Menu()
        if desicion == 3:
            TotalCuentaAhorro = sum(CuentaAhorro)
            TotalCuentaCorriente = sum(CuentaCorriente)
            print("1 = Cuenta de ahorros >>> ")
            print("2 = Cuenta corriente >>> ")
            seleccion = int(input("Digite una opcion <<< "))
            if seleccion == 1:
                print("Cuenta de Ahorros seleccionada >>> ")
                print("Saldo actual : ",CuentaAhorro)
                dinerosaliente = int(input("Digite la cantidad de dinero a retirar <<< "))
                if dinerosaliente < TotalCuentaAhorro:
                    print("Retiro realizado con exito >>> ")
                    DineroRestante = dinerosaliente - TotalCuentaAhorro
                    CuentaAhorro.clear()
                    CuentaAhorro.append(DineroRestante)
                    print("Su nuevo saldo es de : ", CuentaAhorro)
                    print("Regresando a el menu principal >>> ")
                    self.Menu()
                if dinerosaliente > TotalCuentaAhorro:
                    print("Error... >>> ")
                    print("Dinero insuficiente >>> ")
                    self.Menu()
            if seleccion == 2:
                print("Cuenta corriente seleccionada >>> ")
                print("Saldo actual : ",CuentaCorriente)
                dinerosaliente = int(input("Digite la cantidad de dinero a retirar <<< "))
                if dinerosaliente < TotalCuentaCorriente:
                    print("Retiro realizado con exito >>> ")
                    DineroRestante = dinerosaliente - TotalCuentaCorriente
                    CuentaCorriente.clear()
                    CuentaCorriente.append(DineroRestante)
                    print("Su nuevo saldo es de : ", CuentaCorriente)
                    print("Regresando a el menu principal >>> ")
                    self.Menu()
                if dinerosaliente > TotalCuentaCorriente:
                    print("Error... >>> ")
                    print("Dinero insuficiente >>> ")
                    self.Menu()
        if desicion == 4:
            print("Regresando a el menu principal >>> ")
            self.Menu()
Main()