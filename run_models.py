import retrain as r
import sys
import json
import os
from pathlib import Path

model_list = []
cur_path = Path(os.getcwd())
base_dir = cur_path.parent
code_dir = str(cur_path)
image_dir = os.path.join(base_dir, "Images")


with open("./pooMeta.json") as f:
    model_list = json.load(f)

print(model_list)

for model in model_list:
    
    model_dir = os.path.join(base_dir, "models\\"+model["model"]+"\\"+model["iteration"])

    module = model["module"]
    model_name = model["model"]
    iteration = model["iteration"]
    number_of_steps = model["number_of_steps"]
    summaries_dir = os.path.join(model_dir, model["summaries_dir"])
    output_labels = os.path.join(model_dir, model["output_labels"])
    output_graph = os.path.join(model_dir, model["output_graph"])
    random_crop = model["random_crop"]
    random_brightness = model["random_brightness"]
    sys.argv = (
        ['./retrain.py', '--image_dir', image_dir,
         '--how_many_training_steps', number_of_steps,
         '--tfhub_module', module,
         '--summaries_dir', summaries_dir,
         '--output_labels', output_labels,
         '--output_graph', output_graph,
         '--random_crop', random_crop,
         '--random_brightness', random_brightness,
         ]
    )
    r.run_app()

