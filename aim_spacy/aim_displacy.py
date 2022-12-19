from typing import NoReturn

from spacy import displacy
from aim import Image

from aim_spacy.utils import svg_to_png, html_to_img


class AimDisplaCy:
    def __init__(self, image_size=(200, 200), **kwargs):
        self.image_size = image_size
        self.options = kwargs


    def __call__(self, docs, style, caption='', quality=90, optimize=False):

        image_list = []

        self.options.update(dict(jupyter=False, style=style, page=False))
        for doc in docs:
            html = displacy.render(doc, jupyter=False, style=style, page=False, options=self.options)

            if style == 'dep':
                img = svg_to_png(html)
            else:
                img = html_to_img(html, size=self.image_size)

            if not img:
                raise ValueError('docs is not passed properly or the given style is not supported')

            image_list.append(Image(img, caption, format='png', quality=quality, optimize=optimize))

        return image_list


    def serve(self, **kwargs) -> NoReturn:
        displacy.serve(docs=self.docs, **kwargs)