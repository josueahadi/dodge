import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="SprintKart",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["AlphaKart.png"]}},
    executables=executables
)
