# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1alpha/user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/mysql/v1alpha/user.proto',
  package='yandex.cloud.mdb.mysql.v1alpha',
  syntax='proto3',
  serialized_options=b'\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysql',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)yandex/cloud/mdb/mysql/v1alpha/user.proto\x12\x1eyandex.cloud.mdb.mysql.v1alpha\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"i\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.Permission\"\xa4\x03\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12L\n\x05roles\x18\x02 \x03(\x0e\x32\x34.yandex.cloud.mdb.mysql.v1alpha.Permission.PrivilegeB\x07\x82\xc8\x31\x03>=1\"\xb0\x02\n\tPrivilege\x12\x19\n\x15PRIVILEGE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x41LL_PRIVILEGES\x10\x01\x12\t\n\x05\x41LTER\x10\x02\x12\x11\n\rALTER_ROUTINE\x10\x03\x12\n\n\x06\x43REATE\x10\x04\x12\x12\n\x0e\x43REATE_ROUTINE\x10\x05\x12\x1b\n\x17\x43REATE_TEMPORARY_TABLES\x10\x06\x12\x0f\n\x0b\x43REATE_VIEW\x10\x07\x12\n\n\x06\x44\x45LETE\x10\x08\x12\x08\n\x04\x44ROP\x10\t\x12\t\n\x05\x45VENT\x10\n\x12\x0b\n\x07\x45XECUTE\x10\x0b\x12\t\n\x05INDEX\x10\x0c\x12\n\n\x06INSERT\x10\r\x12\x0f\n\x0bLOCK_TABLES\x10\x0e\x12\n\n\x06SELECT\x10\x0f\x12\r\n\tSHOW_VIEW\x10\x10\x12\x0b\n\x07TRIGGER\x10\x11\x12\n\n\x06UPDATE\x10\x12\"\x99\x01\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=32\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.PermissionBn\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysqlb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_PERMISSION_PRIVILEGE = _descriptor.EnumDescriptor(
  name='Privilege',
  full_name='yandex.cloud.mdb.mysql.v1alpha.Permission.Privilege',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIVILEGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL_PRIVILEGES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALTER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALTER_ROUTINE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_ROUTINE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_TEMPORARY_TABLES', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_VIEW', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DROP', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXECUTE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INDEX', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOCK_TABLES', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELECT', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHOW_VIEW', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIGGER', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=364,
  serialized_end=668,
)
_sym_db.RegisterEnumDescriptor(_PERMISSION_PRIVILEGE)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='yandex.cloud.mdb.mysql.v1alpha.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.mysql.v1alpha.User.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.mysql.v1alpha.User.cluster_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='yandex.cloud.mdb.mysql.v1alpha.User.permissions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=140,
  serialized_end=245,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='yandex.cloud.mdb.mysql.v1alpha.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='database_name', full_name='yandex.cloud.mdb.mysql.v1alpha.Permission.database_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roles', full_name='yandex.cloud.mdb.mysql.v1alpha.Permission.roles', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\3101\003>=1', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PERMISSION_PRIVILEGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=668,
)


_USERSPEC = _descriptor.Descriptor(
  name='UserSpec',
  full_name='yandex.cloud.mdb.mysql.v1alpha.UserSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.mdb.mysql.v1alpha.UserSpec.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=32\362\3071\r[a-zA-Z0-9_]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='yandex.cloud.mdb.mysql.v1alpha.UserSpec.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\0058-128', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='yandex.cloud.mdb.mysql.v1alpha.UserSpec.permissions', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=671,
  serialized_end=824,
)

_USER.fields_by_name['permissions'].message_type = _PERMISSION
_PERMISSION.fields_by_name['roles'].enum_type = _PERMISSION_PRIVILEGE
_PERMISSION_PRIVILEGE.containing_type = _PERMISSION
_USERSPEC.fields_by_name['permissions'].message_type = _PERMISSION
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['UserSpec'] = _USERSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.User)
  })
_sym_db.RegisterMessage(User)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.Permission)
  })
_sym_db.RegisterMessage(Permission)

UserSpec = _reflection.GeneratedProtocolMessageType('UserSpec', (_message.Message,), {
  'DESCRIPTOR' : _USERSPEC,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.UserSpec)
  })
_sym_db.RegisterMessage(UserSpec)


DESCRIPTOR._options = None
_PERMISSION.fields_by_name['roles']._options = None
_USERSPEC.fields_by_name['name']._options = None
_USERSPEC.fields_by_name['password']._options = None
# @@protoc_insertion_point(module_scope)
