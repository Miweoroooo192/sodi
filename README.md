#  Sodi
Sodi is a basic file watcher made in python made by Miweoro (rust port soon).

## How to use Sodi?

Well for now it only can detect single files, lets say you have a C++ file, this is the file structure:
```
sodi
  \sodi_config.txt
index.cpp
main.py (sodi)
```
The `sodi_config.txt` file has this following contents:
```
Build=1
targetFile=index.cpp
```
The targetfile option specifies what file to watch (Note: The arguments shown in the targetFile option aren't the default, you have to edit it manually when you initialize a sodi project).

And the build number shows how many times you edited the file.

To make a sodi project, you need to install Python and then run `py/python/python3 main.py make` on where you installed sodi.

To run sodi on a sodi project, you need to run `py/python/python3 main.py run`.

## Plans for the future

- Make it so you can watch multiple files at once
- Make a rust (or a executable) port
