from html2image.html2image import Html2Image
from svglib.svglib import SvgRenderer
from html2image import Html2Image
from aim_spacy.displacy_wrapper import AimDisplacy
from aim_spacy.handler import Handler
from spacy import displacy
from typing import List
from tqdm import tqdm
import argparse
import spacy
import aim


def load_data(data_path: str = '') -> List:
   data = []
   with open(args.data_path) as f:
      for line in f.readlines():
         data.append(line.strip())
   return data


if __name__ == '__main__':

   parser = argparse.ArgumentParser(
   description="Aim-Spacy integration Namespace"
   )

   parser.add_argument('--data_path', help='Path to textualt data file')

   parser.add_argument(
   '--remote_tracking_server',default=None,
   help="The name of the experiment to assign"
   )

   parser.add_argument(
   '--model_name',
   help="The name of the model to use"
   )

   parser.add_argument(
   '--experiment_name',
   help="The name of the experiment to assign"
   )


   args = parser.parse_args()


   experiment_name = args.experiment_name
   if args.remote_tracking_server is not None:
      remote_tracking_server = f'aim://{args.remote_tracking_server}'
      aim_run  = aim.Run(experiment = experiment_name, repo = remote_tracking_server)
   else:
      aim_run  = aim.Run(experiment = experiment_name)


   env = Handler.getInstance()
   nlp = spacy.load(args.model_name)
   html_handeler = Html2Image()
   svg_handeler = SvgRenderer('')
   aim_handler = AimDisplacy()

   env.set_attr(**{'html_handeler':html_handeler, 'svg_handeler':svg_handeler, 'aim_run':aim_run, 'aim_handeler':aim_handler})

   data = load_data(args.data_path)

   for index, text in tqdm(enumerate(data), total=len(data)):
      doc = nlp(text)
      
      if len(doc.ents) > 0:
         img_dep = aim_handler.render(doc,jupyter=False, style="dep")
         img_ner = aim_handler.render(doc, jupyter = False, style="ent", page=False)

                  
         aim_run.track(aim.Image(img_dep, caption=f'Dependecy for data: {index}'), \
            name = 'Parsing',  context = {'type':'dependency'})
         
         aim_run.track(aim.Image(img_ner, caption=f'Entity for data: {index}'), \
            name = 'Parsing',  context = {'type':'entity'})
