from svglib.svglib import SvgRenderer
from html2image import Html2Image

from aim_spacy.types import Singleton


class Handler(metaclass=Singleton):
    def __init__(self, **kwargs):
        self.html_handler = kwargs.get('html_handler') or Html2Image
        self.svg_handler = kwargs.get('svg_handler') or SvgRenderer
