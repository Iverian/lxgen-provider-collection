import json
import os.path
import shutil
import subprocess
from typing import Dict, Any

from lxgen import BasicDataProvider


def locate_wolfram_kernel():
    env = 'WOLFRAMSCRIPT_KERNELPATH'
    if not os.getenv(env):
        os.putenv(env, shutil.which('wolfram'))


class WolframProvider(BasicDataProvider):
    def __init__(self, executable: str):
        BasicDataProvider.__init__(self, executable)
        locate_wolfram_kernel()

    @staticmethod
    def get_short_description():
        return 'Provides data by calling wolfram script from command line'

    def __call__(self, directory: str, data: Dict[str, Any]) -> Dict[str, Any]:
        result = subprocess.run(['wolframscript', '-file', self.get_executable(), directory, json.dumps(data)],
                                stdout=subprocess.PIPE, check=True, shell=True).stdout
        print(result)
        return json.loads(result)
