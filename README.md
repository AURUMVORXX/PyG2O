# PyG2O

Python support for server-side scripts in [Gothic 2 Online](https://gothic-online.com.pl/).
 
## How to use
1. Download latest module version from the **Release** page
2. Unzip downloaded archive into your server directory (you should now have **PyG2O.xYY.dll**, **python312.dll** and **libs/** in your root server directory)
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
## Documentation
TBD

## QnA
**Q:** Do I need to install Python to use it?

**A:** No, Python interpreter is already inside the module and will run your code as normal, if you installed and connected the module properly.
However, if you plan to build this module yourself, you need to install Python (see *How to build* section).

**Q:** Can I use external Python libraries?

**A:** Yes, but you need to put them inside ``libs/`` folder in your server root directory.

**Q:** Can I use it as client-side module?

**A:** No, it doesn't support any client-side functionality, and there's no plans to add it for now due to security reasons and technical difficulties with C++ modules.

**Q:** Can I use it along side with Squirrel?

**A:** No, in most cases you can't. This module do call Squirrel's root table and const table directly, but there's no way to transfer data between Python and Squirrel (such as variables or class instances). 
But, if you want to use Squirrel and Python separately without data sharing, it should be ok (untested).

## How to build
**Requirements:**

CMake 21.0 +

Python 3.12+

After cloning this repository, you should init all the submodules and build CPython. You can do it via command line:
```
cd {PROJECT FOLDER}/dependencies/cpython/PCBuild/
build.bat -c Debug
```
Now, you're able to build the module with CMake. If you're using VSCode, then just open project folder and press hotkey **F7**. You should also pick the right preset (if you have x64 Python installed, then you can't build x32 module).