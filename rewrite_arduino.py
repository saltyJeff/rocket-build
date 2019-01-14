import re
import field

EXTERN_REGEX = re.compile(r'^\s*extern (unsigned )?([a-z]+) (\w+)\b', re.MULTILINE)
UPDATE_REGEX = re.compile(r'^\s*void\s+update\s*\(\s*\)\s*\{', re.MULTILINE)
INITIALIZE_REGEX = re.compile(r'^\s*void\s+initialize\s*\(\s*\)\s*\{', re.MULTILINE)
def rewrite_arduino(inoFile, namespace, defines, dueMode):
    print('re-writing '+namespace)
    #replace defines first
    for key, value in defines.items():
        inoFile = inoFile.replace(key, value)
    
    fields = []

    # rewrite externs to references
    for match in re.finditer(EXTERN_REGEX, inoFile):
        fieldName = match.group(3)

        if fieldName == 'last_update':
            continue
        
        fieldTypeName = None
        if not match.group(1):
            fieldTypeName = match.group(2)
        else:
            fieldTypeName = match.group(1)+match.group(2)
        
        fieldType = None
        if dueMode:
            fieldType = field.DUE_TYPE_DICT.get(fieldTypeName)
        else:
            fieldType = field.UNO_TYPE_DICT.get(fieldTypeName)
        if not fieldType:
            fieldType = field.EXPLICIT_TYPE_DICT.get(fieldTypeName)
        if not fieldType:
            raise RuntimeError('Unknown field '+fieldTypeName+" for "+fieldName)
        nsFieldName = namespace + "_" + fieldName
        fields.append(field.Field(nsFieldName, fieldTypeName, fieldType))
        inoFile = inoFile.replace(
            match.group(0), 
            fieldTypeName+"& "+fieldName+" = package."+nsFieldName
        )

    # rename the method stubs
    inoFile = re.sub(INITIALIZE_REGEX, 'void '+namespace+'_initialize () {', inoFile)
    inoFile = re.sub(UPDATE_REGEX, 'void '+namespace+'_update () {', inoFile)
    return (inoFile, fields)