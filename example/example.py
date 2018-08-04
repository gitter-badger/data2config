import os
import sys

abspath = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(abspath)

from d2c.config import Config
from d2c.d2c import D2C

testpath = os.path.dirname(os.path.abspath(__file__))
myapppath = os.path.join(testpath, 'myapp')


def testTemplate(configpath: str):
    config = Config().load(configpath)
    d2c: D2C = D2C(config)
    d2c.doD2c()


if __name__ == "__main__":
    configpath = os.path.join(myapppath, 'config.yml')
    if len(sys.argv) == 2:
        configpath = sys.argv[1]
    testTemplate(configpath)
