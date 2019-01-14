def generate_arduino(namespaces, deps):
    package = '#pragma once\n'
    package += 'struct DATA_PACKAGE {\n'
    for dep in deps:
        package += dep.fieldTypeName+' '+dep.name+';\n'
    package += """} package;
const char* PKG_START = (char*)&package;
const int PKG_LEN = sizeof(package);"""
    
    methods = """#include "package.h"
unsigned long last_update = 0;
"""
    for ns in namespaces:
        methods += "extern void "+ns+"_initialize();\n"
        methods += "extern void "+ns+"_update();\n"
    methods += 'void initialize () {\n'
    for ns in namespaces:
        methods += ns+"_initialize();\n"
    methods += """}
void update () {\n"""
    for ns in namespaces:
        methods += ns+"_update();\n"
    methods += 'last_update = millis();\n}'
    return (package, methods)