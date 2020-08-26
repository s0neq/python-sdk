# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/format_schema_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.clickhouse.v1 import format_schema_pb2 as yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_format__schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/mdb/clickhouse/v1/format_schema_service.proto',
  package='yandex.cloud.mdb.clickhouse.v1',
  syntax='proto3',
  serialized_options=b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:yandex/cloud/mdb/clickhouse/v1/format_schema_service.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x32yandex/cloud/mdb/clickhouse/v1/format_schema.proto\"v\n\x16GetFormatSchemaRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12:\n\x12\x66ormat_schema_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"z\n\x18ListFormatSchemasRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"z\n\x19ListFormatSchemasResponse\x12\x44\n\x0e\x66ormat_schemas\x18\x01 \x03(\x0b\x32,.yandex.cloud.mdb.clickhouse.v1.FormatSchema\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xd2\x01\n\x19\x43reateFormatSchemaRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12:\n\x12\x66ormat_schema_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x44\n\x04type\x18\x03 \x01(\x0e\x32\x30.yandex.cloud.mdb.clickhouse.v1.FormatSchemaTypeB\x04\xe8\xc7\x31\x01\x12\x11\n\x03uri\x18\x04 \x01(\tB\x04\xe8\xc7\x31\x01\"L\n\x1a\x43reateFormatSchemaMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x1a\n\x12\x66ormat_schema_name\x18\x02 \x01(\t\"\xb7\x01\n\x19UpdateFormatSchemaRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12:\n\x12\x66ormat_schema_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0b\n\x03uri\x18\x04 \x01(\t\"L\n\x1aUpdateFormatSchemaMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x1a\n\x12\x66ormat_schema_name\x18\x02 \x01(\t\"y\n\x19\x44\x65leteFormatSchemaRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12:\n\x12\x66ormat_schema_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"L\n\x1a\x44\x65leteFormatSchemaMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x1a\n\x12\x66ormat_schema_name\x18\x02 \x01(\t2\xea\x08\n\x13\x46ormatSchemaService\x12\xc4\x01\n\x03Get\x12\x36.yandex.cloud.mdb.clickhouse.v1.GetFormatSchemaRequest\x1a,.yandex.cloud.mdb.clickhouse.v1.FormatSchema\"W\x82\xd3\xe4\x93\x02Q\x12O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}\x12\xbf\x01\n\x04List\x12\x38.yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest\x1a\x39.yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasResponse\"B\x82\xd3\xe4\x93\x02<\x12:/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas\x12\xdb\x01\n\x06\x43reate\x12\x39.yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest\x1a!.yandex.cloud.operation.Operation\"s\x82\xd3\xe4\x93\x02?\":/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas:\x01*\xb2\xd2**\n\x1a\x43reateFormatSchemaMetadata\x12\x0c\x46ormatSchema\x12\xf1\x01\n\x06Update\x12\x39.yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\x82\xd3\xe4\x93\x02T2O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}:\x01*\xb2\xd2**\n\x1aUpdateFormatSchemaMetadata\x12\x0c\x46ormatSchema\x12\xf7\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaRequest\x1a!.yandex.cloud.operation.Operation\"\x8e\x01\x82\xd3\xe4\x93\x02Q*O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}\xb2\xd2*3\n\x1a\x44\x65leteFormatSchemaMetadata\x12\x15google.protobuf.EmptyBs\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_format__schema__pb2.DESCRIPTOR,])




_GETFORMATSCHEMAREQUEST = _descriptor.Descriptor(
  name='GetFormatSchemaRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.GetFormatSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.GetFormatSchemaRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.GetFormatSchemaRequest.format_schema_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=433,
)


_LISTFORMATSCHEMASREQUEST = _descriptor.Descriptor(
  name='ListFormatSchemasRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=435,
  serialized_end=557,
)


_LISTFORMATSCHEMASRESPONSE = _descriptor.Descriptor(
  name='ListFormatSchemasResponse',
  full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format_schemas', full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasResponse.format_schemas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasResponse.next_page_token', index=1,
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
  serialized_start=559,
  serialized_end=681,
)


_CREATEFORMATSCHEMAREQUEST = _descriptor.Descriptor(
  name='CreateFormatSchemaRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest.format_schema_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=684,
  serialized_end=894,
)


_CREATEFORMATSCHEMAMETADATA = _descriptor.Descriptor(
  name='CreateFormatSchemaMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaMetadata.format_schema_name', index=1,
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
  serialized_start=896,
  serialized_end=972,
)


_UPDATEFORMATSCHEMAREQUEST = _descriptor.Descriptor(
  name='UpdateFormatSchemaRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest.format_schema_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest.update_mask', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest.uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=975,
  serialized_end=1158,
)


_UPDATEFORMATSCHEMAMETADATA = _descriptor.Descriptor(
  name='UpdateFormatSchemaMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaMetadata.format_schema_name', index=1,
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
  serialized_start=1160,
  serialized_end=1236,
)


_DELETEFORMATSCHEMAREQUEST = _descriptor.Descriptor(
  name='DeleteFormatSchemaRequest',
  full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaRequest.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaRequest.format_schema_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1238,
  serialized_end=1359,
)


_DELETEFORMATSCHEMAMETADATA = _descriptor.Descriptor(
  name='DeleteFormatSchemaMetadata',
  full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaMetadata.cluster_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format_schema_name', full_name='yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaMetadata.format_schema_name', index=1,
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
  serialized_start=1361,
  serialized_end=1437,
)

_LISTFORMATSCHEMASRESPONSE.fields_by_name['format_schemas'].message_type = yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_format__schema__pb2._FORMATSCHEMA
_CREATEFORMATSCHEMAREQUEST.fields_by_name['type'].enum_type = yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_format__schema__pb2._FORMATSCHEMATYPE
_UPDATEFORMATSCHEMAREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['GetFormatSchemaRequest'] = _GETFORMATSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['ListFormatSchemasRequest'] = _LISTFORMATSCHEMASREQUEST
DESCRIPTOR.message_types_by_name['ListFormatSchemasResponse'] = _LISTFORMATSCHEMASRESPONSE
DESCRIPTOR.message_types_by_name['CreateFormatSchemaRequest'] = _CREATEFORMATSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['CreateFormatSchemaMetadata'] = _CREATEFORMATSCHEMAMETADATA
DESCRIPTOR.message_types_by_name['UpdateFormatSchemaRequest'] = _UPDATEFORMATSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['UpdateFormatSchemaMetadata'] = _UPDATEFORMATSCHEMAMETADATA
DESCRIPTOR.message_types_by_name['DeleteFormatSchemaRequest'] = _DELETEFORMATSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['DeleteFormatSchemaMetadata'] = _DELETEFORMATSCHEMAMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFormatSchemaRequest = _reflection.GeneratedProtocolMessageType('GetFormatSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFORMATSCHEMAREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.GetFormatSchemaRequest)
  })
