import os
import subprocess
import sys

p = subprocess.Popen(
    [os.path.join(os.path.dirname(sys.executable), "<stdin>"), "-m", "asyncio"],
    executable=sys.executable,
    text=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
p.stdin.write("exit")
p.stdin.close()
data = p.stdout.read()
p.stdout.close()
# try to cleanup the child so we don't appear to leak when running
# with regrtest -R.
p.wait()
subprocess._cleanup()
if "unclosed event loop" in data:
    raise SystemExit(1)
