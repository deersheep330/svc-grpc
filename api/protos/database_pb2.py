# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/protos/database.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/protos/database.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x61pi/protos/database.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x18\n\x06Symbol\x12\x0e\n\x06symbol\x18\x01 \x01(\t\"%\n\x05Stock\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1c\n\x08RowCount\x12\x10\n\x08rowcount\x18\x01 \x01(\r\":\n\x14TrendWithDefaultDate\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x12\n\npopularity\x18\x02 \x01(\r\"Z\n\x0c\x42oughtOrSold\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12(\n\x04\x64\x61te\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x32\xc0\x03\n\x08\x44\x61tabase\x12.\n\nget_stocks\x12\x16.google.protobuf.Empty\x1a\x06.Stock0\x01\x12\x1c\n\tget_stock\x12\x07.Symbol\x1a\x06.Stock\x12$\n\rupsert_stocks\x12\x06.Stock\x1a\t.RowCount(\x01\x12\x34\n\x10insert_ptt_trend\x12\x15.TrendWithDefaultDate\x1a\t.RowCount\x12\x38\n\x14insert_reunion_trend\x12\x15.TrendWithDefaultDate\x1a\t.RowCount\x12\x33\n\x17insert_twse_over_bought\x12\r.BoughtOrSold\x1a\t.RowCount\x12\x31\n\x15insert_twse_over_sold\x12\r.BoughtOrSold\x1a\t.RowCount\x12\x34\n\x18insert_fugle_over_bought\x12\r.BoughtOrSold\x1a\t.RowCount\x12\x32\n\x16insert_fugle_over_sold\x12\r.BoughtOrSold\x1a\t.RowCountb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SYMBOL = _descriptor.Descriptor(
  name='Symbol',
  full_name='Symbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='Symbol.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=115,
)


_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='Stock.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Stock.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=117,
  serialized_end=154,
)


_ROWCOUNT = _descriptor.Descriptor(
  name='RowCount',
  full_name='RowCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rowcount', full_name='RowCount.rowcount', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=156,
  serialized_end=184,
)


_TRENDWITHDEFAULTDATE = _descriptor.Descriptor(
  name='TrendWithDefaultDate',
  full_name='TrendWithDefaultDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='TrendWithDefaultDate.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='popularity', full_name='TrendWithDefaultDate.popularity', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=186,
  serialized_end=244,
)


_BOUGHTORSOLD = _descriptor.Descriptor(
  name='BoughtOrSold',
  full_name='BoughtOrSold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='BoughtOrSold.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='BoughtOrSold.date', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='BoughtOrSold.quantity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=246,
  serialized_end=336,
)

_BOUGHTORSOLD.fields_by_name['date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Symbol'] = _SYMBOL
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['RowCount'] = _ROWCOUNT
DESCRIPTOR.message_types_by_name['TrendWithDefaultDate'] = _TRENDWITHDEFAULTDATE
DESCRIPTOR.message_types_by_name['BoughtOrSold'] = _BOUGHTORSOLD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Symbol = _reflection.GeneratedProtocolMessageType('Symbol', (_message.Message,), {
  'DESCRIPTOR' : _SYMBOL,
  '__module__' : 'api.protos.database_pb2'
  # @@protoc_insertion_point(class_scope:Symbol)
  })
_sym_db.RegisterMessage(Symbol)

Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), {
  'DESCRIPTOR' : _STOCK,
  '__module__' : 'api.protos.database_pb2'
  # @@protoc_insertion_point(class_scope:Stock)
  })
_sym_db.RegisterMessage(Stock)

RowCount = _reflection.GeneratedProtocolMessageType('RowCount', (_message.Message,), {
  'DESCRIPTOR' : _ROWCOUNT,
  '__module__' : 'api.protos.database_pb2'
  # @@protoc_insertion_point(class_scope:RowCount)
  })
_sym_db.RegisterMessage(RowCount)

TrendWithDefaultDate = _reflection.GeneratedProtocolMessageType('TrendWithDefaultDate', (_message.Message,), {
  'DESCRIPTOR' : _TRENDWITHDEFAULTDATE,
  '__module__' : 'api.protos.database_pb2'
  # @@protoc_insertion_point(class_scope:TrendWithDefaultDate)
  })
_sym_db.RegisterMessage(TrendWithDefaultDate)

BoughtOrSold = _reflection.GeneratedProtocolMessageType('BoughtOrSold', (_message.Message,), {
  'DESCRIPTOR' : _BOUGHTORSOLD,
  '__module__' : 'api.protos.database_pb2'
  # @@protoc_insertion_point(class_scope:BoughtOrSold)
  })
_sym_db.RegisterMessage(BoughtOrSold)



_DATABASE = _descriptor.ServiceDescriptor(
  name='Database',
  full_name='Database',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=339,
  serialized_end=787,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_stocks',
    full_name='Database.get_stocks',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_STOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_stock',
    full_name='Database.get_stock',
    index=1,
    containing_service=None,
    input_type=_SYMBOL,
    output_type=_STOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='upsert_stocks',
    full_name='Database.upsert_stocks',
    index=2,
    containing_service=None,
    input_type=_STOCK,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_ptt_trend',
    full_name='Database.insert_ptt_trend',
    index=3,
    containing_service=None,
    input_type=_TRENDWITHDEFAULTDATE,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_reunion_trend',
    full_name='Database.insert_reunion_trend',
    index=4,
    containing_service=None,
    input_type=_TRENDWITHDEFAULTDATE,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_twse_over_bought',
    full_name='Database.insert_twse_over_bought',
    index=5,
    containing_service=None,
    input_type=_BOUGHTORSOLD,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_twse_over_sold',
    full_name='Database.insert_twse_over_sold',
    index=6,
    containing_service=None,
    input_type=_BOUGHTORSOLD,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_fugle_over_bought',
    full_name='Database.insert_fugle_over_bought',
    index=7,
    containing_service=None,
    input_type=_BOUGHTORSOLD,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='insert_fugle_over_sold',
    full_name='Database.insert_fugle_over_sold',
    index=8,
    containing_service=None,
    input_type=_BOUGHTORSOLD,
    output_type=_ROWCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASE)

DESCRIPTOR.services_by_name['Database'] = _DATABASE

# @@protoc_insertion_point(module_scope)
