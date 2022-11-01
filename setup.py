from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "colorama", "iqoptionapi"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="teste",
    options=options,
    version="1.0.0",
    description='teste',
    executables=executables
)
