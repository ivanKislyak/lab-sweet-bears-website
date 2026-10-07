import gradio as gr

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


def include_header():
    with gr.Row(elem_classes="custom-header"):
        gr.Markdown(f"### {os.getenv('WEBSITE_NAME', 'Website Name')}")
        gr.Button("Профиль", elem_classes="btn-nav")
        gr.Button("Выход", elem_classes="btn-nav")