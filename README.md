<p align="center">
<img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/woman-artist_1f469-200d-1f3a8.png" width="60" alt="Dali">
  <h2 align="center">BASH-E</h2>
</p>

A command line DALL-E Playground, based largely on the wonderful work of Sahar Mor's [DALL-E Playground](https://github.com/saharmor/dalle-playground).  Uses the open-source version of
OpenAI's [DALL-E](https://openai.com/blog/dall-e/), based on [DALL-E Mini](https://github.com/borisdayma/dalle-mini).

## Usage

1.  Clone this repo locally
2.  cd $repo/backend
3.  pip install -r requirements.txt
4.  python BASH-E.py

BASH-E takes the following arguments:

--num (number of images to generate)

--prompt (text prompt)

--format (format to use)

--save_dir (custom directory to save in)

--model_version (which version to use).  Supports mini (default), mega, and mega_full.  Mini tends to work decently on lightweight systems with little RAM and is fast enough for generation to play around with on slower CPUs.  Mega requires a decent amount of RAM (>8GB) and a GPU with sufficient VRAM to speed up the process a bit.  Mega_Full requires >12GB of RAM/VRAM, although CPU-only generation can take upwards of an hour per image.  Note that it's not currently possible to use system memory in place of insufficient VRAM unless you do not have a GPU, or otherwise do not have a GPU processing it.

Currently this is just a quick and dirty setup, and I plan on expanding more as time goes on.

The original istructions from Sahar indicated that PyConda was needed to run this; in my clearing of excess requirements I found that it wasn't necessary (at least for CPU builds) and it's not present when installing it on Colab.  However, if you run into issues it may be a place to look.

## Acknowledgements

This Repo is laregly a fork of [Sahar Mor's](https;//github.com/saharmor) Dall-E Playground repository.  I'm not a skilled coder, and a lot of the Python that I've learned in here is either a modification from it, directly from there, or at least, used as a framework for later code.

The repo this was based on is a full-stack flavour of [Boris Dayma's](https://github.com/borisdayma) DALL-E Mini
repository. 
