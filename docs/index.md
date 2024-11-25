## How to use
1. Install [Python 3.13](https://www.python.org/downloads/release/python-3130/)
*Optionally, for Windows instead of installing Python, you can download Windows embeddable package from Python download page, and extract ZIP into your server folder*
1. Download latest module version from the **Release** page
2. Unzip downloaded archive into your server directory (you should now have **PyG2O.xYY.dll** and **g2o/** in your root server directory, or similar `.so` file if you're using linux)
3. Place .DLL module in the place you want and connect it with **config.xml**
```xml
<module  src="PyG2O.x64.dll"  type="server"  />
```
4. Create **scripts/** folder in your server root directory, and put an empty ``__init__.py`` file inside it

Now, your **scripts/** folder is a Python package and serves as an entry point. You can't rename it (at least for now), but inside this folder you can use any file structure you want.

Your entry point should import PyG2O library:
```python
import g2o
# your code
```
If you make package that uses PyG2O functions, then this package also should also contain import.

## Examples
You can find default (example) scripts in [this repository](https://github.com/AURUMVORXX/PyG2O-DefaultScripts)