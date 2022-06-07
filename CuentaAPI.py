from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.cliente import Cliente
from models.cuenta import Cuenta
from bd import Repositorio
import json
from fastapi.encoders import jsonable_encoder

app = FastAPI()

posts = []
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

@app.get("/clientes/morosos", operation_id="clientes_morosos",
    summary="Listado de cliente morosos",
    description="Listado de clientes morosos del ultimo mes correspondiente a la cartera rodados"
)
def cliente_morosos():
    return ["Carlos", "Felipe", "Manuel"]

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
def delete_cliente(id:int):
    for cliente in  Cliente:
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted succesfully"}
    
    raise HTTPException(status_code=404, detail="Código 404 Bad Request")

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