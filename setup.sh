#!/bin/sh
pip install -U "pyautogen[retrievechat]" chromadb
pip install gradio
export AUTOGEN_USE_DOCKER=False
# Not required as for now we pass everything on config array in app.ui
# export OPENAI_API_KEY=OLLAMA
# export OPENAI_API_BASE_URL="http://localhost:11434/v1/chat/completions"

curl https://arxiv.org/pdf/2308.08155 -o autogen.pdf
