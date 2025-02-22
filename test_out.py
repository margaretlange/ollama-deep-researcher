from assistant.prompts import (
    query_writer_instructions,
    summarizer_instructions,
    reflection_instructions,
)
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import json
from assistant.state import SummaryStateInput
import pdb
from assistant.graph import graph


if __name__ == "__main__":
    # use the same topic as in the example
    # content = "How was qwen2.5 trained?"
    # state = SummaryStateInput(research_topic=content)
    #query_writer_instructions_formatted = query_writer_instructions.format(
    #    research_topic=state.research_topic
    #)
    #llm_json_mode = ChatOpenAI(model="gpt-4o", temperature=0, response_format={"type": "json_object"})
    #result = llm_json_mode.invoke(
    #    [
    #        SystemMessage(content=query_writer_instructions_formatted),
    #        HumanMessage(content="Generate a query for web search:"),
    #    ]
    #)
    # query = json.loads(result.content)
    # print(query)
    content = "How was qwen2.5 trained?"
    state = SummaryStateInput(research_topic=content)
    result = graph.invoke(state)
    print(result["running_summary"])
