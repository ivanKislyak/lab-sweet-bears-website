import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from html_blocks._header import include_header
from base import render_base_page
import gradio as gr

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


def content_page_1():
    pass

def content_page_2():
    pass

def content_page_3():
    pass

custom_css = """
.clean-image button { display: none !important; }
.clean-image .icon-container { display: none !important; }
.clean-image .image-container { padding: 0 !important; }
.clean-image { border: none !important; background: transparent !important; }
"""

with gr.Blocks(css="static/css/base.css", js="static/js/base.js") as demo:
    with gr.Tab("Главная"):
        render_base_page("Главная страница", content_page_1)
        gr.Image("static/images/page_1/logo.png", width=100, elem_classes=custom_css,
                show_label=False,
                interactive=False)

    with gr.Tab("Аналитика"):
        render_base_page("Панель управления", content_page_2)

    with gr.Tab("Настройки"):
        render_base_page("Настройки профиля", content_page_3)


if __name__ == "__main__":
    demo.launch()