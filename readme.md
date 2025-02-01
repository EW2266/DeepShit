# DeepShit
python script developed to use locally hosted DeepSeek for Toxic Translation.
Tested with LM Studio

## How it works
After typing a message in the in-game chat, use the default hotkey "**alt + t**" to initiate the translation.
The message user typed in will be converted to "Translating" during translation process.
The returned message will be replace "Translating" when given.
![](https://github.com/EW2266/DeepShit/blob/main/test.gif)

## To Run the Script
Clone this repo and run the following command to download the required dependencies.
> pip install -r "requirements.txt"


## LM Studio Settings
### System Prompt
You are my translator in Dota 2. Translate what I say into Spanish, but make it sound like an uneducated, rude, and toxic Peruvian person. Use short sentences, no more than 4 or 5 words each. If the response needs to be longer, break it up into separate lines or sections, just like how people type in in-game chat Keep it simple, rough, mean and do not type any symbols!

Tested with deepseeek-r1-distill-llma-8b
