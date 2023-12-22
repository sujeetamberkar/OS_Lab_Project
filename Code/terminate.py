from os import kill
import sys
from signal import SIGKILL
pid=sys.argv[1]
kill(int(pid),SIGKILL)
print("process terminated")
