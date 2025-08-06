import requests
import json
import uuid

# API endpoints
BASE_URL = "http://127.0.0.1:8000"

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

def run_conversation(session_id, user_id=None, message="Hello"):
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

def main():
    try:
        # Generate a random user ID and create a session
        user_id = str(uuid.uuid4())
        print(f"Generated User ID: {user_id}")
        
        # Create a session first
        session_response = create_session(user_id)
        print("Session Response:", json.dumps(session_response, indent=2))
        
        # Extract session ID from response (adjust this based on actual response structure)
        session_id = session_response.get('id')  # Adjust this key based on actual response
        
        if session_id:
            # Run the conversation with the same user ID
            conversation_response = run_conversation(session_id, user_id)
            print("\nConversation Response:", json.dumps(conversation_response, indent=2))
        else:
            print("Failed to get session ID from response")
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
