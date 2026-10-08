import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from html_blocks._header import include_header
from base import render_base_page
import gradio as gr

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / '.env')


custom_css = """
.clean-image button { display: none !important; }
.clean-image .icon-container { display: none !important; }
.clean-image .image-container { padding: 0 !important; }
.clean-image { border: none !important; background: transparent !important; }
"""

def content_page_1():
    gr.Markdown("### Контент главной страницы")

def content_page_2():
    gr.Markdown("### Панель управления аналитикой")

def content_page_3():
    gr.Markdown("### Настройки профиля пользователя")

with gr.Blocks(css="static/css/base.css", js="static/js/base.js") as demo:
    include_header()
    # Красивый хедер сверху
    with gr.Row(elem_classes="header-container"):
        gr.Image(
            "static/images/page_1/logo.png",
            height=250,
            show_label=False,
            interactive=False,
            elem_classes=["clean-image"]
        )
        gr.Markdown("# Мое приложение")

    with gr.Tabs():
        with gr.Tab("Главная"):
            content_page_1()
        with gr.Tab("Аналитика"):
            content_page_2()
        with gr.Tab("Настройки"):
            content_page_3()

if __name__ == "__main__":
    demo.launch()