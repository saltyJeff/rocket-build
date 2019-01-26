def generate_dump(deps):
    dump = '#pragma once\n'
    dump += "#define PRINT(x) Serial.print(x);\n"
    dump += 'void dump() {\n'
    for dep in deps:
        dump += 'PRINT('+dep.name+')\n'
    dump += '}'
    return dump