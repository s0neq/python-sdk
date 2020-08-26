# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/kms/v1/symmetric_crypto_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.kms.v1 import symmetric_key_pb2 as yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/kms/v1/symmetric_crypto_service.proto',
  package='yandex.cloud.kms.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.kms.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1;kms',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2yandex/cloud/kms/v1/symmetric_crypto_service.proto\x12\x13yandex.cloud.kms.v1\x1a\x1cgoogle/api/annotations.proto\x1a\'yandex/cloud/kms/v1/symmetric_key.proto\x1a\x1dyandex/cloud/validation.proto\"\x9a\x01\n\x17SymmetricEncryptRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1f\n\x0b\x61\x61\x64_context\x18\x03 \x01(\x0c\x42\n\x8a\xc8\x31\x06<=8192\x12\"\n\tplaintext\x18\x04 \x01(\x0c\x42\x0f\xe8\xc7\x31\x01\x8a\xc8\x31\x07<=32768\"j\n\x18SymmetricEncryptResponse\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x12\n\nciphertext\x18\x03 \x01(\x0c\"r\n\x17SymmetricDecryptRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\x0b\x61\x61\x64_context\x18\x02 \x01(\x0c\x42\n\x8a\xc8\x31\x06<=8192\x12\x18\n\nciphertext\x18\x03 \x01(\x0c\x42\x04\xe8\xc7\x31\x01\"Q\n\x18SymmetricDecryptResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\x11\n\tplaintext\x18\x03 \x01(\x0c\"\xcd\x01\n\x16GenerateDataKeyRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1f\n\x0b\x61\x61\x64_context\x18\x03 \x01(\x0c\x42\n\x8a\xc8\x31\x06<=8192\x12>\n\rdata_key_spec\x18\x04 \x01(\x0e\x32\'.yandex.cloud.kms.v1.SymmetricAlgorithm\x12\x16\n\x0eskip_plaintext\x18\x05 \x01(\x08\"v\n\x17GenerateDataKeyResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x61ta_key_plaintext\x18\x03 \x01(\x0c\x12\x1b\n\x13\x64\x61ta_key_ciphertext\x18\x04 \x01(\x0c\"\xdf\x01\n\x19SymmetricReEncryptRequest\x12\x1c\n\x06key_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\nversion_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1f\n\x0b\x61\x61\x64_context\x18\x03 \x01(\x0c\x42\n\x8a\xc8\x31\x06<=8192\x12#\n\rsource_key_id\x18\x04 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12&\n\x12source_aad_context\x18\x05 \x01(\x0c\x42\n\x8a\xc8\x31\x06<=8192\x12\x18\n\nciphertext\x18\x06 \x01(\x0c\x42\x04\xe8\xc7\x31\x01\"\x86\x01\n\x1aSymmetricReEncryptResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\x15\n\rsource_key_id\x18\x03 \x01(\t\x12\x19\n\x11source_version_id\x18\x04 \x01(\t\x12\x12\n\nciphertext\x18\x05 \x01(\x0c\x32\xfa\x04\n\x16SymmetricCryptoService\x12\x90\x01\n\x07\x45ncrypt\x12,.yandex.cloud.kms.v1.SymmetricEncryptRequest\x1a-.yandex.cloud.kms.v1.SymmetricEncryptResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/kms/v1/keys/{key_id}:encrypt:\x01*\x12\x90\x01\n\x07\x44\x65\x63rypt\x12,.yandex.cloud.kms.v1.SymmetricDecryptRequest\x1a-.yandex.cloud.kms.v1.SymmetricDecryptResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/kms/v1/keys/{key_id}:decrypt:\x01*\x12\x98\x01\n\tReEncrypt\x12..yandex.cloud.kms.v1.SymmetricReEncryptRequest\x1a/.yandex.cloud.kms.v1.SymmetricReEncryptResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/kms/v1/keys/{key_id}:reEncrypt:\x01*\x12\x9e\x01\n\x0fGenerateDataKey\x12+.yandex.cloud.kms.v1.GenerateDataKeyRequest\x1a,.yandex.cloud.kms.v1.GenerateDataKeyResponse\"0\x82\xd3\xe4\x93\x02*\"%/kms/v1/keys/{key_id}:generateDataKey:\x01*BV\n\x17yandex.cloud.api.kms.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/kms/v1;kmsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_SYMMETRICENCRYPTREQUEST = _descriptor.Descriptor(
  name='SymmetricEncryptRequest',
  full_name='yandex.cloud.kms.v1.SymmetricEncryptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricEncryptRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.SymmetricEncryptRequest.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aad_context', full_name='yandex.cloud.kms.v1.SymmetricEncryptRequest.aad_context', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=8192', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plaintext', full_name='yandex.cloud.kms.v1.SymmetricEncryptRequest.plaintext', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\007<=32768', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=332,
)


