from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

root_agent = Agent(
   # A unique name for the agent.
   name="news_agent",
   # The Large Language Model (LLM) that agent will use.
   # Please fill in the latest model id that supports live from
   # https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models
   model="gemini-2.0-flash",  # for example: model="gemini-2.0-flash-live-001" or model="gemini-2.0-flash-live-preview-04-09"
   # A short description of the agent's purpose.
   description="Agent to find latest news articles on a given topic.",
   # Instructions to set the agent's behavior.
   instruction="""You are a news search agent. Your task is to find the latest news articles on a given topic. Use the provided tools to perform searches and gather information. You need to gather only the top 20 latest news search results from Google. The result we want is in json format with the list of articles in an array of object with object containing title of the article, url of the article, and a short description of the article, and the date of the article.
                  Output Format (JSON):

                  {
                     "news": [
                        {
                              "title": "<Title of the article>",
                              "url": "<URL of the article>",
                              "description": "<Short description of the article>",
                              "date": "<Date of the article>",
                              "content": "<Detailed summary of the article in at least 200 words>"
                        },
                        {
                              "title": "<Title of the article>",
                              "url": "<URL of the article>",
                              "description": "<Short description of the article>",
                              "date": "<Date of the article>",
                              "content": "<Detailed summary of the article in at least 200 words>"
                        }
                        // Add more articles as needed

                     ]
                  }
   """,
   # Add google_search tool to perform grounding with Google search.
   tools=[google_search]
)