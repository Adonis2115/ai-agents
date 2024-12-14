from pydantic_ai import Agent

agent = Agent(  
    'ollama:llama3.2',
    system_prompt='Write an engaging tweet, with little emojis and some hashtags.',
)

result = agent.run_sync('Why learn to draw ?')  
print(result.data)