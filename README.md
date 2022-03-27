# Purpose
This repository parses the [`*.objml` XML](https://github.com/dotnet/mbmlbook/tree/main/src/4.%20Uncluttering%20Your%20Inbox/Data) files found in [Chapter 4](https://www.mbmlbook.com/EmailClassifier.html) of [Model-Based Machine Learning](https://www.mbmlbook.com/index.html) into flat CSV files. The MBML book is an excellent source for designing probabilistic programs. Yet, with some datasets given as XML, each with a custom schema, parsing the datasets and learning from the book can add an unnecessary burden when working with the material. 

# Data 🗃️🗂️💾
The parsed `objml` XML files are stored in `data/`.

# Run
If you want to parse the data from the book's Github just run the `get_data.py` script as `python get_data.py save_data path/to/save`

## Motivation 🙌💯💪🎯
* Wanted to playaround with parsing XML files, dust off the cobwebbs, level up some skills
* Will eventually use this data for myself
* Inspired by [Omniverse's YouTube video titled Model Based Machine Learning with Pyro](https://youtu.be/lmGOQ3SRoPc), the code can be found [here](https://github.com/omniverse-labs/model-based-machine-learning)

## Wiki
I also have some notes on the [Wiki tab](https://github.com/bdatko/email_mbmlbook/wiki/Notes) 👀 ... shhh it's a secret* 🤐
