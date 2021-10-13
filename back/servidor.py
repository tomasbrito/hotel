# ORM: Object Relational Map
from flask import Flask, request, Response
from flask import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime

Base = declarative_base()

class ToJson():
    def to_json(self):
        return json.dumps({col.name: getattr(self, col.name) for col in self.__table__.columns })


class Usuario(Base, ToJson):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    clave = Column(String)
    nombre = Column(String)
    celular = Column(String)
    email = Column(String)

class Reserva(Base, ToJson):
    __tablename__ = 'reserva'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    fechaEntrada = Column(String)
    fechaSalida = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(
        Usuario,
        backref=backref('reservas', uselist=True, cascade='delete,all')
    )

engine = create_engine('sqlite:///base_servido2.sqlite')

session = sessionmaker()
session.configure(bind=engine)

app = Flask(__name__) 

@app.route('/crearbase')
def crear_base():
    Base.metadata.create_all(engine)

    usuario = Usuario(nombre='admin', clave='admin')
    s = session()
    s.add(usuario)
    s.commit()

    return 'Ok'


@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    if not 'username' in request.form:
        return Response("Nombre de usuario no especificado", status=400)

    if not 'password' in request.form:
        return Response("Contraseña no especificada", status=400)

    username = request.form['username']
    password = request.form['password']

    s = session()
    d = s.query(Usuario).filter(Usuario.nombre==username).first()
    

    if d == None:
        return Response("Usuario/Contraseña incorrecto", status=400)
    elif d.clave != password:
        return Response("Usuario/Contraseña incorrecto", status=400)
    
    
    return Response(str(d.id),status=200, mimetype='application/json' )

@app.route('/registrar', methods=['POST'])
def registrar():
    if not 'username' in request.form:
        print('usuario no registradso')
        return Response("Nombre de usuario no especificado", status=400)

    if not 'password' in request.form:
        print('usuario no registraado')
        return Response("Contraseña no especificada", status=400)

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    celular = request.form['celular']
    s = session()
    d = s.query(Usuario).filter(Usuario.nombre==username).first()


    if d == None:
        usuario = Usuario(nombre=username, clave=password, email=email, celular=celular)
        s.add(usuario)
        s.commit()
        print('usuario registrado')
        return Response("Usuario registrado", status=200)
    else:
        return Response("Nombre de usuario ya utilizado", status=400)



@app.route('/reservar', methods=['POST'])
def reservar():
    if not 'tipo' in request.form:
        return Response("tipo no especificado", status=400)

    if not 'fechaEntrada' in request.form:
        return Response("fecha de entrada no especificada", status=400)

    if not 'fechaSalida' in request.form:
        return Response("fecha de salida no especificada", status=400)    


    if not 'id_usuario' in request.form:
        return Response("id usuario no encontrado", status=400)

    tipob = request.form['tipo']
    fechaEntradab = request.form['fechaEntrada']
    fechaSalidab = request.form['fechaSalida']
    iduser = request.form['id_usuario']
    reserva = Reserva(tipo=tipob,fechaEntrada=fechaEntradab,fechaSalida=fechaSalidab,usuario_id=iduser)
    s = session()
    s.add(reserva)
    s.commit()
    return 'ok'


@app.route('/hola')
def hola():
    print('hola')
    return'hola'

@app.route('/usuarios')
def list_usuarios():
    s = session()
    usuarios = s.query(Usuario)
    return Response(json.dumps([d.to_json() for d in usuarios]), status=200, mimetype='application/json')

@app.route('/reservas')
def list_reservas():
    s = session()
    reservas = s.query(Reserva)
    return Response(json.dumps([d.to_json() for d in reservas]), status=200, mimetype='application/json')


@app.route('/borrarUsuario/<id>', methods=['PUT', 'DELETE'])
def borrar_usuario(id):
    print(id)
    
    s = session()
    d = s.query(Usuario).filter(Usuario.id==id).first()
    if d != None:
        s.delete(d)
        s.commit()
        print('usuario eliminado')
        return Response("Usuario eliminado", status=200)
    
    return 'ok'

@app.route('/borrarReserva/<id>', methods=['PUT', 'DELETE'])
def borrar_reserva(id):
    print(id)
    
    s = session()
    d = s.query(Reserva).filter(Reserva.id==id).first()
    if d != None:
        s.delete(d)
        s.commit()
        print('Reserva eliminada')
        return Response("Reserva eliminada", status=200)
    
    return 'ok'

@app.route('/buscarUsuario/<id>')
def buscar_usuario(id):
    
    s = session()
    d = s.query(Usuario).filter(Usuario.id==id).first()

    if d != None:
        return Response(str(d.to_json()), status=200)
    
    return Response("No se encontro usuario",  status=404)

if __name__ == '__main__':
    app.run(port=9001)
