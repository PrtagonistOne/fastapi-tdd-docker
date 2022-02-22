from pydantic import BaseModel, AnyUrl


class SummaryPayloadSchema(BaseModel):
    url: AnyUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
