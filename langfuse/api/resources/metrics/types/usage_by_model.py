# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class UsageByModel(pydantic_v1.BaseModel):
    """
    Daily usage of a given model. Usage corresponds to the unit set for the specific model (e.g. tokens).
    """

    model: typing.Optional[str] = None
    input_usage: int = pydantic_v1.Field(alias="inputUsage")
    """
    Total number of generation input units (e.g. tokens)
    """

    output_usage: int = pydantic_v1.Field(alias="outputUsage")
    """
    Total number of generation output units (e.g. tokens)
    """

    total_usage: int = pydantic_v1.Field(alias="totalUsage")
    """
    Total number of generation total units (e.g. tokens)
    """

    count_traces: int = pydantic_v1.Field(alias="countTraces")
    count_observations: int = pydantic_v1.Field(alias="countObservations")
    total_cost: float = pydantic_v1.Field(alias="totalCost")
    """
    Total model cost in USD
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        kwargs_with_defaults_exclude_none: typing.Any = {
            "by_alias": True,
            "exclude_none": True,
            **kwargs,
        }

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset),
            super().dict(**kwargs_with_defaults_exclude_none),
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
