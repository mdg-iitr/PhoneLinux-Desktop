# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comProto.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='comProto.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x63omProto.proto\"\x87\x01\n\x0e\x63ommandMessage\x12\x0b\n\x03one\x18\x01 \x01(\t\x12\x0b\n\x03two\x18\x02 \x01(\t\x12\r\n\x05three\x18\x03 \x01(\t\x12\x0c\n\x04\x66our\x18\x04 \x01(\t\x12\x0c\n\x04\x66ive\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x12\x10\n\x08passcode\x18\x07 \x01(\t\x12\x12\n\ngetCommand\x18\x08 \x01(\t2B\n\x0e\x63ommandService\x12\x30\n\ntopCommand\x12\x0f.commandMessage\x1a\x0f.commandMessage\"\x00\x62\x06proto3'
)




_COMMANDMESSAGE = _descriptor.Descriptor(
  name='commandMessage',
  full_name='commandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='one', full_name='commandMessage.one', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='two', full_name='commandMessage.two', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='three', full_name='commandMessage.three', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='four', full_name='commandMessage.four', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='five', full_name='commandMessage.five', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='commandMessage.id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passcode', full_name='commandMessage.passcode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getCommand', full_name='commandMessage.getCommand', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['commandMessage'] = _COMMANDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

commandMessage = _reflection.GeneratedProtocolMessageType('commandMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDMESSAGE,
  '__module__' : 'comProto_pb2'
  # @@protoc_insertion_point(class_scope:commandMessage)
  })
_sym_db.RegisterMessage(commandMessage)



_COMMANDSERVICE = _descriptor.ServiceDescriptor(
  name='commandService',
  full_name='commandService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=156,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='topCommand',
    full_name='commandService.topCommand',
    index=0,
    containing_service=None,
    input_type=_COMMANDMESSAGE,
    output_type=_COMMANDMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDSERVICE)

DESCRIPTOR.services_by_name['commandService'] = _COMMANDSERVICE

# @@protoc_insertion_point(module_scope)
