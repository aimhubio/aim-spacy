from typing import NoReturn

from spacy import displacy
from aim import Image

from aim_spacy.utils import svg_to_png, html_to_img


class AimDisplaCy(Image):
    def __init__(self, docs, style, caption='', quality=90, optimize=False):
        self.docs = docs
        self.style = style

        image_size = (600, 200)
        html = displacy.render(self.docs, jupyter=False, style=style, page=False)

        if style == 'dep':
            img = svg_to_png(html)
        else:
            img = html_to_img(html, size=image_size)

        if not img:
            raise ValueError('docs is not passed properly or the given style is not supported')

        super().__init__(img, caption, format='png', quality=quality, optimize=optimize)

    def serve(self, **kwargs) -> NoReturn:
        displacy.serve(docs=self.docs, **kwargs)
