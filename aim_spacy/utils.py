import sys
from tempfile import TemporaryDirectory
from reportlab.graphics import renderPM
from PIL import Image
from lxml import etree

from aim_spacy.handler import Handler
from spacy.tokens import DocBin
from spacy import Language


def svg_to_png(svg_str: str = ''):
    svg_handler = Handler().svg_handler('')
    root = etree.fromstring(svg_str)
    drawing = svg_handler.render(root)
    pil_image = renderPM.drawToPILP(drawing)
    return pil_image if pil_image else None


def html_to_img(html_str: str = '', size: tuple = (600, 200)):
    flags = []
    with TemporaryDirectory() as temp_path:
        flags.append("--enable-logging=/dev/null")
        flags.append("--headless")
        flags.append("--no-sandbox")
        flags.append("--disable-logging")
        flags.append("--v=-3")

        html_handler = Handler().html_handler(
            output_path=temp_path,
            custom_flags=flags
        )
        file_name = 'sample.png'
        paths = html_handler.screenshot(html_str=html_str,
                                        save_as=file_name,
                                        size=size)

        for path in paths:
            img = Image.open(path)
            return img

    return None

def docbin_to_doc(docbin_path: str = None, nlp: 'Language' = None):
    docbin = DocBin()
    data = docbin.from_disk(docbin_path)
    docs = list(data.get_docs(nlp.vocab))
    return docs