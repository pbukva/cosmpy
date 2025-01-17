# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/connection/v1/connection.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ibc/core/connection/v1/connection.proto',
  package='ibc.core.connection.v1',
  syntax='proto3',
  serialized_options=b'Z;github.com/cosmos/cosmos-sdk/x/ibc/core/03-connection/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'ibc/core/connection/v1/connection.proto\x12\x16ibc.core.connection.v1\x1a\x14gogoproto/gogo.proto\x1a\'ibc/core/commitment/v1/commitment.proto\"\x90\x02\n\rConnectionEnd\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12\x31\n\x08versions\x18\x02 \x03(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12,\n\x05state\x18\x03 \x01(\x0e\x32\x1d.ibc.core.connection.v1.State\x12@\n\x0c\x63ounterparty\x18\x04 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12-\n\x0c\x64\x65lay_period\x18\x05 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\":\x04\x88\xa0\x1f\x00\"\xb2\x02\n\x14IdentifiedConnection\x12\x19\n\x02id\x18\x01 \x01(\tB\r\xf2\xde\x1f\tyaml:\"id\"\x12\'\n\tclient_id\x18\x02 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12\x31\n\x08versions\x18\x03 \x03(\x0b\x32\x1f.ibc.core.connection.v1.Version\x12,\n\x05state\x18\x04 \x01(\x0e\x32\x1d.ibc.core.connection.v1.State\x12@\n\x0c\x63ounterparty\x18\x05 \x01(\x0b\x32$.ibc.core.connection.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12-\n\x0c\x64\x65lay_period\x18\x06 \x01(\x04\x42\x17\xf2\xde\x1f\x13yaml:\"delay_period\":\x04\x88\xa0\x1f\x00\"\xaa\x01\n\x0c\x43ounterparty\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12/\n\rconnection_id\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:\"connection_id\"\x12:\n\x06prefix\x18\x03 \x01(\x0b\x32$.ibc.core.commitment.v1.MerklePrefixB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00\"\x1c\n\x0b\x43lientPaths\x12\r\n\x05paths\x18\x01 \x03(\t\"I\n\x0f\x43onnectionPaths\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"client_id\"\x12\r\n\x05paths\x18\x02 \x03(\t\"5\n\x07Version\x12\x12\n\nidentifier\x18\x01 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x02 \x03(\t:\x04\x88\xa0\x1f\x00*\x99\x01\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x1a\x04\x88\xa3\x1e\x00\x42=Z;github.com/cosmos/cosmos-sdk/x/ibc/core/03-connection/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2.DESCRIPTOR,])

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='ibc.core.connection.v1.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNINITIALIZED_UNSPECIFIED', index=0, number=0,
      serialized_options=b'\212\235 \rUNINITIALIZED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_INIT', index=1, number=1,
      serialized_options=b'\212\235 \004INIT',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_TRYOPEN', index=2, number=2,
      serialized_options=b'\212\235 \007TRYOPEN',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE_OPEN', index=3, number=3,
      serialized_options=b'\212\235 \004OPEN',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\210\243\036\000',
  serialized_start=1048,
  serialized_end=1201,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
STATE_UNINITIALIZED_UNSPECIFIED = 0
STATE_INIT = 1
STATE_TRYOPEN = 2
STATE_OPEN = 3



_CONNECTIONEND = _descriptor.Descriptor(
  name='ConnectionEnd',
  full_name='ibc.core.connection.v1.ConnectionEnd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.ConnectionEnd.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versions', full_name='ibc.core.connection.v1.ConnectionEnd.versions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='ibc.core.connection.v1.ConnectionEnd.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.connection.v1.ConnectionEnd.counterparty', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_period', full_name='ibc.core.connection.v1.ConnectionEnd.delay_period', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"delay_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=403,
)


_IDENTIFIEDCONNECTION = _descriptor.Descriptor(
  name='IdentifiedConnection',
  full_name='ibc.core.connection.v1.IdentifiedConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ibc.core.connection.v1.IdentifiedConnection.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\tyaml:\"id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.IdentifiedConnection.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versions', full_name='ibc.core.connection.v1.IdentifiedConnection.versions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='ibc.core.connection.v1.IdentifiedConnection.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='counterparty', full_name='ibc.core.connection.v1.IdentifiedConnection.counterparty', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_period', full_name='ibc.core.connection.v1.IdentifiedConnection.delay_period', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\023yaml:\"delay_period\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=712,
)


