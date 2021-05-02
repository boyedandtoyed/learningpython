"""
reloadall.py: transitively reload nested modules
"""
import types
from importlib import reload  # from required in 3.0


def status(module):
    print('reloading ' + module.__name__)


def transitive_reload(module, visited):
    if module not in visited:  # Trap cycles, duplicates
        status(module)  # Reload this module
        reload(module)  # And visit children
        visited[module] = None
        for attrobj in module.__dict__.values():  # For all attrs
            if type(attrobj) == types.ModuleType:  # Recur if module
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


if __name__ == '__main__':
    import mr_reload  # Test code: reload myself

    reload_all(mr_reload)  # Should reload this, types