_SYMMETRICENCRYPTRESPONSE = _descriptor.Descriptor(
  name='SymmetricEncryptResponse',
  full_name='yandex.cloud.kms.v1.SymmetricEncryptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricEncryptResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.SymmetricEncryptResponse.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='yandex.cloud.kms.v1.SymmetricEncryptResponse.ciphertext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=334,
  serialized_end=440,
)


_SYMMETRICDECRYPTREQUEST = _descriptor.Descriptor(
  name='SymmetricDecryptRequest',
  full_name='yandex.cloud.kms.v1.SymmetricDecryptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricDecryptRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aad_context', full_name='yandex.cloud.kms.v1.SymmetricDecryptRequest.aad_context', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=8192', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='yandex.cloud.kms.v1.SymmetricDecryptRequest.ciphertext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=442,
  serialized_end=556,
)


_SYMMETRICDECRYPTRESPONSE = _descriptor.Descriptor(
  name='SymmetricDecryptResponse',
  full_name='yandex.cloud.kms.v1.SymmetricDecryptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricDecryptResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.SymmetricDecryptResponse.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plaintext', full_name='yandex.cloud.kms.v1.SymmetricDecryptResponse.plaintext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=558,
  serialized_end=639,
)


_GENERATEDATAKEYREQUEST = _descriptor.Descriptor(
  name='GenerateDataKeyRequest',
  full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aad_context', full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest.aad_context', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=8192', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_key_spec', full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest.data_key_spec', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_plaintext', full_name='yandex.cloud.kms.v1.GenerateDataKeyRequest.skip_plaintext', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=642,
  serialized_end=847,
)


_GENERATEDATAKEYRESPONSE = _descriptor.Descriptor(
  name='GenerateDataKeyResponse',
  full_name='yandex.cloud.kms.v1.GenerateDataKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.GenerateDataKeyResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.GenerateDataKeyResponse.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_key_plaintext', full_name='yandex.cloud.kms.v1.GenerateDataKeyResponse.data_key_plaintext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_key_ciphertext', full_name='yandex.cloud.kms.v1.GenerateDataKeyResponse.data_key_ciphertext', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=849,
  serialized_end=967,
)


_SYMMETRICREENCRYPTREQUEST = _descriptor.Descriptor(
  name='SymmetricReEncryptRequest',
  full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aad_context', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.aad_context', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=8192', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_key_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.source_key_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_aad_context', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.source_aad_context', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\006<=8192', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='yandex.cloud.kms.v1.SymmetricReEncryptRequest.ciphertext', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=970,
  serialized_end=1193,
)


_SYMMETRICREENCRYPTRESPONSE = _descriptor.Descriptor(
  name='SymmetricReEncryptResponse',
  full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse.key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse.version_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_key_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse.source_key_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_version_id', full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse.source_version_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='yandex.cloud.kms.v1.SymmetricReEncryptResponse.ciphertext', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1196,
  serialized_end=1330,
)

_GENERATEDATAKEYREQUEST.fields_by_name['data_key_spec'].enum_type = yandex_dot_cloud_dot_kms_dot_v1_dot_symmetric__key__pb2._SYMMETRICALGORITHM
DESCRIPTOR.message_types_by_name['SymmetricEncryptRequest'] = _SYMMETRICENCRYPTREQUEST
DESCRIPTOR.message_types_by_name['SymmetricEncryptResponse'] = _SYMMETRICENCRYPTRESPONSE
DESCRIPTOR.message_types_by_name['SymmetricDecryptRequest'] = _SYMMETRICDECRYPTREQUEST
DESCRIPTOR.message_types_by_name['SymmetricDecryptResponse'] = _SYMMETRICDECRYPTRESPONSE
DESCRIPTOR.message_types_by_name['GenerateDataKeyRequest'] = _GENERATEDATAKEYREQUEST
DESCRIPTOR.message_types_by_name['GenerateDataKeyResponse'] = _GENERATEDATAKEYRESPONSE
DESCRIPTOR.message_types_by_name['SymmetricReEncryptRequest'] = _SYMMETRICREENCRYPTREQUEST
DESCRIPTOR.message_types_by_name['SymmetricReEncryptResponse'] = _SYMMETRICREENCRYPTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SymmetricEncryptRequest = _reflection.GeneratedProtocolMessageType('SymmetricEncryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICENCRYPTREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricEncryptRequest)
  })
_sym_db.RegisterMessage(SymmetricEncryptRequest)

SymmetricEncryptResponse = _reflection.GeneratedProtocolMessageType('SymmetricEncryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICENCRYPTRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricEncryptResponse)
  })
_sym_db.RegisterMessage(SymmetricEncryptResponse)

SymmetricDecryptRequest = _reflection.GeneratedProtocolMessageType('SymmetricDecryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICDECRYPTREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricDecryptRequest)
  })
