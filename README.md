**Project name: LLM Chat Host / LLM Chat Web Application**

**Notice!!!:** Code comments are pending review and are **NOT** necessarily a reliable code description in all parts of the project.

**Description:** Python Flask server which hosts a Large Language Model Chat via Ollama. 
<br>**Motivation:** This project was created as a part of a work experience internship with Elucidat (https://www.elucidat.com/).

**Main Dependencies:** 
<br>The Python **Flask** Module: (https://github.com/pallets/flask)
<br>The Python **Ollama** Module: (https://github.com/ollama/ollama)

________________________________________________________________
**Usage Instructions:** <br>
<br>**Starting -** Download Main without changing its internal file organisation structure, run Flaskserver.py and open "http://127.0.0.1:5000" in your web browser.
It is recommended to open Flaskserver in a code editor when you do this so that the python terminal outputs are easily available - the terminal provides information not currently displayed in the web page such as LLM model pulling progress messages.
<br><br>**Pulling LLMs -** Type the model name in the text box on the left ("Selected model: "), then press the "Pull" button. Wait for an alert to pop up indicating that the Pull has finished. It is recommended to check the terminal to confirm that the Pull has started
<br><br>**Finding LLMs to Pull -** Press the "Open Models Library" button or go to "https://ollama.com/library". A comprehensive, searchable and filterable list of LLMs is available here. 
<br>*LLM Pulling Example:* To pull the first LLM in the list, "deepseek-r1" as of the creation of this guide, click on the name of the LLM to navigate to the versions list. It is recommended to select a reasonably sized model as larger models require large amounts of processing power/time. Copy the LLM name from the name column and paste it into the "Selected model: " text box in the website.
<br><br>**Querying your model -** Type your query into the "Enter text here..." input and then press the "Submit Text" button, the output will appear in the space below the button. Depending on the model size, the output may take some time. **NOTE:** The output box is scrollable; if you do not see an output, try scrolling down inside the output box.
<br><br>**Additional Info -** The LLM is given a memory which holds the last 5 user inputs and LLM outputs. This can easily be altered by changing the memory stack sizes in 'Flaskserver.py'. The memory is sent with the user query for each query sent, this may cause the outputs of some LLM models to include unexpected information.
________________________________________________________________

**Contribution:** This project has been retired for the foreseeable future, if you wish to contribute you should pull the code and work on your own version (but credit me for providing code). <br>
If you wish to use the code for a different project, feel free to do so without crediting me. <br>For more specifics, see License (below).

**License:** This work is licensed under a Creative Commons Attribution 4.0. <br> For License TL:DR see Contribution (above), or for License details see: https://creativecommons.org/licenses/by/4.0/ 
