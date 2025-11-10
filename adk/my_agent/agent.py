from google.adk.agents import Agent, SequentialAgent

# Subagent 1: Math & Logic Expert
math_agent = Agent(
    name="MathExpert",
    model="gemini-2.5-flash",
    description=("""You solve math, logic, and coding problems step-by-step."""), 
    instruction=("""Always show your work. Use LaTeX for equations. Be precise."""), 
    output_key="math_response"
)

# Subagent 2: Creative Writer
writer_agent = Agent(
    model="gemini-2.5-flash",
    name="CreativeWriter",
    description=("""You craft stories, poems, emails, or social media posts."""), 
    instruction=("""Be engaging, vivid, and match the requested tone."""), 
    output_key="writing_response"
)

# Subagent 3: Local Guide (Poland Edition)
local_guide = Agent(
    model="gemini-2.5-flash",
    name="PolandGuide",
    description=("""You give insider tips about Poland: food, travel, culture, events."""),
    instruction=("""Use Polish phrases when relevant. Be warm and practical."""),
    output_key="local_guide_response"
)

# Root Agent: The Smart Dispatcher
root_agent = Agent(
    model="gemini-2.5-flash",
    name="RootAgent",
    description=("""A helpful assistant that routes questions to the right expert."""),
    instruction=("""
    Analyze the user's request. Choose ONE subagent to anser it based on the topic, and user request.:
    - MathExpert → math, puzzles, code, calculations
    - CreativeWriter → stories, writing, emails, poetry
    - PolandGuide → anything about Poland, travel, culture, food

    Forward the query exactly. Do not answer yourself.
    If user do not specify a topic, sugest topic based on their query or show options.
    After the expert replies, say: 'Routed to: {agent name}' at the end.
    """),
    sub_agents=[math_agent, writer_agent, local_guide]
)