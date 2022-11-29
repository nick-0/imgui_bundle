"""Markdown for ImGui
Python bindings for https://github.com/mekhontsev/imgui_md (with an additional custom wrapper)
"""

from typing import Optional, Callable
from imgui_bundle.imgui import ImTextureID, ImVec2, ImVec4


# using VoidFunction = std::function<void(void)>;
# using StringFunction = std::function<void(std::string)>;
# using HtmlDivFunction = std::function<void(const std::string& divClass, bool openingDiv)>;
# using MarkdownImageFunction = std::function<std::optional<MarkdownImage>(const std::string&)>;

VoidFunction = Callable[[None], None]
StringFunction = Callable[[str], None]
HtmlDivFunction = Callable[[str, bool], None]
MarkdownImageFunction = Callable[[str], MarkdownImage]


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imgui_md_wrapper.h>    ####################
class MarkdownFontOptions:
    font_base_path: str = "fonts/Roboto/Roboto"
    max_header_level: int = 3
    size_diff_between_levels: float = 3.0
    regular_size: float = 14.0

class MarkdownImage:
    texture_id: ImTextureID
    size: ImVec2
    uv0: ImVec2
    uv1: ImVec2
    col_tint: ImVec4
    col_border: ImVec4

def on_image_default(image_path: str) -> Optional[MarkdownImage]:
    pass

def on_open_link_default(url: str) -> None:
    pass

class MarkdownCallbacks:
    # The default version will open the link in a browser iif it starts with "http"
    on_open_link: StringFunction = on_open_link_default

    # The default version will load the image as a cached texture and display it
    on_image: MarkdownImageFunction = on_image_default

    # OnHtmlDiv does nothing by default, by you could write:
    #     In  C++:
    #        markdownOptions.callbacks.onHtmlDiv = [](const std::string& divClass, bool openingDiv)
    #        {
    #            if (divClass == "red")
    #            {
    #                if (e)
    #                    ImGui::PushStyleColor(ImGuiCol_Text, IM_COL32(255, 0, 0, 255));
    #                else
    #                    ImGui::PopStyleColor();
    #            }
    #        };
    on_html_div: HtmlDivFunction

class MarkdownOptions:
    font_options: MarkdownFontOptions
    callbacks: MarkdownCallbacks

def initialize_markdown(options: MarkdownOptions = MarkdownOptions()) -> None:
    """InitializeMarkdown: Call this once at application startup
    Don't forget to later call GetFontLoaderFunction(): it will return a function that you should call
    during ImGui initialization (and before rendering the first frame, since it will load the fonts)

    If using HelloImGui, the code would look like:
        Python:
           runner_params = hello_imgui.RunnerParams()

           ... // Fill runner_params callbacks

           # Initialize markdown and ask HelloImGui to load the required fonts
           imgui_md.initialize_markdown()
           runner_params.callbacks.load_additional_fonts = imgui_md.get_font_loader_function()

           hello_imgui.run(runnerParams)
    """
    pass

def get_font_loader_function() -> VoidFunction:
    """GetFontLoaderFunction() will return a function that you should call during ImGui initialization."""
    pass

def render(markdown_string: str) -> None:
    pass
####################    </generated_from:imgui_md_wrapper.h>    ####################

# </litgen_stub> // Autogenerated code end!
