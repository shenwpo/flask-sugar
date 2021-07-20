from typing import Any, Dict, Optional

from typing_extensions import Literal
from pydantic.fields import FieldInfo, Undefined


class Param(FieldInfo):
    in_: Literal["query", "header", "path", "cookie"]

    def __init__(
            self,
            default: Any,
            *,
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            deprecated: Optional[bool] = None,
            **extra: Any,
    ):
        self.deprecated = deprecated
        self.example = example
        self.examples = examples
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            **extra,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.default})"


class Path(Param):
    in_ = "path"

    def __init__(
            self,
            default: Any,
            *,
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            deprecated: Optional[bool] = None,
            **extra: Any,
    ):
        self.in_ = self.in_
        super().__init__(
            ...,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


class Query(Param):
    in_ = "query"

    def __init__(
            self,
            default: Any,
            *,
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            deprecated: Optional[bool] = None,
            **extra: Any,
    ):
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


class Header(Param):
    in_ = "header"

    def __init__(
            self,
            default: Any,
            *,
            alias: Optional[str] = None,
            convert_underscores: bool = True,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            deprecated: Optional[bool] = None,
            **extra: Any,
    ):
        self.convert_underscores = convert_underscores
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


class Cookie(Param):
    in_ = "cookie"

    def __init__(
            self,
            default: Any,
            *,
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            deprecated: Optional[bool] = None,
            **extra: Any,
    ):
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            deprecated=deprecated,
            example=example,
            examples=examples,
            **extra,
        )


class Body(FieldInfo):
    def __init__(
            self,
            default: Any,
            *,
            embed: bool = False,
            media_type: str = "application/json",
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            **extra: Any,
    ):
        self.embed = embed
        self.media_type = media_type
        self.example = example
        self.examples = examples
        super().__init__(
            default,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            **extra,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.default})"


class Form(Body):
    def __init__(
            self,
            default: Any,
            *,
            media_type: str = "application/x-www-form-urlencoded",
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            **extra: Any,
    ):
        super().__init__(
            default,
            embed=True,
            media_type=media_type,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            **extra,
        )


class File(Form):
    def __init__(
            self,
            default: Any,
            *,
            media_type: str = "multipart/form-data",
            alias: Optional[str] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            gt: Optional[float] = None,
            ge: Optional[float] = None,
            lt: Optional[float] = None,
            le: Optional[float] = None,
            min_length: Optional[int] = None,
            max_length: Optional[int] = None,
            regex: Optional[str] = None,
            example: Any = Undefined,
            examples: Optional[Dict[str, Any]] = None,
            **extra: Any,
    ):
        super().__init__(
            default,
            media_type=media_type,
            alias=alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            example=example,
            examples=examples,
            **extra,
        )