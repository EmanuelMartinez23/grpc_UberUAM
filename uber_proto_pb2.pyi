from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Posicion(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class InfoResponse(_message.Message):
    __slots__ = ("disponible", "coordenadas", "uber", "tarifa", "placas")
    DISPONIBLE_FIELD_NUMBER: _ClassVar[int]
    COORDENADAS_FIELD_NUMBER: _ClassVar[int]
    UBER_FIELD_NUMBER: _ClassVar[int]
    TARIFA_FIELD_NUMBER: _ClassVar[int]
    PLACAS_FIELD_NUMBER: _ClassVar[int]
    disponible: bool
    coordenadas: Posicion
    uber: str
    tarifa: int
    placas: str
    def __init__(self, disponible: bool = ..., coordenadas: _Optional[_Union[Posicion, _Mapping]] = ..., uber: _Optional[str] = ..., tarifa: _Optional[int] = ..., placas: _Optional[str] = ...) -> None: ...

class TerminarViajeRequest(_message.Message):
    __slots__ = ("posicion_final", "placas", "costo_viaje")
    POSICION_FINAL_FIELD_NUMBER: _ClassVar[int]
    PLACAS_FIELD_NUMBER: _ClassVar[int]
    COSTO_VIAJE_FIELD_NUMBER: _ClassVar[int]
    posicion_final: Posicion
    placas: str
    costo_viaje: int
    def __init__(self, posicion_final: _Optional[_Union[Posicion, _Mapping]] = ..., placas: _Optional[str] = ..., costo_viaje: _Optional[int] = ...) -> None: ...

class TerminarViajeResponse(_message.Message):
    __slots__ = ("exito",)
    EXITO_FIELD_NUMBER: _ClassVar[int]
    exito: bool
    def __init__(self, exito: bool = ...) -> None: ...

class EstadoServicioResponse(_message.Message):
    __slots__ = ("viajes_realizados", "autos_libres", "ganancia_total")
    VIAJES_REALIZADOS_FIELD_NUMBER: _ClassVar[int]
    AUTOS_LIBRES_FIELD_NUMBER: _ClassVar[int]
    GANANCIA_TOTAL_FIELD_NUMBER: _ClassVar[int]
    viajes_realizados: int
    autos_libres: int
    ganancia_total: int
    def __init__(self, viajes_realizados: _Optional[int] = ..., autos_libres: _Optional[int] = ..., ganancia_total: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
