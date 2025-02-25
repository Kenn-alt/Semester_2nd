import os

# Checking the accessibility of a file

print(os.access('text.txt', os.F_OK))
print(os.access('text.txt', os.R_OK))
print(os.access('text.txt', os.W_OK))
print(os.access('text.txt', os.X_OK))