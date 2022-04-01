from tempfile import TemporaryDirectory

from reportlab.graphics import renderPM
from PIL import Image
from lxml import etree

from aim_spacy.handler import Handler


def svg_to_png(svg_str: str = ''):
    svg_handler = Handler().svg_handler('')
    root = etree.fromstring(svg_str)
    drawing = svg_handler.render(root)
    pil_image = renderPM.drawToPILP(drawing)
    return pil_image if pil_image else None


def html_to_img(html_str: str = '', size: tuple = (600, 200)):
    with TemporaryDirectory() as temp_path:
        html_handler = Handler().html_handler(
            output_path=temp_path,
            custom_flags=['--disable-gpu', '--log-level=0']
        )
        # TODO: disable headless browser logging
        file_name = 'sample.png'
        paths = html_handler.screenshot(html_str=html_str,
                                        save_as=file_name,
                                        size=size)
        for path in paths:
            img = Image.open(path)
            # TODO: returns only the first image
            return img

    return None
