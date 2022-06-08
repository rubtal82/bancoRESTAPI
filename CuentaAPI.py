from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.cliente import Cliente
from models.cuenta import Cuenta
from bd import Repositorio
import json
from fastapi.encoders import jsonable_encoder

app = FastAPI()

#Recursos
# 1 - Cliente
# Registrar - POST /clientes
# listar - GET /clientes
# consultar- GET /clientes/{pk} 
# actualizar- PUT /clientes/{pk}
# eliminar - DELETE /clientes/{pk}

# 2 - Pago 
# - POST /pagos
# - GET /pagos
# - GET /pagos/{pk} 
# - PUT /pagos/{pk}
# - DELETE /pagos/{pk}

@app.get('/')
def read_root():
    return {"Bienvenidos a Telefonia RT"}

@app.post("/clientes", operation_id="registar_cliente")
def registar_cliente(cliente: Cliente):
    Repositorio.insertarCliente(cliente)
    return cliente

@app.get("/clientes")
def recuperar_clientes():
    registros: dict[int, Cliente]= Repositorio.recuperar_clientes()
    listObjetos =  list(registros) #lista DE objetos CLIENTES 
    listaJson = jsonable_encoder(listObjetos) #convertimos lista de objetos a json

    return listaJson


@app.get("/clientes/{id}")
def recuperar_cliente(id:int):
    cliente: Cliente= Repositorio.recuperar_cliente(id)
    return cliente


@app.delete('/clientes/{id}')
def delete_cliente(id: int):
    for index, Cliente in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")
    
@app.put('/clientes/{id}')
def update_cliente(id:int, updatedPost: Cliente):
    for index, Cliente in enumerate(posts):
        if Cliente["id"] == id:
            posts[index]["cedula"]= updatedPost.dict()["cedula"]
            posts[index]["nombre"]= updatedPost.dict()["nombre"]
            posts[index]["apellido"]= updatedPost.dict()["apellido"]
            posts[index]["cuenta_debito"]= updatedPost.dict()["cuenta_debito"]
            return {"message": "Post has been updated succesfully"}
    raise HTTPException(status_code=404, detail="Código 404 Bad Request")



@app.post("/cuenta", operation_id="registar_cuenta")
def registar_cuenta(cuenta: Cuenta):
    Repositorio.insertarCuenta(cuenta)
    return cuenta

@app.get("/cuenta")
def recuperar_cuenta():
    registros: dict[int, Cuenta]= Repositorio.recuperar_cuenta()
    listObjetos =  list(registros) #lista DE objetos CLIENTES 
    listaJson = jsonable_encoder(listObjetos) #convertimos lista de objetos a json

    return listaJson


@app.get("/cuenta/{id}")
def recuperar_cuenta(id:int):
    cuenta: Cuenta= Repositorio.recuperar_cuenta(id)
    return cuenta

@app.delete('/cuenta/{id}')
def delete_cuenta(id: int):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")