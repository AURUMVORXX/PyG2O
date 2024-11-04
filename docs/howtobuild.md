### Requirements

* **CMake** 21.0+
* **Python** 3.12+

After cloning this repository, you should init all the submodules and build CPython. You can do it via command line:
```console
cd {PROJECT FOLDER}/dependencies/cpython/PCBuild/
build.bat -c Debug
```
Now, you're able to build the module with CMake. If you're using VSCode, then just open project folder and press hotkey **F7**. You should also pick the right preset (if you have x64 Python installed, then you can't build x32 module).