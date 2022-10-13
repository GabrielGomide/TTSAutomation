# Text-to-Speech Automation

TTSAutomation is a program that takes as input a text file and converts the text into MP3 audios.
<br>
It does so by using selenium to access https://fretts.com the website supports 37 different languages and a couple of different voices for every single language.
<br>
Every new line in the text file becomes a new audio.
<br>
There are already two text files in the directory if you want to test the program, one in American English and another in Brazilian Portuguese.

## How to use

Step 1: Clone this repository into your computer
<br>
Step 2: Download the Chrome driver for your version of Chrome at https://chromedriver.chromium.org/downloads, unzip the .zip file and keep the file in your Downloads directory.
<br>
Step 3: Update the part of the code where Google Chrome is initialized with the directory for the chromedriver you just downloaded
<br>
Step 4: Run the program
<br>

```shell
python3 main.py 
```

<br>
Step 5: Enter the name of your input file
<br>
Step 6: Choose the language
<br>
Step 7: Choose the voice
<br>
Step 8: Wait until all audios are downloaded


