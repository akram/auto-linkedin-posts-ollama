import autogen
import chromadb
from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import gradio

def autogen_chat( pdf_path, query):
    config_list = [
        {
            "model": "openhermes",
            "base_url": "http://localhost:11434/v1",
            "api_key": "NotRequired", # Not needed
        }
    ]

    llm_config_proxy = {
        "temperature": 0,
        "config_list": config_list,
    }

    assistant = AssistantAgent(
        name="assistant",
        llm_config=llm_config_proxy,
        system_message="""You are a helpful assistant. Provide accurate answers based on the context. Respond "Unsure about answer" if uncertain.""",
    )

    user = RetrieveUserProxyAgent(
        name="user",
        human_input_mode="NEVER",
        system_message="Assistant who has extra content retrieval power for solving difficult problems.",
        max_consecutive_auto_reply=10,
        retrieve_config={
            "task": "code",
            "docs_path": ['./autogen.pdf'],
            "chunk_token_size": 1000,
            "model": config_list[0]["model"],
            "client": chromadb.PersistentClient(path='/tmp/chromadb'),
            "collection_name": "pdfreader",
            "get_or_create": True,
        },
        code_execution_config={"work_dir": "coding"},
    )

    user_question = """
    Compose a LinkedIn post on {query} from {pdf_path}.
    Craft an introduction, main body, and a compelling conclusion. 
    Encourage readers to share the post. Keep the post under 500 words.
    Return in markdown format.
    """
    user_question = user_question.format(query=query, pdf_path=pdf_path)


    response = user.initiate_chat(
        assistant,
        problem=user_question,
    )
    messages = user.chat_messages[assistant]
    last_message = messages[-1]["content"]
    return last_message



js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""


iface = gradio.Interface( 
    fn=autogen_chat,
    inputs=[ gradio.Textbox(label="Path to PDF", placeholder="Enter PDF path"),
           gradio.Textbox(label="Topic", placeholder="Enter the topic of the post") ],
    outputs=gradio.Textbox(label="Assistant's response"),
    title="Autogen Assistant Chat",
    description="Enter a PDF path to get an answer from Autogen Assistant Chat",
    js=js_func
)

iface.launch(share=True)


