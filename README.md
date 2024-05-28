# AutoGen agents to created linkedin posts from a PDF document

AutoGen agents to created linkedin posts from a PDF document. It uses ollama local 
agent instead of OpenAPI.
The model used for testing is `openhermes2` here. But other models may give better results.

## Credits
Inspired by https://www.youtube.com/watch?v=B_-AaxswV6o&t=315s

## Install
Install the requirements by running the script setup.sh

```
./setup.sh
```

It will install `AutoGen`, `chromadb` and `gradio` and download a sample pdf file use for the article generation.

## Run
### Command line
Just run  `app.py`:
```
python app.py
```

### Web UI
for a web based version run `ui.py`:
```
python ui.py
```

And then click on the link in terminal to open it in your browser.


