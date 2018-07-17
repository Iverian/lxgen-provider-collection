import importlib
import os.path
import sys
from typing import Dict, Any

from lxgen import BasicDataProvider


class PythonProvider(BasicDataProvider):
    def __init__(self, executable: str):
        BasicDataProvider.__init__(self, executable)
        sys.path.append(os.path.dirname(os.path.abspath(executable)))

    @staticmethod
    def get_short_description():
        return 'Provides data by calling function gen(dir: str, data: Dict[str, Any]) -> Dict[str, Any] from Python script'

    def __call__(self, directory: str, data: Dict[str, Any]):
        module = os.path.basename(self.get_executable()).rsplit(sep='.', maxsplit=1)[0]
        provider = importlib.import_module(module)
        return dict(provider.gen(directory, data))
