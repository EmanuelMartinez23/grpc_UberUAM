# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: uber_proto.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'uber_proto.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10uber_proto.proto\x12\x03uam\" \n\x08Posicion\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\"t\n\x0cInfoResponse\x12\x12\n\ndisponible\x18\x01 \x01(\x08\x12\"\n\x0b\x63oordenadas\x18\x02 \x01(\x0b\x32\r.uam.Posicion\x12\x0c\n\x04uber\x18\x03 \x01(\t\x12\x0e\n\x06tarifa\x18\x04 \x01(\x05\x12\x0e\n\x06placas\x18\x05 \x01(\t\"b\n\x14TerminarViajeRequest\x12%\n\x0eposicion_final\x18\x01 \x01(\x0b\x32\r.uam.Posicion\x12\x0e\n\x06placas\x18\x02 \x01(\t\x12\x13\n\x0b\x63osto_viaje\x18\x03 \x01(\x05\"&\n\x15TerminarViajeResponse\x12\r\n\x05\x65xito\x18\x01 \x01(\x08\"a\n\x16\x45stadoServicioResponse\x12\x19\n\x11viajes_realizados\x18\x01 \x01(\x05\x12\x14\n\x0c\x61utos_libres\x18\x02 \x01(\x05\x12\x16\n\x0eganancia_total\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xf9\x01\n\x0eSolicitarViaje\x12.\n\x08InfoAuto\x12\r.uam.Posicion\x1a\x11.uam.InfoResponse\"\x00\x12H\n\rTerminarViaje\x12\x19.uam.TerminarViajeRequest\x1a\x1a.uam.TerminarViajeResponse\"\x00\x12;\n\x0e\x45stadoServicio\x12\n.uam.Empty\x1a\x1b.uam.EstadoServicioResponse\"\x00\x12\x30\n\x08SayHello\x12\x11.uam.HelloRequest\x1a\x0f.uam.HelloReply\"\x00\x42&\n\x11\x63om.grpc.uber.uamB\tUberProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'uber_proto_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.grpc.uber.uamB\tUberProtoP\001\242\002\003HLW'
  _globals['_POSICION']._serialized_start=25
  _globals['_POSICION']._serialized_end=57
  _globals['_INFORESPONSE']._serialized_start=59
  _globals['_INFORESPONSE']._serialized_end=175
  _globals['_TERMINARVIAJEREQUEST']._serialized_start=177
  _globals['_TERMINARVIAJEREQUEST']._serialized_end=275
  _globals['_TERMINARVIAJERESPONSE']._serialized_start=277
  _globals['_TERMINARVIAJERESPONSE']._serialized_end=315
  _globals['_ESTADOSERVICIORESPONSE']._serialized_start=317
  _globals['_ESTADOSERVICIORESPONSE']._serialized_end=414
  _globals['_EMPTY']._serialized_start=416
  _globals['_EMPTY']._serialized_end=423
  _globals['_HELLOREQUEST']._serialized_start=425
  _globals['_HELLOREQUEST']._serialized_end=453
  _globals['_HELLOREPLY']._serialized_start=455
  _globals['_HELLOREPLY']._serialized_end=484
  _globals['_SOLICITARVIAJE']._serialized_start=487
  _globals['_SOLICITARVIAJE']._serialized_end=736
# @@protoc_insertion_point(module_scope)
