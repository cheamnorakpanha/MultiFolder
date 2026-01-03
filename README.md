## Overview
- **Purpose**: Instructions to rebuild the `export.exe` and `import.exe` executables from the repository using PyInstaller.

## Prerequisites
- **Python**: 3.13 (the environment used here was Python 3.13.7).
- **PyInstaller**: installed in the active Python environment (used PyInstaller 6.16.0).
- **Workspace**: repository root contains the `EXP` and `IMP` folders.

## Rebuild Steps
- **Export EXE**: Run PyInstaller with the provided spec in the `EXP` folder.

```powershell
cd EXP
pyinstaller export.spec
```

- **Import EXE**: Run PyInstaller with the provided spec in the `IMP` folder.

```powershell
cd IMP
pyinstaller import.spec
```

## Run & Test
- **Run built EXEs**: The built executables are placed in the `dist` directories.

```powershell
EXP\dist\export.exe
IMP\dist\import.exe
```
