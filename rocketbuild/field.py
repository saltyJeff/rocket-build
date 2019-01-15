class Field:
    def __init__(self, name, fieldTypeName, fieldType):
        self.name = name
        self.fieldTypeName = fieldTypeName
        self.fieldType = fieldType

class FieldType:
    def __init__(self, charCode, length):
        self.charCode = charCode
        self.length = length


EXPLICIT_TYPE_DICT = {
    'int8_t': FieldType('b', 1),
    'uint8_t': FieldType('B', 1),
    'int16_t': FieldType('h', 2),
    'uint16_t': FieldType('H', 2),
    'int32_t': FieldType('i', 4),
    'uint32_t': FieldType('I', 4),
    'int64_t': FieldType('q', 8),
    'uint64_t': FieldType('Q', 8),
    'float': FieldType('f', 4),
    'double': FieldType('d', 8),
    'short': FieldType('h', 2),
    'byte': FieldType('B', 1),
    'unsigned char': FieldType('B', 1),
    'char': FieldType('b', 1),
    'long': FieldType('i', 4),
    'unsigned long': FieldType('I', 4),
}

UNO_TYPE_DICT = {
    'int': EXPLICIT_TYPE_DICT['int16_t'],
    'unsigned int': EXPLICIT_TYPE_DICT['uint16_t']
}

DUE_TYPE_DICT = {
    'int': EXPLICIT_TYPE_DICT['int32_t'],
    'unsigned int': EXPLICIT_TYPE_DICT['uint32_t']
}