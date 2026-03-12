from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

from ria.prompts import load_prompt

load_dotenv()

MODEL_NAME_DEFAULT = "gpt-4o"


class MetaphorModel(BaseModel):
    metaphor: str = Field(description="The metaphor.")
    key_traits: str = Field(
        description=(
            "A brief text description of the key traits that the metaphor aims "
            "to transfer to the building's design."
        )
    )


class MetaphorAgent:
    def __init__(self, model_name=MODEL_NAME_DEFAULT):
        model = ChatOpenAI(model=model_name)
        parser = PydanticOutputParser(pydantic_object=MetaphorModel)
        system_prompt = PromptTemplate(
            template=load_prompt("metaphor", ext="md")
            + "return JSON as follows:\n{format_instructions}",
            input_variables=[],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(prompt=system_prompt),
                ("user", "{text}"),
            ]
        )
        self.chain = prompt_template | model | parser

    def propose_new_metaphor(self, previously_generated_metaphors=""):
        return self.chain.invoke(
            {
                "previously_generated_metaphors": previously_generated_metaphors,
                "text": "Propose a new metaphor for a building.",
            }
        )

    def expand_given_metaphor(self, metaphor_str):
        return self.chain.invoke(
            {
                "previously_generated_metaphors": "",
                "text": (
                    "State the key traits for the metaphor and return both "
                    f"metaphor and key traits in the specified format: {metaphor_str}"
                ),
            }
        )
