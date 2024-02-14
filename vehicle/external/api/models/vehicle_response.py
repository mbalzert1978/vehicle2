import json
import typing

import pydantic


class VehicleResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)
    id: str
    name: str
    year_of_manufacture: int
    body: typing.Annotated[
        str, pydantic.PlainSerializer(lambda x: json.loads(x), return_type=dict)
    ]
    ready_to_drive: bool
