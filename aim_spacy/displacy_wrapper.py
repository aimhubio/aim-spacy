from PIL import Image
from spacy import displacy
from typing import List, NoReturn
from aim_spacy.utils import svg_to_png, html_to_img


class AimDisplacy:
    def __init__(self, size=(600, 200)):
        self.displacy_module = displacy
        self.image_size = size

    def render(self, docs, **kwargs) -> Image:
        html = self.displacy_module.render(docs, **kwargs)

        if kwargs['style'] == 'dep':
            img = svg_to_png(html)
        else: 
            img = html_to_img(html, size=self.image_size)

        return img

    def serve(self, docs, **kwargs) -> NoReturn:
        self.displacy_module.serve(docs=docs, **kwargs)
