# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QSLcPyeTbjjOWenmnnAGTXWLnyltxoej/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej/model.proto',
  package='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,QSLcPyeTbjjOWenmnnAGTXWLnyltxoej/model.proto\x12 QSLcPyeTbjjOWenmnnAGTXWLnyltxoej\"M\n\rImageFrameSet\x12<\n\x06\x66rames\x18\x01 \x03(\x0b\x32,.QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrame\"\x1b\n\nImageFrame\x12\r\n\x05Image\x18\x01 \x01(\t\"\x1c\n\x0b\x43lassifyOut\x12\r\n\x05value\x18\x01 \x03(\t2s\n\x05Model\x12j\n\x08\x63lassify\x12/.QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrameSet\x1a-.QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ClassifyOutb\x06proto3')
)




_IMAGEFRAMESET = _descriptor.Descriptor(
  name='ImageFrameSet',
  full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrameSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrameSet.frames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=82,
  serialized_end=159,
)


_IMAGEFRAME = _descriptor.Descriptor(
  name='ImageFrame',
  full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Image', full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrame.Image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=161,
  serialized_end=188,
)


_CLASSIFYOUT = _descriptor.Descriptor(
  name='ClassifyOut',
  full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ClassifyOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ClassifyOut.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=190,
  serialized_end=218,
)

_IMAGEFRAMESET.fields_by_name['frames'].message_type = _IMAGEFRAME
DESCRIPTOR.message_types_by_name['ImageFrameSet'] = _IMAGEFRAMESET
DESCRIPTOR.message_types_by_name['ImageFrame'] = _IMAGEFRAME
DESCRIPTOR.message_types_by_name['ClassifyOut'] = _CLASSIFYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageFrameSet = _reflection.GeneratedProtocolMessageType('ImageFrameSet', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEFRAMESET,
  __module__ = 'QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.model_pb2'
  # @@protoc_insertion_point(class_scope:QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrameSet)
  ))
_sym_db.RegisterMessage(ImageFrameSet)

ImageFrame = _reflection.GeneratedProtocolMessageType('ImageFrame', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEFRAME,
  __module__ = 'QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.model_pb2'
  # @@protoc_insertion_point(class_scope:QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ImageFrame)
  ))
_sym_db.RegisterMessage(ImageFrame)

ClassifyOut = _reflection.GeneratedProtocolMessageType('ClassifyOut', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFYOUT,
  __module__ = 'QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.model_pb2'
  # @@protoc_insertion_point(class_scope:QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.ClassifyOut)
  ))
_sym_db.RegisterMessage(ClassifyOut)



_MODEL = _descriptor.ServiceDescriptor(
  name='Model',
  full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.Model',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=220,
  serialized_end=335,
  methods=[
  _descriptor.MethodDescriptor(
    name='classify',
    full_name='QSLcPyeTbjjOWenmnnAGTXWLnyltxoej.Model.classify',
    index=0,
    containing_service=None,
    input_type=_IMAGEFRAMESET,
    output_type=_CLASSIFYOUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODEL)

DESCRIPTOR.services_by_name['Model'] = _MODEL

# @@protoc_insertion_point(module_scope)