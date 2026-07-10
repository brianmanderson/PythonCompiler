# PythonCompiler

Utility script that byte-compiles the `Make_Raystation_Data_Structure` project (a private companion repo) into a source-free package, so the RayStation data-structure builder can be shared as `.pyc` files without distributing the `.py` source.

Personal build tool with hardcoded local paths, not a general-purpose compiler and not maintained as a library.

## How it works

`Compile.py`:

1. Wipes and recreates a `package_files/` folder inside the sibling `Make_Raystation_Data_Structure` checkout.
2. Copies in `BuildDataBase.py` and the `.py` files from `InfoStructure/`, `InfoStructure/AbstractInfoStructure/`, and `RaystationDatabaseSaver/`.
3. Runs `compileall` on the folder, deletes the `.py` sources, moves each `.pyc` out of `__pycache__` next to where its source was (stripping the `cpython-XXX` version tag), and removes the `__pycache__` folders.
4. Copies `run_builder.py` into the package as `main.py` — a two-line entry point that calls `run()` from `BuildDataBase`.

## Requirements and usage

- Python standard library only (`os`, `shutil`, `compileall`).
- Expects the companion project at a hardcoded Windows path (`C:\Users\...\Modular_Projects\Make_Raystation_Data_Structure`); edit `path_base` in `Compile.py` before running.
- The output `.pyc` files only run on the same minor Python version that compiled them.

```
python Compile.py
```
