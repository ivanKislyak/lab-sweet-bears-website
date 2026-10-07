import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from html_blocks._header import include_header

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


import gradio as gr

def render_base_page(page_title, content):
    include_header()