from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv(override=True)

# ollma is hostel locally
ollama_url = "http://localhost:11434/v1"

# creating a client
ollama = OpenAI(api_key="ollama", base_url=ollama_url)

# Add some test tools
tools = [{'type': "function",
          "function": {
              "name": "check_calender",
              "description": "This tool checks calender events",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "date": {"type": "string"}
                  },
                  "required": ["date"]
              }

          }
          }]

def check_calender(date):
    return "10am: Standup, 2pm: Doctors appointment"

def execute_tool(name,args):
    if name == 'check_calender':
        return check_calender(**args)
    return f"Unknown tool {name}"

messages = [{'role': 'system', 'content': 'You are a helpful assistant'},
            {'role': 'user', 'content': 'Hi there, whats on my calender ?'}
            ]

response = ollama.chat.completions.create(messages=messages, tools=tools,temperature=0, model='llama3.2:1b')

print(response.choices[0].message.content)

# basically checking what was the reason the call got finished
print(response.choices[0].finish_reason)

# Now since the llm knows about the avaibke tools, it decied to call a tool
# and finished the turn wiht the finish_reason
if response.choices[0].finish_reason == 'tool_calls':

    # All tool related information is present here
    msg = response.choices[0].message
    messages.append(msg)
    for tc in msg.tool_calls:

        result = execute_tool(tc.function.name,json.loads(tc.function.arguments))

        messages.append({'role':'tool','tool_call_id':tc.id, "content":result})

    final = ollama.chat.completions.create(model='llama3.2:1b', messages=messages)

    print(final.choices[0].message.content)