# Squirrel module template

## Table of contents

- [Usage requirements](#usage-requirements)
- [Build requirements](#build-requirements)
- [Build instructions](#build-instructions)
- [CMake options](#cmake-options)
- [Loading client module](#loading-client-module)
- [Loading server module](#loading-server-module)

## Usage requirements

**_NOTE:_** Client modules aren't downloaded by default.

In order to use the module, the user have to install: \
[Microsoft Visual C++ 2015-2019 Redistributable (x86)](https://aka.ms/vs/16/release/vc_redist.x86.exe) \
This package is essential only for **Windows** platform.

## Build requirements

**_NOTE:_**  Some of the requirements like _IDE_ or _compiler_ are just recommendation

In order to compile the module, you have to meet some \
essential requirements,
depending on the target platform.

### Windows

- Visual Studio, 2015+ (recommended [2019 Community Edition](https://visualstudio.microsoft.com/pl/thank-you-downloading-visual-studio/?sku=Community&rel=16))
    
    Visual Studio Components
    * Windows SDK
    * one of the following toolsets, pick one: v140, v141, v142 (recommended v142)
    * (Optional) CMake Tools for Visual Studio
- [CMake 3.17+](https://cmake.org/download/)

### Linux

- g++ compiler
- [CMake 3.17+](https://cmake.org/download/)

## Build instructions

### Windows

#### Visual Studio with CMake tools

- open a local folder using Visual Studio
- build the project

#### Visual Studio without CMake tools

- open command line in repo-directory
- type ``mkdir build``
- type ``cd build``
- type ``cmake ..``
- open visual studio .sln and compile the project
- alternatively if you want to build from command line instead, \
    type ``cmake --build .``

### Linux

- open terminal in repo-directory
- type ``mkdir build``
- type ``cd build``
- type ``cmake ..``
- type ``cmake --build .``

## CMake options

This project has some configurable options.  

### Cache options

Cache options are stored inside **CMakeCache.txt** inside generated CMake build folder.  
You can set these options, by either manually editing the file, or by using cmake-gui.

- **GAME_PATH** this cache option allows you to setup the destination  
    where module will be installed. If it's set to some value, it will  
    generate an installation step. by default it's set to ``""`` (disabled).

- **SERVER_PATH** this cache option allows you to setup the destination  
    where module will be installed. If it's set to some value, it will  
    generate an installation step. by default it's set to ``""`` (disabled).

- **INSTALL_AFTER_BUILD** this cache option allows you to run  
    cmake install step after a successfull build.  
    By default it's disabled.

## Loading client module

### Global (client modules will be shared across multiple servers)

**_NOTE:_** You always gives a path to a module relative to a .xml file. \
**_NOTE:_** The client module must be located in top server directory. \
**_NOTE:_** The client module must be located in Game/Multiplayer/Modules directory. \
**_NOTE:_** This approach can cause problems when different server is using older/newer version \
of the client module. 

To load your module, you have to add reference in .xml file (for example: __config.xml__).

```xml
<module src="NameOfTheModule.dll" type="client" />
```

### Server specific

**_NOTE:_** You always gives a path to a module relative to a .xml file. \
**_NOTE:_** The client module must be located in ServerFolder/YourServerName. \
**_NOTE:_** The client module must be located in Game/Multiplayer/Modules/YourServerName directory.

Loading client module this way will help you to prevent situations when different \
server is using the older/newer version of the module than yours.

To load your module, you have to add reference in .xml file (for example: __config.xml__).

```xml
<module src="YourServerName/NameOfTheModule.dll" type="client" />
```

# Loading server module


**_NOTE:_** You always gives a path to a module relative to a .xml file.

You can put your server module in any directory you want, only client modules \
must be placed in specific directories.

To load your module, you have to add reference in .xml file (for example: __config.xml__).

```xml
<!-- For windows server -->
<module src="NameOfTheModule.dll" type="server" />
<!-- For linux server -->
<module src="./NameOfTheModule.so" type="server" />
```