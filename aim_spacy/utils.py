from tempfile import TemporaryDirectory
from typing import Optional

from reportlab.graphics import renderPM
from PIL import Image
from lxml import etree

from aim_spacy.handler import Handler


def svg_to_png(svg_str: str = '') -> Optional[Image]:
    svg_handler = Handler().svg_handler('')
    root = etree.fromstring(svg_str)
    drawing = svg_handler.render(root)
    pil_image = renderPM.drawToPILP(drawing)
    return pil_image if pil_image else None


def html_to_img(html_str: str = '', size: tuple = (600, 200)) -> Optional[Image]:
    with TemporaryDirectory() as temp_path:
        html_handler = Handler().html_handler(output_path=temp_path)
        file_name = 'sample.png'
        paths = html_handler.screenshot(html_str=html_str,
                                        save_as=file_name,
                                        size=size)
        for path in paths:
            img = Image.open(path)
            # TODO: returns only the first image
            return img

    return None
