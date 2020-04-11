# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='grpcSkill',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rservice.proto\x12\tgrpcSkill\"W\n\x1aSkillDeterminationResponse\x12\x10\n\x08\x41\x63\x63uracy\x18\x01 \x01(\x02\x12\x10\n\x08\x44uration\x18\x02 \x01(\x02\x12\x15\n\rFowardAddress\x18\x03 \x01(\t\",\n\x19SkillDeterminationRequest\x12\x0f\n\x07Message\x18\x01 \x01(\t\"4\n\tSkillInfo\x12\x13\n\x0b\x45xampleText\x18\x01 \x01(\t\x12\x12\n\nPOSMapping\x18\x02 \x01(\t\"O\n\x0fRegisterRequest\x12)\n\x0b\x45xampleInfo\x18\x01 \x03(\x0b\x32\x14.grpcSkill.SkillInfo\x12\x11\n\tSkillName\x18\x02 \x01(\t\"(\n\x10RegisterResponse\x12\x14\n\x0cIsRegistered\x18\x01 \x01(\x08\x32\xcd\x01\n\tgrpcSkill\x12T\n\x17RegisterCurrentInstance\x12\x1a.grpcSkill.RegisterRequest\x1a\x1b.grpcSkill.RegisterResponse\"\x00\x12j\n\x19\x44\x65termineSkillFromMessage\x12$.grpcSkill.SkillDeterminationRequest\x1a%.grpcSkill.SkillDeterminationResponse\"\x00\x62\x06proto3'
)




_SKILLDETERMINATIONRESPONSE = _descriptor.Descriptor(
  name='SkillDeterminationResponse',
  full_name='grpcSkill.SkillDeterminationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Accuracy', full_name='grpcSkill.SkillDeterminationResponse.Accuracy', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Duration', full_name='grpcSkill.SkillDeterminationResponse.Duration', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FowardAddress', full_name='grpcSkill.SkillDeterminationResponse.FowardAddress', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=28,
  serialized_end=115,
)


_SKILLDETERMINATIONREQUEST = _descriptor.Descriptor(
  name='SkillDeterminationRequest',
  full_name='grpcSkill.SkillDeterminationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='grpcSkill.SkillDeterminationRequest.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=161,
)


_SKILLINFO = _descriptor.Descriptor(
  name='SkillInfo',
  full_name='grpcSkill.SkillInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ExampleText', full_name='grpcSkill.SkillInfo.ExampleText', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='POSMapping', full_name='grpcSkill.SkillInfo.POSMapping', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=163,
  serialized_end=215,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='grpcSkill.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ExampleInfo', full_name='grpcSkill.RegisterRequest.ExampleInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SkillName', full_name='grpcSkill.RegisterRequest.SkillName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=217,
  serialized_end=296,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='grpcSkill.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='IsRegistered', full_name='grpcSkill.RegisterResponse.IsRegistered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=298,
  serialized_end=338,
)

_REGISTERREQUEST.fields_by_name['ExampleInfo'].message_type = _SKILLINFO
DESCRIPTOR.message_types_by_name['SkillDeterminationResponse'] = _SKILLDETERMINATIONRESPONSE
DESCRIPTOR.message_types_by_name['SkillDeterminationRequest'] = _SKILLDETERMINATIONREQUEST
DESCRIPTOR.message_types_by_name['SkillInfo'] = _SKILLINFO
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkillDeterminationResponse = _reflection.GeneratedProtocolMessageType('SkillDeterminationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SKILLDETERMINATIONRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:grpcSkill.SkillDeterminationResponse)
  })
_sym_db.RegisterMessage(SkillDeterminationResponse)

SkillDeterminationRequest = _reflection.GeneratedProtocolMessageType('SkillDeterminationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SKILLDETERMINATIONREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:grpcSkill.SkillDeterminationRequest)
  })
_sym_db.RegisterMessage(SkillDeterminationRequest)

SkillInfo = _reflection.GeneratedProtocolMessageType('SkillInfo', (_message.Message,), {
  'DESCRIPTOR' : _SKILLINFO,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:grpcSkill.SkillInfo)
  })
_sym_db.RegisterMessage(SkillInfo)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:grpcSkill.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:grpcSkill.RegisterResponse)
  })
_sym_db.RegisterMessage(RegisterResponse)



_GRPCSKILL = _descriptor.ServiceDescriptor(
  name='grpcSkill',
  full_name='grpcSkill.grpcSkill',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=341,
  serialized_end=546,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterCurrentInstance',
    full_name='grpcSkill.grpcSkill.RegisterCurrentInstance',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DetermineSkillFromMessage',
    full_name='grpcSkill.grpcSkill.DetermineSkillFromMessage',
    index=1,
    containing_service=None,
    input_type=_SKILLDETERMINATIONREQUEST,
    output_type=_SKILLDETERMINATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GRPCSKILL)

DESCRIPTOR.services_by_name['grpcSkill'] = _GRPCSKILL

# @@protoc_insertion_point(module_scope)