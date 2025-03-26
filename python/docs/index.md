## How to use
1. Install [Python 3.13](https://www.python.org/downloads/release/python-3130/)
*Optionally, for Windows instead of installing Python, you can download Windows embeddable package from Python download page, and extract ZIP into your server folder*
1. Download latest module version from the **Release** page
2. Unzip downloaded archive into your server directory (you should now have **PyG2O.xYY.dll** and **g2o/** in your root server directory, or similar `.so` file if you're using linux)
3. Place .DLL module in the place you want and connect it with **config.xml**
```xml
<module  src="PyG2O.x64.dll"  type="server"  />
```
4. Create **pyg2o_entry/** folder in your server root directory, and put an empty ``__init__.py`` file inside it

Now, your **pyg2o_entry/** folder is a Python package and serves as an entry point. You can't rename it (at least for now), but inside this folder you can use any file structure you want.

Your entry point should import PyG2O library:
```python
import g2o
# your code
```
If you make package that uses PyG2O functions, then this package also should also contain import.

## How to change entry point name
1. Create ``pyg2o.json`` in your root server folder
2. Place this content in it and change entry point name
```json
{
    "entry": "your_entry_name"
}
```

## How to add additional packages folder
You can create ``.pth`` file in your root server folder and it will be added to your ``sys.path`` before entry point

## How to launch under venv
Create and launch ``.bat`` file with the following content
```
@echo off
CALL <path_to_your_venv>/scripts/activate.bat
G2O_Server.x64.exe
```

## Examples
You can find default (example) scripts in [this repository](https://github.com/AURUMVORXX/PyG2O-DefaultScripts)