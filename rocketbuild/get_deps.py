import re

DEP_REGEX = re.compile(r'^\s*#include <(\w+)\.h>\s+///(\S+)', re.MULTILINE)
def get_deps(inoFile):
    ret = []
    for match in re.finditer(DEP_REGEX, inoFile):
        ret.append(match.group(2))
    return ret