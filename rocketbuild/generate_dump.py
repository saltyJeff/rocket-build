def generate_dump(deps):
    dump = '#include "package.h"\n'
    dump += 'void dump() {\n'
    for dep in deps:
        dump += 'DEBUG_LOG_FIELD('+dep.name+')\n'
    dump += '}'
    return dump