<p align="center">
<img src="https://raw.githubusercontent.com/trekkie1701c/BASH-E/522540b5398b0ca98ea44ce738534821ec7c6890/backend/RobotCreation.jpg" width="256" alt="BASH-E">
  <h2 align="center">BASH-E</h2>
</p>

A command line DALL-E Playground, based largely on the wonderful work of Sahar Mor's [DALL-E Playground](https://github.com/saharmor/dalle-playground).  Uses the open-source version of
OpenAI's [DALL-E](https://openai.com/blog/dall-e/), based on [DALL-E Mini](https://github.com/borisdayma/dalle-mini).

## Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/trekkie1701c/BASH-E/blob/main/backend/BASH-E%20Notebook.ipynb)

Google Colab restricts usage based both on tier and recent personal usage; if you've never used colab before, you may be able to run mega_full for free, although after some time you won't be allocated powerful enough systems for this, or at least, will be unlikely to.  Conversely, if you run this for several hours even with a Pro+ subscription, you may find yourself allocated a system that doesn't have sufficient memory to run mega_full, and you'll need to wait a few hours before you can try again.

Note that only Pro+ offers background execution, although runtimes will be destroyed after 24 hours regardless.

Currently there's no way to automatically have Colab destroy a runtime when all execution is complete, so you'll want to make sure to check up on it and delete the runtime when you're done so that you don't waste resources and get throttled.

## Local Usage

1.  Clone this repo locally
2.  cd $repo/backend
3.  pip install -r requirements.txt
4.  python BASH-E.py

BASH-E takes the following arguments:

--num (number of images to generate).  Default is 10.

--prompt (text prompt).  Defaults "The Quick Brown Fox Jumps over the Lazy Dog"

--format (format to use).  Defaults PNG.

--save_dir (custom directory to save in).  Default generations subdirectory of whatever your current working directory is.

--model_version (which version to use).  Supports mini (default), mega, and mega_full.

--interactive (run in interactive mode).  True/False.  May not work in Colab.  Default False.

--ascii (draw ascii art as images are generated). True/False.  Default False.  Does not work in Colab.

## Which Model do I use?

Currently there are three models to choose from:

-Mini, which requires the least amount of compute resources.  I can comfortably run it on a system with 8 gigs of RAM, no GPU, and get an image in around 5-10 minutes or so.  Image quality can be lacking, particularly for more complex requests however.

-Mega, which requires a modest amount of compute resources.  If you have a non-laptop GPU from the last couple of years you can probably run this one.  Has significantly better image results.

-Mega Full, which requires the most compute resources (>12 GB of memory).  Generally you'll want a newer GPU, or you'll want to have something like a Google Colab Pro+ subscription in order to run this.

## Notes

Currently this is just a quick and dirty setup, and I plan on expanding more as time goes on.  This was made primarily because I found myself wanting to generate many hundreds to thousands of images at once from a single prompt for various reasons, and although Sahar's work is great for seeing images as they're generated and trying out a bunch of different prompts rapidly, it's a little cumbersome when you want to actually generate a lot of images at once, and several things on it don't work if you want to generate more than 5 images on mega_full with Google Colab.

The original istructions from Sahar indicated that PyTorch was needed to run this; in my clearing of excess requirements I found that it wasn't necessary (at least for CPU builds) and it's not present when installing it on Colab.  However, if you run into issues it may be a place to look.

## Acknowledgements

This Repo is laregly a fork of [Sahar Mor's](https://github.com/saharmor) Dall-E Playground repository.  I'm not a skilled coder, and a lot of the Python that I've learned in here is either a modification from it, directly from there, or at least, used as a framework for later code.

The repo this was based on is a full-stack flavour of [Boris Dayma's](https://github.com/borisdayma) DALL-E Mini
repository. 
