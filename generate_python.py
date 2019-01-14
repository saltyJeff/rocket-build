def generate_python(fields):
    pkgSize = 0
    pkgStr = '<'

    for field in fields:
        pkgSize += field.fieldType.length
        pkgStr += field.fieldType.charCode
    
    pyStr = 'PACKAGE_LEN = '+str(pkgSize)+'\n'
    pyStr += 'PACKAGE_CODE = "'+pkgStr+'"\n'
    pyStr += 'PACKAGE_FIELDS = ' + list(
        map(lambda f: f.name, fields)
    ).__str__()

    return pyStr