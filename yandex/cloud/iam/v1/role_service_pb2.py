# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iam/v1/role_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.iam.v1 import role_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/iam/v1/role_service.proto',
  package='yandex.cloud.iam.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iam',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&yandex/cloud/iam/v1/role_service.proto\x12\x13yandex.cloud.iam.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1eyandex/cloud/iam/v1/role.proto\"/\n\x0eGetRoleRequest\x12\x1d\n\x07role_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"l\n\x10ListRolesRequest\x12\x1d\n\tpage_size\x18\x01 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"V\n\x11ListRolesResponse\x12(\n\x05roles\x18\x01 \x03(\x0b\x32\x19.yandex.cloud.iam.v1.Role\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe3\x01\n\x0bRoleService\x12\x66\n\x03Get\x12#.yandex.cloud.iam.v1.GetRoleRequest\x1a\x19.yandex.cloud.iam.v1.Role\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/iam/v1/roles/{role_id}\x12l\n\x04List\x12%.yandex.cloud.iam.v1.ListRolesRequest\x1a&.yandex.cloud.iam.v1.ListRolesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/iam/v1/rolesBV\n\x17yandex.cloud.api.iam.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/iam/v1;iamb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_iam_dot_v1_dot_role__pb2.DESCRIPTOR,])




_GETROLEREQUEST = _descriptor.Descriptor(
  name='GetRoleRequest',
  full_name='yandex.cloud.iam.v1.GetRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='yandex.cloud.iam.v1.GetRoleRequest.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=203,
)


_LISTROLESREQUEST = _descriptor.Descriptor(
  name='ListRolesRequest',
  full_name='yandex.cloud.iam.v1.ListRolesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.iam.v1.ListRolesRequest.page_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.iam.v1.ListRolesRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='yandex.cloud.iam.v1.ListRolesRequest.filter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=205,
  serialized_end=313,
)


_LISTROLESRESPONSE = _descriptor.Descriptor(
  name='ListRolesResponse',
  full_name='yandex.cloud.iam.v1.ListRolesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='yandex.cloud.iam.v1.ListRolesResponse.roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.iam.v1.ListRolesResponse.next_page_token', index=1,
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
  serialized_start=315,
  serialized_end=401,
)

_LISTROLESRESPONSE.fields_by_name['roles'].message_type = yandex_dot_cloud_dot_iam_dot_v1_dot_role__pb2._ROLE
DESCRIPTOR.message_types_by_name['GetRoleRequest'] = _GETROLEREQUEST
DESCRIPTOR.message_types_by_name['ListRolesRequest'] = _LISTROLESREQUEST
DESCRIPTOR.message_types_by_name['ListRolesResponse'] = _LISTROLESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRoleRequest = _reflection.GeneratedProtocolMessageType('GetRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETROLEREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.role_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.GetRoleRequest)
  })
_sym_db.RegisterMessage(GetRoleRequest)

ListRolesRequest = _reflection.GeneratedProtocolMessageType('ListRolesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTROLESREQUEST,
  '__module__' : 'yandex.cloud.iam.v1.role_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListRolesRequest)
  })
_sym_db.RegisterMessage(ListRolesRequest)

ListRolesResponse = _reflection.GeneratedProtocolMessageType('ListRolesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTROLESRESPONSE,
  '__module__' : 'yandex.cloud.iam.v1.role_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iam.v1.ListRolesResponse)
  })
_sym_db.RegisterMessage(ListRolesResponse)


DESCRIPTOR._options = None
_GETROLEREQUEST.fields_by_name['role_id']._options = None
_LISTROLESREQUEST.fields_by_name['page_size']._options = None
_LISTROLESREQUEST.fields_by_name['page_token']._options = None
_LISTROLESREQUEST.fields_by_name['filter']._options = None

_ROLESERVICE = _descriptor.ServiceDescriptor(
  name='RoleService',
  full_name='yandex.cloud.iam.v1.RoleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=404,
  serialized_end=631,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.iam.v1.RoleService.Get',
    index=0,
    containing_service=None,
    input_type=_GETROLEREQUEST,
    output_type=yandex_dot_cloud_dot_iam_dot_v1_dot_role__pb2._ROLE,
    serialized_options=b'\202\323\344\223\002\031\022\027/iam/v1/roles/{role_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.iam.v1.RoleService.List',
    index=1,
    containing_service=None,
    input_type=_LISTROLESREQUEST,
    output_type=_LISTROLESRESPONSE,
    serialized_options=b'\202\323\344\223\002\017\022\r/iam/v1/roles',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLESERVICE)

DESCRIPTOR.services_by_name['RoleService'] = _ROLESERVICE

# @@protoc_insertion_point(module_scope)
