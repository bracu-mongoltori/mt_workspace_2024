# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stop_live_stream.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stop_live_stream.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16stop_live_stream.proto\x12\x11insta360.messages\"\x10\n\x0eStopLiveStream\"\x14\n\x12StopLiveStreamRespB\x08\xa2\x02\x05INSPBb\x06proto3'
)




_STOPLIVESTREAM = _descriptor.Descriptor(
  name='StopLiveStream',
  full_name='insta360.messages.StopLiveStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=45,
  serialized_end=61,
)


_STOPLIVESTREAMRESP = _descriptor.Descriptor(
  name='StopLiveStreamResp',
  full_name='insta360.messages.StopLiveStreamResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=63,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['StopLiveStream'] = _STOPLIVESTREAM
DESCRIPTOR.message_types_by_name['StopLiveStreamResp'] = _STOPLIVESTREAMRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopLiveStream = _reflection.GeneratedProtocolMessageType('StopLiveStream', (_message.Message,), {
  'DESCRIPTOR' : _STOPLIVESTREAM,
  '__module__' : 'stop_live_stream_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopLiveStream)
  })
_sym_db.RegisterMessage(StopLiveStream)

StopLiveStreamResp = _reflection.GeneratedProtocolMessageType('StopLiveStreamResp', (_message.Message,), {
  'DESCRIPTOR' : _STOPLIVESTREAMRESP,
  '__module__' : 'stop_live_stream_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.StopLiveStreamResp)
  })
_sym_db.RegisterMessage(StopLiveStreamResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
