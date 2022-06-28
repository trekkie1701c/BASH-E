import argparse
import os
from pathlib import Path

import time

from utils import parse_arg_dalle_version, parse_arg_save_dir, parse_arg_format, parse_arg_prompt, parse_arg_boolean, parse_arg_list
from consts import ModelSize

print("--> Starting BASH-E.  This may take several minutes, depending on model size.")

from dalle_model import DalleModel

parser = argparse.ArgumentParser(description = "BASH-E. A DALL-E app to turn your text prompts into images!")
parser.add_argument("--model_version", type = parse_arg_dalle_version, default = ModelSize.MINI, help = "Mini, Mega, or Mega_Full.  Default Mini")
parser.add_argument("--save_dir", type = parse_arg_save_dir, default = "generations", help = "Custom directory for saved images.  Default generations")
parser.add_argument("--format", type = parse_arg_format, default = "PNG", help = "Format to save images in.  Default PNG")
parser.add_argument("--interactive", type = parse_arg_boolean, default = False, help = "Interactive mode.  Prompts you to supply prompt/number of images at the start and after each set of image generation.  Ignores --num and --prompt.  Default False")
parser.add_argument("--num", type = int, default = 10, help = "Number of images to generate.  Default 10")
parser.add_argument("--prompt", type = parse_arg_prompt, default = "A quick brown fox jumping over a lazy dog", help = "Text Prompt to use")
parser.add_argument("--ascii", type = parse_arg_boolean, default = False, help = "Draw ASCII art of generated images as they're generated.")
parser.add_argument("--list", type = parse_arg_list, default ="", help = "List of prompts to run.  Ignores --num and --prompt.")
args = parser.parse_args()

if (args.ascii):
	from ascii import convert
	from PIL import Image
	convert(Image.open("RobotCreation.jpg"))

print(f"DALL-E model {args.model_version} loading...")

dalle_model = DalleModel(args.model_version)

print("Model loaded.")

def generate(prompt: str, num: int):

	print(f"Now generating {num} images from prompt [{prompt}].")


	dir_name = os.path.join(args.save_dir,f"{time.strftime('%Y-%m-%d_%H:%M:%S')}_{prompt}")
	Path(dir_name).mkdir(parents=True, exist_ok=True)

	#This could be done without a loop like this - generate_images can be called directly.  However, doing it this way means that it will save each and every image immediately after it's generated; rather than generating all the images and then saving them.

	for idx in range(num):

		generated_img=dalle_model.generate_images(prompt, 1)
		for img in generated_img:
			img.save(os.path.join(dir_name, f'{idx}.{args.format}'), format=args.format)
			if (args.ascii):
				convert(img)

			print(f"Saved {idx}.{args.format}...")


	print(f"Created {num} images from text prompt [{prompt}]")

while (args.interactive):
	print("Running in interactive mode.  Ctrl+C to quit...")
	prompt = input("Text prompt? ")
	num = int(input("Number of images? "))
	generate(prompt, num)
else:
	if args.list != "":

		for idx, string in enumerate(args.list):
			data = string.split(", ", 1)
			prompt = data[0]
			num = int(data[1])
			generate (prompt, num)
	else:
		generate(args.prompt, args.num)
