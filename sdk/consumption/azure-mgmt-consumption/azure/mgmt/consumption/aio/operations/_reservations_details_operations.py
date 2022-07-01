# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._reservations_details_operations import build_list_by_reservation_order_and_reservation_request, build_list_by_reservation_order_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ReservationsDetailsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.consumption.aio.ConsumptionManagementClient`'s
        :attr:`reservations_details` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_by_reservation_order(
        self,
        reservation_order_id: str,
        filter: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.ReservationDetailsListResult]:
        """Lists the reservations details for provided date range.

        :param reservation_order_id: Order Id of the reservation.
        :type reservation_order_id: str
        :param filter: Filter reservation details by date range. The properties/UsageDate for start
         date and end date. The filter supports 'le' and  'ge'.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ReservationDetailsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.consumption.models.ReservationDetailsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ReservationDetailsListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_reservation_order_request(
                    reservation_order_id=reservation_order_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_by_reservation_order.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_reservation_order_request(
                    reservation_order_id=reservation_order_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationDetailsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_reservation_order.metadata = {'url': "/providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails"}  # type: ignore

    @distributed_trace
    def list_by_reservation_order_and_reservation(
        self,
        reservation_order_id: str,
        reservation_id: str,
        filter: str,
        **kwargs: Any
    ) -> AsyncIterable[_models.ReservationDetailsListResult]:
        """Lists the reservations details for provided date range.

        :param reservation_order_id: Order Id of the reservation.
        :type reservation_order_id: str
        :param reservation_id: Id of the reservation.
        :type reservation_id: str
        :param filter: Filter reservation details by date range. The properties/UsageDate for start
         date and end date. The filter supports 'le' and  'ge'.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ReservationDetailsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.consumption.models.ReservationDetailsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ReservationDetailsListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_reservation_order_and_reservation_request(
                    reservation_order_id=reservation_order_id,
                    reservation_id=reservation_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_by_reservation_order_and_reservation.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_reservation_order_and_reservation_request(
                    reservation_order_id=reservation_order_id,
                    reservation_id=reservation_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationDetailsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_reservation_order_and_reservation.metadata = {'url': "/providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails"}  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_scope: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        filter: Optional[str] = None,
        reservation_id: Optional[str] = None,
        reservation_order_id: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.ReservationDetailsListResult]:
        """Lists the reservations details for the defined scope and provided date range.

        :param resource_scope: The scope associated with reservations details operations. This includes
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope
         (legacy), and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope (modern).
        :type resource_scope: str
        :param start_date: Start date. Only applicable when querying with billing profile. Default
         value is None.
        :type start_date: str
        :param end_date: End date. Only applicable when querying with billing profile. Default value is
         None.
        :type end_date: str
        :param filter: Filter reservation details by date range. The properties/UsageDate for start
         date and end date. The filter supports 'le' and  'ge'. Not applicable when querying with
         billing profile. Default value is None.
        :type filter: str
        :param reservation_id: Reservation Id GUID. Only valid if reservationOrderId is also provided.
         Filter to a specific reservation. Default value is None.
        :type reservation_id: str
        :param reservation_order_id: Reservation Order Id GUID. Required if reservationId is provided.
         Filter to a specific reservation order. Default value is None.
        :type reservation_order_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ReservationDetailsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.consumption.models.ReservationDetailsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-10-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.ReservationDetailsListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_scope=resource_scope,
                    api_version=api_version,
                    start_date=start_date,
                    end_date=end_date,
                    filter=filter,
                    reservation_id=reservation_id,
                    reservation_order_id=reservation_order_id,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    resource_scope=resource_scope,
                    api_version=api_version,
                    start_date=start_date,
                    end_date=end_date,
                    filter=filter,
                    reservation_id=reservation_id,
                    reservation_order_id=reservation_order_id,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ReservationDetailsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/{resourceScope}/providers/Microsoft.Consumption/reservationDetails"}  # type: ignore
