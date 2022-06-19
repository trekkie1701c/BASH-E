import argparse
import os
from pathlib import Path
from io import BytesIO
import time

from utils import parse_arg_dalle_version, parse_arg_save_dir, parse_arg_format, parse_arg_terminate, parse_arg_num, parse_arg_prompt
from consts import ModelSize

print("--> Starting BASH-E.  This may take several minutes, depending on model size.")

from dalle_model import DalleModel

parser = argparse.ArgumentParser(description = "BASH-E. A DALL-E app to turn your text prompts into images!")
parser.add_argument("--model_version", type = parse_arg_dalle_version, default = ModelSize.MINI, help = "Mini, Mega, or Mega_Full.  Default Mini")
parser.add_argument("--save_dir", type = parse_arg_save_dir, default = "generations", help = "Custom directory for saved images.  Default generations")
parser.add_argument("--format", type = parse_arg_format, default = "JPEG", help = "Format to save images in.  Default PNG")
parser.add_argument("--terminate", type = parse_arg_terminate, default = False, help = "Terminate when complete?  Default No")
parser.add_argument("--num", type = parse_arg_num, default = 10, help = "Number of images to generate.  Default 10")
parser.add_argument("--prompt", type = parse_arg_prompt, default = "A quick brown fox jumping over a lazy dog", help = "Text Prompt to use")
args = parser.parse_args()

print(f"DALL-E model {args.model_version} loading...")

dalle_model = DalleModel(args.model_version)

print(f"Model loaded.  Now generating {args.num} images from prompt [{args.prompt}].")

generated_imgs=dalle_model.generate_images(args.prompt, args.num)

print("Generation Completed.  Saving images...")

dir_name = os.path.join(args.save_dir,f"{time.strftime('%Y-%m-%d_%H:%M:%S')}_{args.prompt}")
Path(dir_name).mkdir(parents=True, exist_ok=True)

for idx, img in enumerate(generated_imgs):
	img.save(os.path.join(dir_name, f'{idx}.{args.format}'), format=args.format)
	print(f"Saved {idx}.{args.format}...")

print(f"Created {args.num} images from text prompt [{args.prompt}]")
