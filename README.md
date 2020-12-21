# SmartSTT
So what we have done is a simple execution of a python based voice assistant which converts the speech into text.

Alex.py is our speech to text assistant code which we did using python. So the modules which are required for this are  
speech recognition (to recognise speech)
playsound # to play an audio file
from gtts import gTTS # google text to speech
random
from time import ctime # get time details
webbrowser # open browser
yfinance as yf # to fetch financial data
ssl
certifi
time
os # to remove created audio files 
To download these packages first go to your command prompt (run as administrator). We will use the pip tool which is basically used to install python modules.
Now use the command pip install <<module_name>> ,this will download the package from the internet (basically from the python package index) and install it in the local drive.
Now we can import the modules that are required.
So first the recognizer is initialised then we are defining a function record_audio which will listen to the audio and convert it into the text.We will be using the microphone as the source.After listening for the audio via source, it converts audio into text. We used the try/except for error handling i.e in case of any audio related error it will simply print the error message. We have also included different functionalities.  

main.py is our driver function .We import all the required modules using the import <<module_name>> statement.Firstly, the recognizer is initialised.Then we are defining a function SpeakText() to convert text to speech which takes a command as a parameter .An infinite loop gets intialised when the engine is initialised, for user to speak. Use the microphone as source for input. Wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level. After listening to the user's input it uses google to recognize the audio. After listening it sends a notification to the driver. To terminate the loop process the user simply has to say stop which will make it to break out of the loop.
 


