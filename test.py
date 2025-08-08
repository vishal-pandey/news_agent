import requests
import json
import uuid

# API endpoints
BASE_URL = "https://news-agent.codeshare.live"

def create_session(user_id=None):
    if user_id is None:
        user_id = str(uuid.uuid4())
    url = f"{BASE_URL}/apps/news_agent/users/{user_id}/sessions"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "additionalProp1": {}
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def run_conversation(session_id, user_id=None, message="Latest news on Electric Vehicles"):
    url = f"{BASE_URL}/run"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "appName": "news_agent",
        "userId": user_id if user_id else str(uuid.uuid4()),
        "sessionId": session_id,
        "newMessage": {
            "parts": [
                {
                    "text": message
                }
            ],
            "role": "user"
        },
        "streaming": False
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def extract_news_content(response):
    content = None
    try:
        # Get the first message from the response
        first_message = response[0]
        
        # Extract the content parts
        content = first_message['content']['parts'][0]['text']
        
        # Remove markdown code block syntax
        content = content.replace('```json\n', '').replace('\n```', '')
        
        # Parse the JSON string from the cleaned content
        news_data = json.loads(content)
        
        # Return the formatted JSON
        return news_data
    except (KeyError, json.JSONDecodeError, IndexError) as e:
        print(f"Error parsing response: {e}")
        if content:
            print(f"Raw content: {content}")  # For debugging
        return None

def main():
    try:
        # Generate a random user ID and create a session
        user_id = str(uuid.uuid4())
        print(f"Generated User ID: {user_id}")
        
        # Create a session first
        session_response = create_session(user_id)
        print("Session Response:", json.dumps(session_response, indent=2))
        
        # Extract session ID from response
        session_id = session_response.get('id')
        
        if session_id:
            # Run the conversation with the same user ID
            conversation_response = run_conversation(session_id, user_id)
            
            # Extract and format the news content
            # FINAL CODE HERE
            news_data = extract_news_content(conversation_response)
            
            if news_data:
                # Print the formatted JSON
                print("\nFormatted News Data:")
                print(json.dumps(news_data, indent=2))
                
                # You can also access specific parts of the data, for example:
                for i, news_item in enumerate(news_data['news'], 1):
                    print(f"\nNews Item {i}:")
                    print(f"Title: {news_item['title']}")
                    print(f"Date: {news_item['date']}")
                    print("-" * 50)
            else:
                print("Failed to parse news data from response")
        else:
            print("Failed to get session ID from response")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
