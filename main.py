import streamlit as st
from streamlit_ace import st_ace
from transformers import pipeline

summarizer = pipeline("summarization")


def get_summary(content):
    if content:
        content_len = len(content)
        summary = summarizer(content, max_length=content_len, min_length=content_len//2, do_sample=False)
        print(f"summarized content ====== {summary[0]['summary_text']}")
        return summary[0]["summary_text"]
    else:
        return ""


LANGUAGES = [
    "text"
]

THEMES = [
    "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
    "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
    "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
    "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
    "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
    "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
]

KEYBINDINGS = [
    "emacs", "sublime", "vim", "vscode"
]


def main():
    st.sidebar.title("Summarizer")

    content = st_ace(
        placeholder=st.sidebar.text_input("Editor placeholder", value="Some placeholder."),
        language=st.sidebar.selectbox("Language mode", options=LANGUAGES, index=0),
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=31),
        keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
        font_size=st.sidebar.slider("Font size", 5, 24, 12),
        tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
        show_gutter=st.sidebar.checkbox("Show gutter", value=True),
        show_print_margin=st.sidebar.checkbox("Show print margin", value=True),
        wrap=st.sidebar.checkbox("Wrap enabled", value=False),
        auto_update=st.sidebar.checkbox("Auto update", value=True),
        readonly=st.sidebar.checkbox("Read-only", value=False, key="ace-editor"),
        key="ace-editor"
    )

    summary = get_summary(content)
    st.write(summary)


if __name__ == "__main__":
    main()
