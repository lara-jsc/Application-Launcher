import subprocess
import time

subprocess.Popen([r"C:\laragon\laragon.exe"])
time.sleep(2)

subprocess.Popen(r"C:\Users\Lara Joy\AppData\Local\insomnia\app-11.0.2\Insomnia.exe")
time.sleep(2)

subprocess.Popen([r"C:\Users\Lara Joy\AppData\Local\Programs\Microsoft VS Code\Code.exe", r"C:\laragon\www\crud-laravel-vue"])