_sym_db.RegisterMessage(SymmetricDecryptRequest)

SymmetricDecryptResponse = _reflection.GeneratedProtocolMessageType('SymmetricDecryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICDECRYPTRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricDecryptResponse)
  })
_sym_db.RegisterMessage(SymmetricDecryptResponse)

GenerateDataKeyRequest = _reflection.GeneratedProtocolMessageType('GenerateDataKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEDATAKEYREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.GenerateDataKeyRequest)
  })
_sym_db.RegisterMessage(GenerateDataKeyRequest)

GenerateDataKeyResponse = _reflection.GeneratedProtocolMessageType('GenerateDataKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEDATAKEYRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.GenerateDataKeyResponse)
  })
_sym_db.RegisterMessage(GenerateDataKeyResponse)

SymmetricReEncryptRequest = _reflection.GeneratedProtocolMessageType('SymmetricReEncryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICREENCRYPTREQUEST,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricReEncryptRequest)
  })
_sym_db.RegisterMessage(SymmetricReEncryptRequest)

SymmetricReEncryptResponse = _reflection.GeneratedProtocolMessageType('SymmetricReEncryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYMMETRICREENCRYPTRESPONSE,
  '__module__' : 'yandex.cloud.kms.v1.symmetric_crypto_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.kms.v1.SymmetricReEncryptResponse)
  })
_sym_db.RegisterMessage(SymmetricReEncryptResponse)


DESCRIPTOR._options = None
_SYMMETRICENCRYPTREQUEST.fields_by_name['key_id']._options = None
_SYMMETRICENCRYPTREQUEST.fields_by_name['version_id']._options = None
_SYMMETRICENCRYPTREQUEST.fields_by_name['aad_context']._options = None
_SYMMETRICENCRYPTREQUEST.fields_by_name['plaintext']._options = None
_SYMMETRICENCRYPTRESPONSE.fields_by_name['key_id']._options = None
_SYMMETRICENCRYPTRESPONSE.fields_by_name['version_id']._options = None
_SYMMETRICDECRYPTREQUEST.fields_by_name['key_id']._options = None
_SYMMETRICDECRYPTREQUEST.fields_by_name['aad_context']._options = None
_SYMMETRICDECRYPTREQUEST.fields_by_name['ciphertext']._options = None
_GENERATEDATAKEYREQUEST.fields_by_name['key_id']._options = None
_GENERATEDATAKEYREQUEST.fields_by_name['version_id']._options = None
_GENERATEDATAKEYREQUEST.fields_by_name['aad_context']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['key_id']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['version_id']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['aad_context']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['source_key_id']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['source_aad_context']._options = None
_SYMMETRICREENCRYPTREQUEST.fields_by_name['ciphertext']._options = None

_SYMMETRICCRYPTOSERVICE = _descriptor.ServiceDescriptor(
  name='SymmetricCryptoService',
  full_name='yandex.cloud.kms.v1.SymmetricCryptoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1333,
  serialized_end=1967,
  methods=[
  _descriptor.MethodDescriptor(
    name='Encrypt',
    full_name='yandex.cloud.kms.v1.SymmetricCryptoService.Encrypt',
    index=0,
    containing_service=None,
    input_type=_SYMMETRICENCRYPTREQUEST,
    output_type=_SYMMETRICENCRYPTRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\"\035/kms/v1/keys/{key_id}:encrypt:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Decrypt',
    full_name='yandex.cloud.kms.v1.SymmetricCryptoService.Decrypt',
    index=1,
    containing_service=None,
    input_type=_SYMMETRICDECRYPTREQUEST,
    output_type=_SYMMETRICDECRYPTRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\"\035/kms/v1/keys/{key_id}:decrypt:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReEncrypt',
    full_name='yandex.cloud.kms.v1.SymmetricCryptoService.ReEncrypt',
    index=2,
    containing_service=None,
    input_type=_SYMMETRICREENCRYPTREQUEST,
    output_type=_SYMMETRICREENCRYPTRESPONSE,
    serialized_options=b'\202\323\344\223\002$\"\037/kms/v1/keys/{key_id}:reEncrypt:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateDataKey',
    full_name='yandex.cloud.kms.v1.SymmetricCryptoService.GenerateDataKey',
    index=3,
    containing_service=None,
    input_type=_GENERATEDATAKEYREQUEST,
    output_type=_GENERATEDATAKEYRESPONSE,
    serialized_options=b'\202\323\344\223\002*\"%/kms/v1/keys/{key_id}:generateDataKey:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYMMETRICCRYPTOSERVICE)

DESCRIPTOR.services_by_name['SymmetricCryptoService'] = _SYMMETRICCRYPTOSERVICE

# @@protoc_insertion_point(module_scope)
