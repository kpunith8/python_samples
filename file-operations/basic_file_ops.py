from pathlib import Path

path = Path()  # Points to current directory if nothing passed

# To get all .py files in the current directory, pass * to get everything
for file in path.glob('*.py'):
    print(file)
