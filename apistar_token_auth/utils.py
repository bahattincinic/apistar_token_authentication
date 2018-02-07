import os
import importlib
import binascii


def import_from_string(val):
    """
    Attempt to import a class from a string representation.
    """
    try:
        parts = val.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError):
        raise ImportError("Could not import '%s'" % val)


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()