_COUNTERPARTY = _descriptor.Descriptor(
  name='Counterparty',
  full_name='ibc.core.connection.v1.Counterparty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.Counterparty.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='ibc.core.connection.v1.Counterparty.connection_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\024yaml:\"connection_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='ibc.core.connection.v1.Counterparty.prefix', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=885,
)


_CLIENTPATHS = _descriptor.Descriptor(
  name='ClientPaths',
  full_name='ibc.core.connection.v1.ClientPaths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='ibc.core.connection.v1.ClientPaths.paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=887,
  serialized_end=915,
)


_CONNECTIONPATHS = _descriptor.Descriptor(
  name='ConnectionPaths',
  full_name='ibc.core.connection.v1.ConnectionPaths',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ibc.core.connection.v1.ConnectionPaths.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\336\037\020yaml:\"client_id\"', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='ibc.core.connection.v1.ConnectionPaths.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=917,
  serialized_end=990,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='ibc.core.connection.v1.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='ibc.core.connection.v1.Version.identifier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='features', full_name='ibc.core.connection.v1.Version.features', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=992,
  serialized_end=1045,
)

_CONNECTIONEND.fields_by_name['versions'].message_type = _VERSION
_CONNECTIONEND.fields_by_name['state'].enum_type = _STATE
_CONNECTIONEND.fields_by_name['counterparty'].message_type = _COUNTERPARTY
_IDENTIFIEDCONNECTION.fields_by_name['versions'].message_type = _VERSION
_IDENTIFIEDCONNECTION.fields_by_name['state'].enum_type = _STATE
_IDENTIFIEDCONNECTION.fields_by_name['counterparty'].message_type = _COUNTERPARTY
_COUNTERPARTY.fields_by_name['prefix'].message_type = ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2._MERKLEPREFIX
DESCRIPTOR.message_types_by_name['ConnectionEnd'] = _CONNECTIONEND
DESCRIPTOR.message_types_by_name['IdentifiedConnection'] = _IDENTIFIEDCONNECTION
DESCRIPTOR.message_types_by_name['Counterparty'] = _COUNTERPARTY
DESCRIPTOR.message_types_by_name['ClientPaths'] = _CLIENTPATHS
DESCRIPTOR.message_types_by_name['ConnectionPaths'] = _CONNECTIONPATHS
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.enum_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectionEnd = _reflection.GeneratedProtocolMessageType('ConnectionEnd', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONEND,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.ConnectionEnd)
  })
_sym_db.RegisterMessage(ConnectionEnd)

IdentifiedConnection = _reflection.GeneratedProtocolMessageType('IdentifiedConnection', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIEDCONNECTION,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.IdentifiedConnection)
  })
_sym_db.RegisterMessage(IdentifiedConnection)

Counterparty = _reflection.GeneratedProtocolMessageType('Counterparty', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERPARTY,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.Counterparty)
  })
_sym_db.RegisterMessage(Counterparty)

ClientPaths = _reflection.GeneratedProtocolMessageType('ClientPaths', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTPATHS,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.ClientPaths)
  })
_sym_db.RegisterMessage(ClientPaths)

ConnectionPaths = _reflection.GeneratedProtocolMessageType('ConnectionPaths', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONPATHS,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.ConnectionPaths)
  })
_sym_db.RegisterMessage(ConnectionPaths)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'ibc.core.connection.v1.connection_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.connection.v1.Version)
  })
_sym_db.RegisterMessage(Version)


DESCRIPTOR._options = None
_STATE._options = None
_STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._options = None
_STATE.values_by_name["STATE_INIT"]._options = None
_STATE.values_by_name["STATE_TRYOPEN"]._options = None
_STATE.values_by_name["STATE_OPEN"]._options = None
_CONNECTIONEND.fields_by_name['client_id']._options = None
_CONNECTIONEND.fields_by_name['counterparty']._options = None
_CONNECTIONEND.fields_by_name['delay_period']._options = None
_CONNECTIONEND._options = None
_IDENTIFIEDCONNECTION.fields_by_name['id']._options = None
_IDENTIFIEDCONNECTION.fields_by_name['client_id']._options = None
_IDENTIFIEDCONNECTION.fields_by_name['counterparty']._options = None
_IDENTIFIEDCONNECTION.fields_by_name['delay_period']._options = None
_IDENTIFIEDCONNECTION._options = None
_COUNTERPARTY.fields_by_name['client_id']._options = None
_COUNTERPARTY.fields_by_name['connection_id']._options = None
_COUNTERPARTY.fields_by_name['prefix']._options = None
_COUNTERPARTY._options = None
_CONNECTIONPATHS.fields_by_name['client_id']._options = None
_VERSION._options = None
# @@protoc_insertion_point(module_scope)
