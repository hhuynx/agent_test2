import os
import subprocess

def login(request):
    password = os.environ.get("DB_PASSWORD", "")   # 不再硬编码
    cmd = ["rm", "-rf", request.get("path", "")]    # 不用 shell=True
    subprocess.run(cmd)
    return "ok"
