# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cancel_capture.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cancel_capture.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x63\x61ncel_capture.proto\x12\x11insta360.messages\"\x0f\n\rCancelCapture\"\x13\n\x11\x43\x61ncelCaptureRespB\x08\xa2\x02\x05INSPBb\x06proto3'
)




_CANCELCAPTURE = _descriptor.Descriptor(
  name='CancelCapture',
  full_name='insta360.messages.CancelCapture',
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
  serialized_start=43,
  serialized_end=58,
)


_CANCELCAPTURERESP = _descriptor.Descriptor(
  name='CancelCaptureResp',
  full_name='insta360.messages.CancelCaptureResp',
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
  serialized_start=60,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['CancelCapture'] = _CANCELCAPTURE
DESCRIPTOR.message_types_by_name['CancelCaptureResp'] = _CANCELCAPTURERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CancelCapture = _reflection.GeneratedProtocolMessageType('CancelCapture', (_message.Message,), {
  'DESCRIPTOR' : _CANCELCAPTURE,
  '__module__' : 'cancel_capture_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.CancelCapture)
  })
_sym_db.RegisterMessage(CancelCapture)

CancelCaptureResp = _reflection.GeneratedProtocolMessageType('CancelCaptureResp', (_message.Message,), {
  'DESCRIPTOR' : _CANCELCAPTURERESP,
  '__module__' : 'cancel_capture_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.CancelCaptureResp)
  })
_sym_db.RegisterMessage(CancelCaptureResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
