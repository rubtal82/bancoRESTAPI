from typing import Union
from models.cliente import Cliente
from models.cuenta import Cuenta


class Repositorio:

    clienteTabla : dict[int, Cliente] = {}
    id = 0

    @classmethod
    def insertarCliente(cls, cliente:Cliente):
        cls.id =  cls.id +1 
        cliente.id = cls.id 
        cls.clienteTabla[cls.id] = cliente

    @classmethod
    def recuperar_clientes(cls):
        return cls.clienteTabla.values()

    @classmethod
    def recuperar_cliente(cls, id:int):
        return cls.clienteTabla[id]

    @classmethod
    def delete_cliente(cls, id:int):
        return cls.clienteTabla[id]

    @classmethod
    def update_cliente(cls, id:int):
        return cls.clienteTabla[id]


    cuentaTabla : dict[int, Cuenta] = {}
    id = 0

    @classmethod
    def insertarCuenta(cls, cuenta:Cuenta):
        cls.id =  cls.id +1 
        cuenta.id = cls.id 
        cls.cuentaTabla[cls.id] = cuenta

    @classmethod
    def recuperar_cuentas(cls):
        return cls.cuentaTabla.values()

    @classmethod
    def recuperar_cuenta(cls, id:int):
        return cls.cuentaTabla[id]

    @classmethod
    def delete_cuenta(cls, id:int):
        return cls.cuentaTabla[id]