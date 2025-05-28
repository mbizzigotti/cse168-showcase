import os

directory = os.getcwd();
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(".png")]
print(files)
