import os

from reportlab.graphics import renderPM
from PIL import Image
from lxml import etree

from aim_spacy.handler import Handler


def svg_to_png(svg_str: str = '') -> Image:
    svg_handler = Handler().svg_handler
    root = etree.fromstring(svg_str)
    drawing = svg_handler.render(root)
    pil_image = renderPM.drawToPILP(drawing)
    return pil_image


def html_to_img(html_str: str = '',
                file_name: str = 'random.png',
                size=(600, 200)) -> Image:
    html_handler = Handler().html_handler
    paths = html_handler.screenshot(html_str=html_str,
                                    save_as=file_name,
                                    size=size)
    
    for _ in paths:
        img = Image.open(file_name)
        os.remove(file_name)

    return img
