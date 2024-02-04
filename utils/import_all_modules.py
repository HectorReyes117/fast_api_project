import pkgutil
import importlib


def import_all_modules(package_name):
    package = __import__(package_name, fromlist=[""])

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        importlib.import_module(f"{package_name}.{module_name}")