_sym_db.RegisterMessage(GetFormatSchemaRequest)

ListFormatSchemasRequest = _reflection.GeneratedProtocolMessageType('ListFormatSchemasRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFORMATSCHEMASREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasRequest)
  })
_sym_db.RegisterMessage(ListFormatSchemasRequest)

ListFormatSchemasResponse = _reflection.GeneratedProtocolMessageType('ListFormatSchemasResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFORMATSCHEMASRESPONSE,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.ListFormatSchemasResponse)
  })
_sym_db.RegisterMessage(ListFormatSchemasResponse)

CreateFormatSchemaRequest = _reflection.GeneratedProtocolMessageType('CreateFormatSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFORMATSCHEMAREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaRequest)
  })
_sym_db.RegisterMessage(CreateFormatSchemaRequest)

CreateFormatSchemaMetadata = _reflection.GeneratedProtocolMessageType('CreateFormatSchemaMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFORMATSCHEMAMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.CreateFormatSchemaMetadata)
  })
_sym_db.RegisterMessage(CreateFormatSchemaMetadata)

UpdateFormatSchemaRequest = _reflection.GeneratedProtocolMessageType('UpdateFormatSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFORMATSCHEMAREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaRequest)
  })
_sym_db.RegisterMessage(UpdateFormatSchemaRequest)

