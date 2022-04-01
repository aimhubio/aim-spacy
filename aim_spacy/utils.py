import sys
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
    flags = []
    with TemporaryDirectory() as temp_path:
        flags.append("--disable-extensions")
        flags.append("--disable-in-process-stack-traces")
        flags.append("--disable-logging")
        flags.append("--disable-dev-shm-usage")
        # flags.append("--log-level=3")
        flags.append("--output=/dev/null")
        flags.append("--disable-gpu")
        flags.append("--headless")
        flags.append("--no-sandbox")
        flags.append("--disable-logging")
        # flags.append("--disable-software-rasterizer")


        html_handler = Handler().html_handler(
            output_path=temp_path,
            custom_flags=flags
        )
        file_name = 'sample.png'
        paths = html_handler.screenshot(html_str=html_str,
                                        save_as=file_name,
                                        size=size)

        print(paths)
        for path in paths:
            img = Image.open(path)
            return img

    return None
