from cx_Freeze import setup, Executable
import sys
 
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.
 
executables = [Executable("JogoDasPortas.py", base=base)]
 
packages = ["tkinter"]
options = {
    'build_exe': {
 
        'packages':packages,
    },
 
}
 
setup(
    name = "Jogo Das Portas",
    options = options,
    version = "1.0",
    description = 'Trabalho: Jogo em Python',
    executables = executables
)
 