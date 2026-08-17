await pyodide.loadPackagesFromImports(code);
await pyodide.runPythonAsync(code);

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Shape:", a.shape)
print("Mean:", a.mean())
print("Transpose:")
print(a.T)

print("Matrix multiplication:")
print(a @ a)

print("Eigenvalues:")
print(np.linalg.eigvals(a))