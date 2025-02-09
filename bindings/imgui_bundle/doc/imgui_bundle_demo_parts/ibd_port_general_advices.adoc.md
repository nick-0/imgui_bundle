# General advices

ImGui is a C++ library that was ported to Python. In order to work with it, you will often refer to its [manual](https://pthom.github.io/imgui_manual_online/manual/imgui_manual.html), which shows example code in C++.

In order to translate from C++ to Python:

1.  Change the function names and parameters\' names from `CamelCase` to `snake_case`

2.  Change the way the output are handled.

    a.  in C++ `ImGui::RadioButton` modifies its second parameter (which is passed by address) and returns true if the user clicked the radio button.

    b.  In python, the (possibly modified) value is transmitted via the return: `imgui.radio_button` returns a `Tuple[bool, str]` which contains `(user_clicked, new_value)`.

3.  if porting some code that uses static variables, use the `@immapp.static` decorator. In this case, this decorator simply adds a variable `value` at the function scope. It is preserved between calls. Normally, this variable should be accessed via `demo_radio_button.value`, however the first line of the function adds a synonym named static for more clarity. Do not overuse them! Static variable suffer from almost the same shortcomings as global variables, so you should prefer to modify an application state.

## Example:

C++

``` cpp
void DemoRadioButton()
{
    static int value = 0;
    ImGui::RadioButton("radio a", &value, 0); ImGui::SameLine();
    ImGui::RadioButton("radio b", &value, 1); ImGui::SameLine();
    ImGui::RadioButton("radio c", &value, 2);
}
```

Python

``` python
@immapp.static(value=0)
def demo_radio_button():
    static = demo_radio_button
    clicked, static.value = imgui.radio_button("radio a", static.value, 0)
    imgui.same_line()
    clicked, static.value = imgui.radio_button("radio b", static.value, 1)
    imgui.same_line()
    clicked, static.value = imgui.radio_button("radio c", static.value, 2)
```