UpdateFormatSchemaMetadata = _reflection.GeneratedProtocolMessageType('UpdateFormatSchemaMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFORMATSCHEMAMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.UpdateFormatSchemaMetadata)
  })
_sym_db.RegisterMessage(UpdateFormatSchemaMetadata)

DeleteFormatSchemaRequest = _reflection.GeneratedProtocolMessageType('DeleteFormatSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFORMATSCHEMAREQUEST,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaRequest)
  })
_sym_db.RegisterMessage(DeleteFormatSchemaRequest)

DeleteFormatSchemaMetadata = _reflection.GeneratedProtocolMessageType('DeleteFormatSchemaMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEFORMATSCHEMAMETADATA,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.format_schema_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.DeleteFormatSchemaMetadata)
  })
_sym_db.RegisterMessage(DeleteFormatSchemaMetadata)


DESCRIPTOR._options = None
_GETFORMATSCHEMAREQUEST.fields_by_name['cluster_id']._options = None
_GETFORMATSCHEMAREQUEST.fields_by_name['format_schema_name']._options = None
_LISTFORMATSCHEMASREQUEST.fields_by_name['cluster_id']._options = None
_LISTFORMATSCHEMASREQUEST.fields_by_name['page_size']._options = None
_LISTFORMATSCHEMASREQUEST.fields_by_name['page_token']._options = None
_CREATEFORMATSCHEMAREQUEST.fields_by_name['cluster_id']._options = None
_CREATEFORMATSCHEMAREQUEST.fields_by_name['format_schema_name']._options = None
_CREATEFORMATSCHEMAREQUEST.fields_by_name['type']._options = None
_CREATEFORMATSCHEMAREQUEST.fields_by_name['uri']._options = None
_UPDATEFORMATSCHEMAREQUEST.fields_by_name['cluster_id']._options = None
_UPDATEFORMATSCHEMAREQUEST.fields_by_name['format_schema_name']._options = None
_DELETEFORMATSCHEMAREQUEST.fields_by_name['cluster_id']._options = None
_DELETEFORMATSCHEMAREQUEST.fields_by_name['format_schema_name']._options = None

_FORMATSCHEMASERVICE = _descriptor.ServiceDescriptor(
  name='FormatSchemaService',
  full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1440,
  serialized_end=2570,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService.Get',
    index=0,
    containing_service=None,
    input_type=_GETFORMATSCHEMAREQUEST,
    output_type=yandex_dot_cloud_dot_mdb_dot_clickhouse_dot_v1_dot_format__schema__pb2._FORMATSCHEMA,
    serialized_options=b'\202\323\344\223\002Q\022O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService.List',
    index=1,
    containing_service=None,
    input_type=_LISTFORMATSCHEMASREQUEST,
    output_type=_LISTFORMATSCHEMASRESPONSE,
    serialized_options=b'\202\323\344\223\002<\022:/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEFORMATSCHEMAREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002?\":/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas:\001*\262\322**\n\032CreateFormatSchemaMetadata\022\014FormatSchema',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEFORMATSCHEMAREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002T2O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}:\001*\262\322**\n\032UpdateFormatSchemaMetadata\022\014FormatSchema',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.mdb.clickhouse.v1.FormatSchemaService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEFORMATSCHEMAREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002Q*O/managed-clickhouse/v1/clusters/{cluster_id}/formatSchemas/{format_schema_name}\262\322*3\n\032DeleteFormatSchemaMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORMATSCHEMASERVICE)

DESCRIPTOR.services_by_name['FormatSchemaService'] = _FORMATSCHEMASERVICE

# @@protoc_insertion_point(module_scope)
