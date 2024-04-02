# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.connection import Connection
from ..types.destination_schema import DestinationSchema
from ..types.error_response import ErrorResponse
from ..types.http_validation_error import HttpValidationError
from ..types.pipeline_response import PipelineResponse
from ..types.source_schema import SourceSchema

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def invoke(
        self,
        pipeline_id: str,
        *,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - pipeline_id: str.

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.invoke(
            pipeline_id="pipeline_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"pipelines/{jsonable_encoder(pipeline_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_pipeline_pipelines_post(
        self,
        *,
        connection_id: str,
        pipeline_id: typing.Optional[str] = OMIT,
        connection: typing.Optional[Connection] = OMIT,
        source: SourceSchema,
        destination: DestinationSchema,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        last_run: typing.Optional[dt.datetime] = OMIT,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineResponse:
        """
        Parameters:
            - connection_id: str.

            - pipeline_id: typing.Optional[str].

            - connection: typing.Optional[Connection].

            - source: SourceSchema.

            - destination: DestinationSchema.

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - enabled: typing.Optional[bool].

            - last_run: typing.Optional[dt.datetime].

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import DestinationSchema, FieldSchema, SourceSchema
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.create_pipeline_pipelines_post(
            connection_id="connection_id",
            source=SourceSchema(
                filters={},
                on_operation=["on_operation"],
                field=FieldSchema(
                    name="name",
                    type="url",
                ),
            ),
            destination=DestinationSchema(
                collection="collection",
                new_field_name="new_field_name",
                new_embeddings="new_embeddings",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"source": source, "destination": destination}
        if pipeline_id is not OMIT:
            _request["pipeline_id"] = pipeline_id
        if connection is not OMIT:
            _request["connection"] = connection
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if enabled is not OMIT:
            _request["enabled"] = enabled
        if last_run is not OMIT:
            _request["last_run"] = last_run
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "pipelines"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "connection_id": connection_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PipelineResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_status(
        self,
        task_id: str,
        *,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Query tasks status.

        Parameters:
            - task_id: str.

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.get_status(
            task_id="task_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"pipelines/status/{jsonable_encoder(task_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "pipelines"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def invoke(
        self,
        pipeline_id: str,
        *,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - pipeline_id: str.

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.pipelines.invoke(
            pipeline_id="pipeline_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"pipelines/{jsonable_encoder(pipeline_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_pipeline_pipelines_post(
        self,
        *,
        connection_id: str,
        pipeline_id: typing.Optional[str] = OMIT,
        connection: typing.Optional[Connection] = OMIT,
        source: SourceSchema,
        destination: DestinationSchema,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        last_run: typing.Optional[dt.datetime] = OMIT,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelineResponse:
        """
        Parameters:
            - connection_id: str.

            - pipeline_id: typing.Optional[str].

            - connection: typing.Optional[Connection].

            - source: SourceSchema.

            - destination: DestinationSchema.

            - metadata: typing.Optional[typing.Dict[str, typing.Any]].

            - enabled: typing.Optional[bool].

            - last_run: typing.Optional[dt.datetime].

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek import DestinationSchema, FieldSchema, SourceSchema
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.pipelines.create_pipeline_pipelines_post(
            connection_id="connection_id",
            source=SourceSchema(
                filters={},
                on_operation=["on_operation"],
                field=FieldSchema(
                    name="name",
                    type="url",
                ),
            ),
            destination=DestinationSchema(
                collection="collection",
                new_field_name="new_field_name",
                new_embeddings="new_embeddings",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"source": source, "destination": destination}
        if pipeline_id is not OMIT:
            _request["pipeline_id"] = pipeline_id
        if connection is not OMIT:
            _request["connection"] = connection
        if metadata is not OMIT:
            _request["metadata"] = metadata
        if enabled is not OMIT:
            _request["enabled"] = enabled
        if last_run is not OMIT:
            _request["last_run"] = last_run
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "pipelines"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "connection_id": connection_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PipelineResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_status(
        self,
        task_id: str,
        *,
        authorization: typing.Optional[str] = None,
        index_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Query tasks status.

        Parameters:
            - task_id: str.

            - authorization: typing.Optional[str].

            - index_id: typing.Optional[str]. filter by organization

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.pipelines.get_status(
            task_id="task_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"pipelines/status/{jsonable_encoder(task_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Authorization": str(authorization),
                        "index-id": str(index_id),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.pipelines.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "pipelines"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)