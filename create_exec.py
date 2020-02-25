
import subprocess, os, shutil

subprocess.call("pyinstaller code.py --onefile")

shutil.rmtree("build")
if os.path.exists("__pycache__"):
    shutil.rmtree("__pycache__")

src_path = 'dist/'
dest_path='malwares/'
# dest_path='C:/malwares/'
f = 'code.exe'
if os.path.exists(dest_path):
    shutil.rmtree(dest_path)
    os.makedirs(dest_path)  
else:
    os.makedirs(dest_path)

shutil.move(src_path + f, dest_path)

os.rmdir("dist")
os.remove("code.spec")
os.remove("code.py")

os.rename(os.path.join(dest_path, f), os.path.join(dest_path, "malware.exe"))