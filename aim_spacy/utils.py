from reportlab.graphics import renderPDF, renderPM
from aim_spacy.handler import Handler
from lxml import etree
from PIL import Image
import os
import io


def svg_to_png(svg_str: str = '') -> Image:
    svg_handeler = Handler.getInstance().svg_handeler
    root = etree.fromstring(svg_str)
    drawing = svg_handeler.render(root)
    png_PIL = renderPM.drawToPILP(drawing)
    return png_PIL


def html_to_img(html_str: str = '',
                file_name: str = 'random.png',
                size=(600, 200)) -> Image:
    html_handeler = Handler.getInstance().html_handeler
    paths = html_handeler.screenshot(html_str=html_str,
                                     save_as=file_name,
                                     size=size)
    
    for path in paths:
        img = Image.open(file_name)
        os.remove(file_name)

    return img
