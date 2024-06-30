# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: button_press_params.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import video_pb2 as video__pb2

from video_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='button_press_params.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x62utton_press_params.proto\x12\x11insta360.messages\x1a\x0bvideo.proto\"\x98\x01\n\x11\x42uttonPressParams\x12J\n\x1e\x62utton_param_record_resolution\x18\x01 \x01(\x0e\x32\".insta360.messages.VideoResolution\x12\x1f\n\x17\x62utton_param_lapse_Time\x18\x02 \x01(\r\x12\x16\n\x0erec_limit_time\x18\x03 \x01(\r*\xaf\x01\n\x15\x42uttonPressParamsType\x12\x1f\n\x1b\x42UTTON_PRESS_PARAMS_UNKNOWN\x10\x00\x12\"\n\x1e\x42UTTON_PARAM_RECORD_RESOLUTION\x10\x01\x12\x1b\n\x17\x42UTTON_PARAM_LAPSE_TIME\x10\x02\x12\x1e\n\x1a\x42UTTON_PARAM_RES_REC_LIMIT\x10\x03\x12\x14\n\x10\x42UTTON_PARAM_NUM\x10\x04\x42\x08\xa2\x02\x05INSPBP\x00\x62\x06proto3'
  ,
  dependencies=[video__pb2.DESCRIPTOR,],
  public_dependencies=[video__pb2.DESCRIPTOR,])

_BUTTONPRESSPARAMSTYPE = _descriptor.EnumDescriptor(
  name='ButtonPressParamsType',
  full_name='insta360.messages.ButtonPressParamsType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON_PRESS_PARAMS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_PARAM_RECORD_RESOLUTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_PARAM_LAPSE_TIME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_PARAM_RES_REC_LIMIT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_PARAM_NUM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=217,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_BUTTONPRESSPARAMSTYPE)

ButtonPressParamsType = enum_type_wrapper.EnumTypeWrapper(_BUTTONPRESSPARAMSTYPE)
BUTTON_PRESS_PARAMS_UNKNOWN = 0
BUTTON_PARAM_RECORD_RESOLUTION = 1
BUTTON_PARAM_LAPSE_TIME = 2
BUTTON_PARAM_RES_REC_LIMIT = 3
BUTTON_PARAM_NUM = 4



_BUTTONPRESSPARAMS = _descriptor.Descriptor(
  name='ButtonPressParams',
  full_name='insta360.messages.ButtonPressParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='button_param_record_resolution', full_name='insta360.messages.ButtonPressParams.button_param_record_resolution', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='button_param_lapse_Time', full_name='insta360.messages.ButtonPressParams.button_param_lapse_Time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rec_limit_time', full_name='insta360.messages.ButtonPressParams.rec_limit_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=62,
  serialized_end=214,
)

_BUTTONPRESSPARAMS.fields_by_name['button_param_record_resolution'].enum_type = video__pb2._VIDEORESOLUTION
DESCRIPTOR.message_types_by_name['ButtonPressParams'] = _BUTTONPRESSPARAMS
DESCRIPTOR.enum_types_by_name['ButtonPressParamsType'] = _BUTTONPRESSPARAMSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ButtonPressParams = _reflection.GeneratedProtocolMessageType('ButtonPressParams', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONPRESSPARAMS,
  '__module__' : 'button_press_params_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.ButtonPressParams)
  })
_sym_db.RegisterMessage(ButtonPressParams)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
