# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resources/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='resources/common.proto',
  package='',
  serialized_pb=_b('\n\x16resources/common.proto\"x\n\x06Header\x12\x0f\n\x07node_id\x18\x01 \x02(\x05\x12\x0c\n\x04time\x18\x02 \x02(\x03\x12$\n\x07message\x18\x04 \x01(\t:\x13Hello from protoc!!\x12\x13\n\x0b\x64\x65stination\x18\x08 \x01(\x05\x12\x14\n\x08max_hops\x18\n \x01(\x05:\x02-1\"6\n\x07\x46\x61ilure\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06ref_id\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xf2\x01\n\x04Task\x12\x10\n\x08\x63hunk_no\x18\x01 \x01(\x05\x12\x14\n\x0cno_of_chunks\x18\x02 \x01(\x05\x12!\n\ttask_type\x18\x03 \x02(\x0e\x32\x0e.Task.TaskType\x12\x0e\n\x06sender\x18\x04 \x02(\t\x12\x10\n\x08\x66ilename\x18\x05 \x02(\t\x12\x0e\n\x04ping\x18\x06 \x01(\x08H\x00\x12\x11\n\x07message\x18\x07 \x01(\tH\x00\x12\x17\n\x03\x65rr\x18\x08 \x01(\x0b\x32\x08.FailureH\x00\x12\x15\n\x0b\x66ileContent\x18\t \x01(\x0cH\x00\"\x1f\n\x08TaskType\x12\x08\n\x04READ\x10\x01\x12\t\n\x05WRITE\x10\x02\x42\t\n\x07payloadB\x0f\n\x0bpipe.commonH\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TASK_TASKTYPE = _descriptor.EnumDescriptor(
  name='TaskType',
  full_name='Task.TaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=405,
  serialized_end=436,
)
_sym_db.RegisterEnumDescriptor(_TASK_TASKTYPE)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='Header.node_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='Header.time', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Header.message', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("Hello from protoc!!").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='Header.destination', index=3,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_hops', full_name='Header.max_hops', index=4,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=146,
)


_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Failure.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref_id', full_name='Failure.ref_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Failure.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=202,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_no', full_name='Task.chunk_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_of_chunks', full_name='Task.no_of_chunks', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='Task.task_type', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='Task.sender', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='Task.filename', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ping', full_name='Task.ping', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='Task.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err', full_name='Task.err', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileContent', full_name='Task.fileContent', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASK_TASKTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='Task.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=205,
  serialized_end=447,
)

_TASK.fields_by_name['task_type'].enum_type = _TASK_TASKTYPE
_TASK.fields_by_name['err'].message_type = _FAILURE
_TASK_TASKTYPE.containing_type = _TASK
_TASK.oneofs_by_name['payload'].fields.append(
  _TASK.fields_by_name['ping'])
_TASK.fields_by_name['ping'].containing_oneof = _TASK.oneofs_by_name['payload']
_TASK.oneofs_by_name['payload'].fields.append(
  _TASK.fields_by_name['message'])
_TASK.fields_by_name['message'].containing_oneof = _TASK.oneofs_by_name['payload']
_TASK.oneofs_by_name['payload'].fields.append(
  _TASK.fields_by_name['err'])
_TASK.fields_by_name['err'].containing_oneof = _TASK.oneofs_by_name['payload']
_TASK.oneofs_by_name['payload'].fields.append(
  _TASK.fields_by_name['fileContent'])
_TASK.fields_by_name['fileContent'].containing_oneof = _TASK.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
DESCRIPTOR.message_types_by_name['Task'] = _TASK

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'resources.common_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  ))
_sym_db.RegisterMessage(Header)

Failure = _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), dict(
  DESCRIPTOR = _FAILURE,
  __module__ = 'resources.common_pb2'
  # @@protoc_insertion_point(class_scope:Failure)
  ))
_sym_db.RegisterMessage(Failure)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'resources.common_pb2'
  # @@protoc_insertion_point(class_scope:Task)
  ))
_sym_db.RegisterMessage(Task)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\013pipe.commonH\001'))
# @@protoc_insertion_point(module_scope)
