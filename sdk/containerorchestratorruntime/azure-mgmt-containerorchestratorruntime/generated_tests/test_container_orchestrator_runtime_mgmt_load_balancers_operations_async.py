# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerorchestratorruntime.aio import ContainerOrchestratorRuntimeMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerOrchestratorRuntimeMgmtLoadBalancersOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerOrchestratorRuntimeMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_load_balancers_get(self, resource_group):
        response = await self.client.load_balancers.get(
            resource_uri="str",
            load_balancer_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_load_balancers_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.load_balancers.begin_create_or_update(
                resource_uri="str",
                load_balancer_name="str",
                resource={
                    "id": "str",
                    "name": "str",
                    "properties": {
                        "addresses": ["str"],
                        "advertiseMode": "str",
                        "bgpPeers": ["str"],
                        "provisioningState": "str",
                        "serviceSelector": {"str": "str"},
                    },
                    "systemData": {
                        "createdAt": "2020-02-20 00:00:00",
                        "createdBy": "str",
                        "createdByType": "str",
                        "lastModifiedAt": "2020-02-20 00:00:00",
                        "lastModifiedBy": "str",
                        "lastModifiedByType": "str",
                    },
                    "type": "str",
                },
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_load_balancers_delete(self, resource_group):
        response = await self.client.load_balancers.delete(
            resource_uri="str",
            load_balancer_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_load_balancers_list(self, resource_group):
        response = self.client.load_balancers.list(
            resource_uri="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
