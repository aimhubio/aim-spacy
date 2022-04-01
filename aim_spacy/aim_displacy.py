from typing import NoReturn

from spacy import displacy
from aim import Image

from aim_spacy.utils import svg_to_png, html_to_img


class AimDisplaCy:
    def __init__(self, image_size=(1024, 768), **kwargs):
        self.image_size = (600, 200)


    def __call__(self, docs, style, caption='', quality=90, optimize=False):

        html = displacy.render(docs, jupyter=False, style=style, page=False)

        if style == 'dep':
            img = svg_to_png(html)
        else:
            img = html_to_img(html, size=self.image_size)

        if not img:
            raise ValueError('docs is not passed properly or the given style is not supported')

        return Image(img, caption, format='png', quality=quality, optimize=optimize)


    def serve(self, **kwargs) -> NoReturn:
        displacy.serve(docs=self.docs, **kwargs)
