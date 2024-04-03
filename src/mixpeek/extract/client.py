# This file was auto-generated by Fern from our API Definition.

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
from ..types.audio_params import AudioParams
from ..types.csv_params import CsvParams
from ..types.error_response import ErrorResponse
from ..types.html_params import HtmlParams
from ..types.http_validation_error import HttpValidationError
from ..types.image_params import ImageParams
from ..types.pdf_params import PdfParams
from ..types.ppt_params import PptParams
from ..types.pptx_params import PptxParams
from ..types.txt_params import TxtParams
from ..types.video_params import VideoParams
from ..types.xlsx_params import XlsxParams

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExtractClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def text(
        self,
        *,
        file_url: typing.Optional[str] = OMIT,
        contents: typing.Optional[str] = OMIT,
        should_chunk: typing.Optional[bool] = OMIT,
        clean_text: typing.Optional[bool] = OMIT,
        max_characters_per_chunk: typing.Optional[int] = OMIT,
        extract_tags: typing.Optional[bool] = OMIT,
        summarize: typing.Optional[bool] = OMIT,
        pdf_settings: typing.Optional[PdfParams] = OMIT,
        html_settings: typing.Optional[HtmlParams] = OMIT,
        csv_settings: typing.Optional[CsvParams] = OMIT,
        ppt_settings: typing.Optional[PptParams] = OMIT,
        pptx_settings: typing.Optional[PptxParams] = OMIT,
        xlsx_settings: typing.Optional[XlsxParams] = OMIT,
        txt_settings: typing.Optional[TxtParams] = OMIT,
        audio_settings: typing.Optional[AudioParams] = OMIT,
        image_settings: typing.Optional[ImageParams] = OMIT,
        video_settings: typing.Optional[VideoParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - file_url: typing.Optional[str].

            - contents: typing.Optional[str].

            - should_chunk: typing.Optional[bool].

            - clean_text: typing.Optional[bool].

            - max_characters_per_chunk: typing.Optional[int].

            - extract_tags: typing.Optional[bool].

            - summarize: typing.Optional[bool].

            - pdf_settings: typing.Optional[PdfParams].

            - html_settings: typing.Optional[HtmlParams].

            - csv_settings: typing.Optional[CsvParams].

            - ppt_settings: typing.Optional[PptParams].

            - pptx_settings: typing.Optional[PptxParams].

            - xlsx_settings: typing.Optional[XlsxParams].

            - txt_settings: typing.Optional[TxtParams].

            - audio_settings: typing.Optional[AudioParams].

            - image_settings: typing.Optional[ImageParams].

            - video_settings: typing.Optional[VideoParams].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import Mixpeek

        client = Mixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        client.extract.text()
        """
        _request: typing.Dict[str, typing.Any] = {}
        if file_url is not OMIT:
            _request["file_url"] = file_url
        if contents is not OMIT:
            _request["contents"] = contents
        if should_chunk is not OMIT:
            _request["should_chunk"] = should_chunk
        if clean_text is not OMIT:
            _request["clean_text"] = clean_text
        if max_characters_per_chunk is not OMIT:
            _request["max_characters_per_chunk"] = max_characters_per_chunk
        if extract_tags is not OMIT:
            _request["extract_tags"] = extract_tags
        if summarize is not OMIT:
            _request["summarize"] = summarize
        if pdf_settings is not OMIT:
            _request["pdf_settings"] = pdf_settings
        if html_settings is not OMIT:
            _request["html_settings"] = html_settings
        if csv_settings is not OMIT:
            _request["csv_settings"] = csv_settings
        if ppt_settings is not OMIT:
            _request["ppt_settings"] = ppt_settings
        if pptx_settings is not OMIT:
            _request["pptx_settings"] = pptx_settings
        if xlsx_settings is not OMIT:
            _request["xlsx_settings"] = xlsx_settings
        if txt_settings is not OMIT:
            _request["txt_settings"] = txt_settings
        if audio_settings is not OMIT:
            _request["audio_settings"] = audio_settings
        if image_settings is not OMIT:
            _request["image_settings"] = image_settings
        if video_settings is not OMIT:
            _request["video_settings"] = video_settings
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "extract"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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


class AsyncExtractClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def text(
        self,
        *,
        file_url: typing.Optional[str] = OMIT,
        contents: typing.Optional[str] = OMIT,
        should_chunk: typing.Optional[bool] = OMIT,
        clean_text: typing.Optional[bool] = OMIT,
        max_characters_per_chunk: typing.Optional[int] = OMIT,
        extract_tags: typing.Optional[bool] = OMIT,
        summarize: typing.Optional[bool] = OMIT,
        pdf_settings: typing.Optional[PdfParams] = OMIT,
        html_settings: typing.Optional[HtmlParams] = OMIT,
        csv_settings: typing.Optional[CsvParams] = OMIT,
        ppt_settings: typing.Optional[PptParams] = OMIT,
        pptx_settings: typing.Optional[PptxParams] = OMIT,
        xlsx_settings: typing.Optional[XlsxParams] = OMIT,
        txt_settings: typing.Optional[TxtParams] = OMIT,
        audio_settings: typing.Optional[AudioParams] = OMIT,
        image_settings: typing.Optional[ImageParams] = OMIT,
        video_settings: typing.Optional[VideoParams] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters:
            - file_url: typing.Optional[str].

            - contents: typing.Optional[str].

            - should_chunk: typing.Optional[bool].

            - clean_text: typing.Optional[bool].

            - max_characters_per_chunk: typing.Optional[int].

            - extract_tags: typing.Optional[bool].

            - summarize: typing.Optional[bool].

            - pdf_settings: typing.Optional[PdfParams].

            - html_settings: typing.Optional[HtmlParams].

            - csv_settings: typing.Optional[CsvParams].

            - ppt_settings: typing.Optional[PptParams].

            - pptx_settings: typing.Optional[PptxParams].

            - xlsx_settings: typing.Optional[XlsxParams].

            - txt_settings: typing.Optional[TxtParams].

            - audio_settings: typing.Optional[AudioParams].

            - image_settings: typing.Optional[ImageParams].

            - video_settings: typing.Optional[VideoParams].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from mixpeek.client import AsyncMixpeek

        client = AsyncMixpeek(
            authorization="YOUR_AUTHORIZATION",
            index_id="YOUR_INDEX_ID",
            api_key="YOUR_API_KEY",
        )
        await client.extract.text()
        """
        _request: typing.Dict[str, typing.Any] = {}
        if file_url is not OMIT:
            _request["file_url"] = file_url
        if contents is not OMIT:
            _request["contents"] = contents
        if should_chunk is not OMIT:
            _request["should_chunk"] = should_chunk
        if clean_text is not OMIT:
            _request["clean_text"] = clean_text
        if max_characters_per_chunk is not OMIT:
            _request["max_characters_per_chunk"] = max_characters_per_chunk
        if extract_tags is not OMIT:
            _request["extract_tags"] = extract_tags
        if summarize is not OMIT:
            _request["summarize"] = summarize
        if pdf_settings is not OMIT:
            _request["pdf_settings"] = pdf_settings
        if html_settings is not OMIT:
            _request["html_settings"] = html_settings
        if csv_settings is not OMIT:
            _request["csv_settings"] = csv_settings
        if ppt_settings is not OMIT:
            _request["ppt_settings"] = ppt_settings
        if pptx_settings is not OMIT:
            _request["pptx_settings"] = pptx_settings
        if xlsx_settings is not OMIT:
            _request["xlsx_settings"] = xlsx_settings
        if txt_settings is not OMIT:
            _request["txt_settings"] = txt_settings
        if audio_settings is not OMIT:
            _request["audio_settings"] = audio_settings
        if image_settings is not OMIT:
            _request["image_settings"] = image_settings
        if video_settings is not OMIT:
            _request["video_settings"] = video_settings
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "extract"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
