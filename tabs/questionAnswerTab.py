import gradio as gr
import requests


def qa(url, q):
    try:
        headers = {'Content-Type': 'application/json',}
        return requests.post(url, data={"query": q, "lang": "en"}, headers=headers).json()
    except Exception as e:
        return e
    
   

with gr.Blocks() as questionAnswerTab:
    with gr.Row():
        question = gr.TextArea(
            label='Question', value='Where is the birthplace of Angela Merkel')
        result = gr.JSON(label='Answer', interactive=False)
    with gr.Row():
        link = gr.Text(label="URL", value='http://localhost:8080/qa')
        qaRun = gr.Button(variant='primary')

    qaRun.click(fn=qa, inputs=[link, question], outputs=result)
