import base64

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


class EvaluationModel(BaseModel):
    metaphor_alignment_score: int | None = Field(
        default=None,
        description=(
            "How well does the represented architectural concept model embody "
            "the intended metaphor throughout its form? Ranging from 1 to 5. "
            "Low score=1: No alignment with the metaphor; the model fails to "
            "represent the key traits of the metaphor. High score=5: Fully "
            "aligned with the intended concept; the model strongly and clearly "
            "embodies the metaphor's key traits."
        ),
    )
    conceptual_strength_score: int | None = Field(
        default=None,
        description=(
            "To what extent does the represented geometric object convey an "
            "architecturally relevant coherent idea? Ranging from 1 to 5. Low "
            "score=1: Poor suitability as a concept model; the model does not "
            "trigger imagination or hold a coherent architectural idea. High "
            "score=5: Excellent concept model; it effectively sparks imagination "
            "while conveying a clear and engaging architectural idea."
        ),
    )
    geometric_complexity_score: int | None = Field(
        default=None,
        description=(
            "Geometric complexity of the represented geometric object. Ranging "
            "from 1 to 5. Low score=1: Very low complexity; composed of only "
            "2-3 simple primitives or shapes. High score=5: Very high complexity; "
            "a geometrically intricate model with rich, detailed forms that "
            "contribute to the overall concept."
        ),
    )
    design_task_adherence_score: int | None = Field(
        default=None,
        description=(
            "If a design task is provided, how well does the represented "
            "geometry adhere to the provided design task? Ranging from 1 to 5. "
            "Low score=1: No adherence to the design task; the model does not "
            "reflect the proposed task. High score=5: Full adherence to the "
            "design task; the model effectively reflects the proposed task."
        ),
    )


class EvaluationAgent:
    def __init__(self, model_name=MODEL_NAME_DEFAULT):
        model = ChatOpenAI(model=model_name)
        parser = PydanticOutputParser(pydantic_object=EvaluationModel)
        system_prompt = PromptTemplate(
            template=load_prompt("evaluation", ext="md") + "\n{format_instructions}",
            input_variables=[],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(prompt=system_prompt),
                ("user", "{text}"),
                (
                    "user",
                    [
                        {
                            "type": "image_url",
                            "image_url": {"url": "data:image/png;base64,{image_data}"},
                            "detail": "low",
                        }
                    ],
                ),
            ]
        )
        self.chain = prompt_template | model | parser

    def evaluate_architectural_model(self, filename, metaphor_data):
        with open(filename, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")

        try:
            return self.chain.invoke(
                {
                    "text": (
                        "Please evaluate the architectural concept model shown "
                        "in the image. The metaphor data is below:\n\n"
                        f"{metaphor_data}"
                    ),
                    "image_data": image_data,
                }
            )
        except Exception as exc:
            print(f"Error: {exc}")
            return EvaluationModel(
                metaphor_alignment_score=None,
                conceptual_strength_score=None,
                geometric_complexity_score=None,
                design_task_adherence_score=None,
            )
