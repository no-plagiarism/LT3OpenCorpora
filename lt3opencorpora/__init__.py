__version__ = '0.2.1'

try:
    from .convert import Dictionary
except ImportError:
    # To make setup.py work
    pass
