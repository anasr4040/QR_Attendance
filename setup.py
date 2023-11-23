from cx_Freeze import setup, Executable

executables = [
    Executable("GUI.py")
]

setup(name = 'Attendance_System',
      version = '0.1',
      executables = executables
       )