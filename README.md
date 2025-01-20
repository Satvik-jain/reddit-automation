# Reddit Automation Bot with PRAW and LLaMA 3.3

## Project Description
This project aims at automating reddit post generation based on users predefined time, it is also capable of replying to post and comments through a user friendly gradio interface.

1. **`Automated Reddit Posting`**: Posts daily content on Reddit using AI-generated text.
2. **`Automated Reddit Commenting and Replying`**: Takes a Reddit post or comment URL as input, generates an AI-based comment or reply using the LLaMA 3.3 model, and posts it automatically.

The project leverages the Reddit API via the PRAW library and integrates AI for text generation. A Gradio interface allows users to input a Reddit URL and choose between commenting on a post or replying to a thread.

---

## Installation Instructions

### 1. Clone the Repository
To clone this repository, run the following command in your terminal:
```bash
git clone https://github.com/Satvik-jain/reddit-automation/
```

### 2. Install Dependencies
After cloning the repository, navigate to the project directory and install the required dependencies using:
```bash
pip install -r requirements.txt
```

---

## Setting Up Environment Variables
This project uses a `.env` file to securely manage sensitive credentials and keys. Create a `.env` file in the root directory of the project and add the following variables:

```env
CLIENT_ID=your_reddit_client_id
SECRET_ID=your_reddit_secret_id
PASSWORD=your_reddit_password
GROQ_API_KEY=your_groq_api_key
```

- Replace `your_reddit_client_id`, `your_reddit_secret_id`, `your_reddit_password`, with the respective credentials from your Reddit account.
- Replace `your_groq_api_key` with your API key for the Groq LLaMA model.

The `praw.Reddit` instance is initialized using credentials from the `.env` file:
```python
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_ID,
    password=PASSWORD,
    user_agent="reddit_assign by u/USERNAME",
    username="<Enter your username>",
)
```

- Replace `<Enter your username>` with your reddit username.

---

## Running the Project

### 1. Start the Reddit Bot
The project includes automation for daily posting and an interactive app for generating and posting comments or replies.

#### Automate Daily Posting
To automate daily Reddit posts, run the following script:
```bash
python scheduler.py
```

#### Launch the Gradio App
To interact with Reddit posts and comments, launch the Gradio interface using:
```bash
python app.py
```

---
