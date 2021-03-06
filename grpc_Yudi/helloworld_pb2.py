#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10helloworld.proto\"\x17\n\x07Request\x12\x0c\n\x04\x64\x65sc\x18\x01 \x01(\t\")\n\x07\x43ontato\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x10\n\x08telefone\x18\x02 \x01(\t\"\x17\n\x07\x42oleano\x12\x0c\n\x04\x66lag\x18\x01 \x01(\t2\x85\x01\n\x07Greeter\x12(\n\x10\x41\x64icionarContato\x12\x08.Contato\x1a\x08.Boleano\"\x00\x12&\n\x0eRemoverContato\x12\x08.Contato\x1a\x08.Boleano\"\x00\x12(\n\x0eListarContatos\x12\x08.Request\x1a\x08.Contato\"\x00\x30\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desc', full_name='Request.desc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=43,
)


_CONTATO = _descriptor.Descriptor(
  name='Contato',
  full_name='Contato',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nome', full_name='Contato.nome', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='telefone', full_name='Contato.telefone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=86,
)


_BOLEANO = _descriptor.Descriptor(
  name='Boleano',
  full_name='Boleano',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='Boleano.flag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Contato'] = _CONTATO
DESCRIPTOR.message_types_by_name['Boleano'] = _BOLEANO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Contato = _reflection.GeneratedProtocolMessageType('Contato', (_message.Message,), dict(
  DESCRIPTOR = _CONTATO,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:Contato)
  ))
_sym_db.RegisterMessage(Contato)

Boleano = _reflection.GeneratedProtocolMessageType('Boleano', (_message.Message,), dict(
  DESCRIPTOR = _BOLEANO,
  __module__ = 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:Boleano)
  ))
_sym_db.RegisterMessage(Boleano)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=114,
  serialized_end=247,
  methods=[
  _descriptor.MethodDescriptor(
    name='AdicionarContato',
    full_name='Greeter.AdicionarContato',
    index=0,
    containing_service=None,
    input_type=_CONTATO,
    output_type=_BOLEANO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoverContato',
    full_name='Greeter.RemoverContato',
    index=1,
    containing_service=None,
    input_type=_CONTATO,
    output_type=_BOLEANO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListarContatos',
    full_name='Greeter.ListarContatos',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CONTATO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
