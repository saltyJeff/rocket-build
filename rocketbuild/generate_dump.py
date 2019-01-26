def generate_dump(deps):
    dump = '#pragma once\n'
    dump += '#include "package.h"\n'
    dump += "#define PRINT(X) Serial.print(X);\n"
    dump += "#define PRINTLN(X) Serial.println(X);\n"
    dump += 'void dump() {\n'
    for dep in deps:
        dump += 'PRINT("'+dep.name+':\\t")\n'
        dump += 'PRINTLN(package.'+dep.name+')\n'
    dump += '}'
    return dump