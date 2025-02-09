# Debug native C++ in python scripts

ImGui Bundle provides tooling to help you debug the C++ side, when you encounter a bug that is difficult to diagnose from Python.

It can be used in two steps:

1.  Edit the file `pybind_native_debug/pybind_native_debug.py`. Change its content so that it runs the python code you would like to debug. Make sure it works when you run it as a python script.

2.  Now, debug the C++ project `pybind_native_debug_bundle` which is defined in the directory `pybind_native_debug/`. This will run your python code from C++, and you can debug the C++ side (place breakpoints, watch variables, etc).

Example: [this issue on macOS](https://github.com/pthom/hello_imgui/issues/33) was solved thanks to this.
