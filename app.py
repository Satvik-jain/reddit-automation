import gradio as gr
from reddit_instance import commenting, thread

def process_comment_or_post(url, action_type):
    try:
        if action_type == "Comment":
            commenting(url)
            return f"Successfully commented on the post"
        elif action_type == "Thread":
            thread(url)
            return f"Successfully replied to the thread"
        else:
            return "Invalid action type selected."
    except Exception as e:
        return f"Error: {str(e)}"

interface = gr.Interface(
    fn=process_comment_or_post,
    inputs=[
        gr.Textbox(label="Reddit Post or Comment URL", placeholder="Enter the URL of the post or comment"),
        gr.Radio(["Comment", "Thread"], label="Action Type", value="Comment"),
    ],
    outputs="text",
    title="Reddit Bot Interface",
    description="Provide a Reddit post or comment URL and select the action type to post a comment or reply to a thread."
)

interface.launch()