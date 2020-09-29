# coding: utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.communication.administration.aio import PhoneNumberAdministrationClient
from azure.communication.administration import (
    PstnConfiguration,
    NumberUpdateCapabilities,
    CreateSearchOptions
)
from phone_number_helper import PhoneNumberUriReplacer
from _shared.asynctestcase  import (
    AsyncCommunicationTestCase
)
from _shared.testcase import BodyReplacerProcessor, ResponseReplacerProcessor
import os

class PhoneNumberAdministrationClientTestAsync(AsyncCommunicationTestCase):

    def setUp(self):
        super(PhoneNumberAdministrationClientTestAsync, self).setUp()
        self.recording_processors.extend([
            BodyReplacerProcessor(
                keys=["id", "token", "capabilitiesUpdateId", "phoneNumber", "phonePlanIds",
                      "phoneNumberCapabilitiesUpdates",	"releaseId",
                      "phoneNumberReleaseStatusDetails", "searchId", "phoneNumbers",
                      "entities", "phonePlanGroups", "phonePlans", "phoneNumberCapabilitiesUpdate"]
            ),
            PhoneNumberUriReplacer(),
            ResponseReplacerProcessor(keys=[self._resource_name])])
        self._phone_number_administration_client = PhoneNumberAdministrationClient.from_connection_string(
            self.connection_str)
        if self.is_live:
            self.country_code = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_COUNTRY_CODE')
            self.locale = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_LOCALE')
            self.phone_plan_group_id = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONE_PLAN_GROUP_ID')
            self.phone_plan_id = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONE_PLAN_ID')
            self.phone_plan_id_area_codes = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONE_PLAN_ID_AREA_CODES')
            self.area_code_for_search = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_AREA_CODE_FOR_SEARCH')
            self.search_id = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_SEARCH_ID')
            self.search_id_to_purchase = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_SEARCH_ID_TO_PURCHASE')
            self.search_id_to_cancel = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_SEARCH_ID_TO_CANCEL')
            self.phonenumber_to_configure = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONENUMBER_TO_CONFIGURE')
            self.phonenumber_to_get_config = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONENUMBER_TO_GET_CONFIG')
            self.phonenumber_to_unconfigure = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONENUMBER_TO_UNCONFIGURE')
            self.phonenumber_for_capabilities = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_PHONENUMBER_FOR_CAPABILITIES')
            self.capabilities_id = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_CAPABILITIES_ID')
            self.release_id = os.getenv('AZURE_COMMUNICATION_SERVICE_TNM_RELEASE_ID')
            self.scrubber.register_name_pair(
                self.phone_plan_group_id,
                "phone_plan_group_id"
            )
            self.scrubber.register_name_pair(
                self.phone_plan_id,
                "phone_plan_id"
            )
            self.scrubber.register_name_pair(
                self.phone_plan_id_area_codes,
                "phone_plan_id_area_codes"
            )
            self.scrubber.register_name_pair(
                self.area_code_for_search,
                "area_code_for_search"
            )
            self.scrubber.register_name_pair(
                self.search_id,
                "search_id"
            )
            self.scrubber.register_name_pair(
                self.search_id_to_purchase,
                "search_id_to_purchase"
            )
            self.scrubber.register_name_pair(
                self.search_id_to_cancel,
                "search_id_to_cancel"
            )
            self.scrubber.register_name_pair(
                self.phonenumber_to_configure,
                "phonenumber_to_configure"
            )
            self.scrubber.register_name_pair(
                self.phonenumber_to_get_config,
                "phonenumber_to_get_config"
            )
            self.scrubber.register_name_pair(
                self.phonenumber_to_unconfigure,
                "phonenumber_to_unconfigure"
            )
            self.scrubber.register_name_pair(
                self.phonenumber_for_capabilities,
                "phonenumber_for_capabilities"
            )
            self.scrubber.register_name_pair(
                self.capabilities_id,
                "capabilities_id"
            )
            self.scrubber.register_name_pair(
                self.release_id,
                "release_id"
            )
        else:
            self.country_code = "US"
            self.locale = "en-us"
            self.phone_plan_group_id = "phone-plan-group-id-1"
            self.phone_plan_id = "phone-plan-id-1"
            self.phone_plan_id_area_codes = "phone-plan-id-1"
            self.area_code_for_search = "777"
            self.search_id = "search-id-1"
            self.search_id_to_purchase = "search-id-1"
            self.search_id_to_cancel = "search-id-2"
            self.phonenumber_to_configure = "+17771234567"
            self.phonenumber_to_get_config = "+17771234567"
            self.phonenumber_to_unconfigure = "+17771234567"
            self.phonenumber_for_capabilities = "+17771234567"
            self.capabilities_id = "capabilities-id-1"
            self.release_id = "release_id_1"

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_list_all_phone_numbers(self):
        async with self._phone_number_administration_client:
            pages = self._phone_number_administration_client.list_all_phone_numbers()

            items = []
            async for item in pages:
                items.append(item)
        assert len(items) > 0

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_all_area_codes(self):
        async with self._phone_number_administration_client:
            area_codes = await self._phone_number_administration_client.get_all_area_codes(
                location_type="NotRequired",
                country_code=self.country_code,
                phone_plan_id=self.phone_plan_id_area_codes
            )
        assert area_codes.primary_area_codes

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_capabilities_update(self):
        async with self._phone_number_administration_client:
            capability_response = await self._phone_number_administration_client.get_capabilities_update(
                capabilities_update_id=self.capabilities_id
            )
        assert capability_response.capabilities_update_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_update_capabilities(self):
        update = NumberUpdateCapabilities(add=iter(["InboundCalling"]))

        phone_number_capabilities_update = {
            self.phonenumber_for_capabilities: update
        }

        async with self._phone_number_administration_client:
            capability_response = await self._phone_number_administration_client.update_capabilities(
                phone_number_capabilities_update=phone_number_capabilities_update
            )
        assert capability_response.capabilities_update_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_list_all_supported_countries(self):
        async with self._phone_number_administration_client:
            countries = self._phone_number_administration_client.list_all_supported_countries()
            items = []
            async for item in countries:
                items.append(item)
        self.assertGreater(len(items), 0)
        assert items[0].localized_name

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_number_configuration(self):
        async with self._phone_number_administration_client:
            phone_number_response = await self._phone_number_administration_client.get_number_configuration(
                phone_number=self.phonenumber_to_get_config
            )
        assert phone_number_response.pstn_configuration

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_configure_number(self):
        pstnConfig = PstnConfiguration(
            callback_url="https://callbackurl",
            application_id="ApplicationId",
            azure_pstn_target_id="AzurePstnTargetId"
        )
        async with self._phone_number_administration_client:
            await self._phone_number_administration_client.configure_number(
                pstn_configuration=pstnConfig,
                phone_number=self.phonenumber_to_configure
            )

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_list_phone_plan_groups(self):
        async with self._phone_number_administration_client:
            phone_plan_group_response = self._phone_number_administration_client.list_phone_plan_groups(
                country_code=self.country_code
            )

            items = []
            async for item in phone_plan_group_response:
                items.append(item)
        assert len(items) > 0
        assert items[0].phone_plan_group_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_list_phone_plans(self):
        async with self._phone_number_administration_client:
            phone_plan_response = self._phone_number_administration_client.list_phone_plans(
                country_code=self.country_code,
                phone_plan_group_id=self.phone_plan_group_id
            )

            items = []
            async for item in phone_plan_response:
                items.append(item)
        assert len(items) > 0
        assert items[0].phone_plan_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_phone_plan_location_options(self):
        async with self._phone_number_administration_client:
            location_options_response = await self._phone_number_administration_client.get_phone_plan_location_options(
                country_code=self.country_code,
                phone_plan_group_id=self.phone_plan_group_id,
                phone_plan_id=self.phone_plan_id
            )
        assert location_options_response.location_options.label_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_release_by_id(self):
        async with self._phone_number_administration_client:
            phone_number_release_response = await self._phone_number_administration_client.get_release_by_id(
                release_id=self.release_id
            )
        assert phone_number_release_response.release_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_list_all_releases(self):
        async with self._phone_number_administration_client:
            releases_response = self._phone_number_administration_client.list_all_releases()

            items = []
            async for item in releases_response:
                items.append(item)
        self.assertGreater(len(items), 0)
        assert items[0].id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_get_search_by_id(self):
        async with self._phone_number_administration_client:
            phone_number_search_response = await self._phone_number_administration_client.get_search_by_id(
                search_id=self.search_id
            )
        assert phone_number_search_response.search_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_create_search(self):
        searchOptions = CreateSearchOptions(
            area_code=self.area_code_for_search,
            description="testsearch20200014",
            display_name="testsearch20200014",
            phone_plan_ids=[self.phone_plan_id],
            quantity=1
        )
        async with self._phone_number_administration_client:
            search_response = await self._phone_number_administration_client.create_search(
                body=searchOptions
            )
        assert search_response.search_id

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_cancel_search(self):
        async with self._phone_number_administration_client:
            await self._phone_number_administration_client.cancel_search(
                search_id=self.search_id_to_cancel
            )

    @AsyncCommunicationTestCase.await_prepared_test
    @pytest.mark.live_test_only
    async def test_purchase_search(self):
        async with self._phone_number_administration_client:
            await self._phone_number_administration_client.purchase_search(
                search_id=self.search_id_to_purchase
            )
