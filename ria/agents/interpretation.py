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


class InterpretationModel(BaseModel):
    implications_form: str = Field(
        description=(
            "How does the metaphor shape the building's form, massing, and "
            "spatial relationships?"
        )
    )
    design_task: str = Field(
        description=(
            "Propose a design task to create an architectural concept model "
            "that evokes the metaphor."
        )
    )


class InterpretationAgent:
    def __init__(self, model_name=MODEL_NAME_DEFAULT):
        model = ChatOpenAI(model=model_name, timeout=15)
        parser = PydanticOutputParser(pydantic_object=InterpretationModel)
        system_prompt = PromptTemplate(
            template=load_prompt("interpretation", ext="md") + "\n{format_instructions}",
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

    def suggest_design_task(self, metaphor, existing_implications):
        return self.chain.invoke(
            {
                "text": (
                    "State the implications and propose a design task based on "
                    f"the metaphor {metaphor}, and following are the previous "
                    "implications and design task, try to come up with something "
                    f"different. {existing_implications}"
                )
            }
        )
