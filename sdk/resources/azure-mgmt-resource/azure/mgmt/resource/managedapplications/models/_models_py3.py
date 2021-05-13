# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._application_client_enums import *


class Resource(msrest.serialization.Model):
    """Resource information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class GenericResource(Resource):
    """Resource information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        managed_by: Optional[str] = None,
        sku: Optional["Sku"] = None,
        identity: Optional["Identity"] = None,
        **kwargs
    ):
        super(GenericResource, self).__init__(location=location, tags=tags, **kwargs)
        self.managed_by = managed_by
        self.sku = sku
        self.identity = identity


class Application(GenericResource):
    """Information about managed application.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param plan: The plan information.
    :type plan: ~azure.mgmt.resource.managedapplications.models.Plan
    :param kind: Required. The kind of the managed application. Allowed values are MarketPlace and
     ServiceCatalog.
    :type kind: str
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param application_definition_id: The fully qualified path of managed application definition
     Id.
    :type application_definition_id: str
    :param parameters: Name and value pairs that define the managed application parameters. It can
     be a JObject or a well formed JSON string.
    :type parameters: str
    :ivar outputs: Name and value pairs that define the managed application outputs.
    :vartype outputs: str
    :ivar provisioning_state: The managed application provisioning state. Possible values include:
     "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled",
     "Failed", "Succeeded", "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.managedapplications.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True, 'pattern': r'^[-\w\._,\(\)]+$'},
        'managed_resource_group_id': {'required': True},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'kind': {'key': 'kind', 'type': 'str'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'application_definition_id': {'key': 'properties.applicationDefinitionId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'str'},
        'outputs': {'key': 'properties.outputs', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        kind: str,
        managed_resource_group_id: str,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        managed_by: Optional[str] = None,
        sku: Optional["Sku"] = None,
        identity: Optional["Identity"] = None,
        plan: Optional["Plan"] = None,
        application_definition_id: Optional[str] = None,
        parameters: Optional[str] = None,
        **kwargs
    ):
        super(Application, self).__init__(location=location, tags=tags, managed_by=managed_by, sku=sku, identity=identity, **kwargs)
        self.plan = plan
        self.kind = kind
        self.managed_resource_group_id = managed_resource_group_id
        self.application_definition_id = application_definition_id
        self.parameters = parameters
        self.outputs = None
        self.provisioning_state = None


class ApplicationArtifact(msrest.serialization.Model):
    """Managed application artifact.

    :param name: The managed application artifact name.
    :type name: str
    :param uri: The managed application artifact blob uri.
    :type uri: str
    :param type: The managed application artifact type. Possible values include: "Template",
     "Custom".
    :type type: str or ~azure.mgmt.resource.managedapplications.models.ApplicationArtifactType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        uri: Optional[str] = None,
        type: Optional[Union[str, "ApplicationArtifactType"]] = None,
        **kwargs
    ):
        super(ApplicationArtifact, self).__init__(**kwargs)
        self.name = name
        self.uri = uri
        self.type = type


class ApplicationDefinition(GenericResource):
    """Information about managed application definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param lock_level: Required. The managed application lock level. Possible values include:
     "CanNotDelete", "ReadOnly", "None".
    :type lock_level: str or ~azure.mgmt.resource.managedapplications.models.ApplicationLockLevel
    :param display_name: The managed application definition display name.
    :type display_name: str
    :param is_enabled: A value indicating whether the package is enabled or not.
    :type is_enabled: str
    :param authorizations: Required. The managed application provider authorizations.
    :type authorizations:
     list[~azure.mgmt.resource.managedapplications.models.ApplicationProviderAuthorization]
    :param artifacts: The collection of managed application artifacts. The portal will use the
     files specified as artifacts to construct the user experience of creating a managed application
     from a managed application definition.
    :type artifacts: list[~azure.mgmt.resource.managedapplications.models.ApplicationArtifact]
    :param description: The managed application definition description.
    :type description: str
    :param package_file_uri: The managed application definition package file Uri. Use this element.
    :type package_file_uri: str
    :param main_template: The inline main template json which has resources to be provisioned. It
     can be a JObject or well-formed JSON string.
    :type main_template: str
    :param create_ui_definition: The createUiDefinition json for the backing template with
     Microsoft.Solutions/applications resource. It can be a JObject or well-formed JSON string.
    :type create_ui_definition: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'lock_level': {'required': True},
        'authorizations': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'lock_level': {'key': 'properties.lockLevel', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[ApplicationProviderAuthorization]'},
        'artifacts': {'key': 'properties.artifacts', 'type': '[ApplicationArtifact]'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'package_file_uri': {'key': 'properties.packageFileUri', 'type': 'str'},
        'main_template': {'key': 'properties.mainTemplate', 'type': 'str'},
        'create_ui_definition': {'key': 'properties.createUiDefinition', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        lock_level: Union[str, "ApplicationLockLevel"],
        authorizations: List["ApplicationProviderAuthorization"],
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        managed_by: Optional[str] = None,
        sku: Optional["Sku"] = None,
        identity: Optional["Identity"] = None,
        display_name: Optional[str] = None,
        is_enabled: Optional[str] = None,
        artifacts: Optional[List["ApplicationArtifact"]] = None,
        description: Optional[str] = None,
        package_file_uri: Optional[str] = None,
        main_template: Optional[str] = None,
        create_ui_definition: Optional[str] = None,
        **kwargs
    ):
        super(ApplicationDefinition, self).__init__(location=location, tags=tags, managed_by=managed_by, sku=sku, identity=identity, **kwargs)
        self.lock_level = lock_level
        self.display_name = display_name
        self.is_enabled = is_enabled
        self.authorizations = authorizations
        self.artifacts = artifacts
        self.description = description
        self.package_file_uri = package_file_uri
        self.main_template = main_template
        self.create_ui_definition = create_ui_definition


class ApplicationDefinitionListResult(msrest.serialization.Model):
    """List of managed application definitions.

    :param value: The array of managed application definitions.
    :type value: list[~azure.mgmt.resource.managedapplications.models.ApplicationDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ApplicationDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ApplicationDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ApplicationDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ApplicationListResult(msrest.serialization.Model):
    """List of managed applications.

    :param value: The array of managed applications.
    :type value: list[~azure.mgmt.resource.managedapplications.models.Application]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Application]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Application"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ApplicationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ApplicationPatchable(GenericResource):
    """Information about managed application.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param plan: The plan information.
    :type plan: ~azure.mgmt.resource.managedapplications.models.PlanPatchable
    :param kind: The kind of the managed application. Allowed values are MarketPlace and
     ServiceCatalog.
    :type kind: str
    :param managed_resource_group_id: The managed resource group Id.
    :type managed_resource_group_id: str
    :param application_definition_id: The fully qualified path of managed application definition
     Id.
    :type application_definition_id: str
    :param parameters: Name and value pairs that define the managed application parameters. It can
     be a JObject or a well formed JSON string.
    :type parameters: str
    :ivar outputs: Name and value pairs that define the managed application outputs.
    :vartype outputs: str
    :ivar provisioning_state: The managed application provisioning state. Possible values include:
     "Accepted", "Running", "Ready", "Creating", "Created", "Deleting", "Deleted", "Canceled",
     "Failed", "Succeeded", "Updating".
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.managedapplications.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'pattern': r'^[-\w\._,\(\)]+$'},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'plan': {'key': 'plan', 'type': 'PlanPatchable'},
        'kind': {'key': 'kind', 'type': 'str'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'application_definition_id': {'key': 'properties.applicationDefinitionId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'str'},
        'outputs': {'key': 'properties.outputs', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        managed_by: Optional[str] = None,
        sku: Optional["Sku"] = None,
        identity: Optional["Identity"] = None,
        plan: Optional["PlanPatchable"] = None,
        kind: Optional[str] = None,
        managed_resource_group_id: Optional[str] = None,
        application_definition_id: Optional[str] = None,
        parameters: Optional[str] = None,
        **kwargs
    ):
        super(ApplicationPatchable, self).__init__(location=location, tags=tags, managed_by=managed_by, sku=sku, identity=identity, **kwargs)
        self.plan = plan
        self.kind = kind
        self.managed_resource_group_id = managed_resource_group_id
        self.application_definition_id = application_definition_id
        self.parameters = parameters
        self.outputs = None
        self.provisioning_state = None


class ApplicationProviderAuthorization(msrest.serialization.Model):
    """The managed application provider authorization.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. The provider's principal identifier. This is the identity that
     the provider will use to call ARM to manage the managed application resources.
    :type principal_id: str
    :param role_definition_id: Required. The provider's role definition identifier. This role will
     define all the permissions that the provider must have on the managed application's container
     resource group. This role definition cannot have permission to delete the resource group.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        principal_id: str,
        role_definition_id: str,
        **kwargs
    ):
        super(ApplicationProviderAuthorization, self).__init__(**kwargs)
        self.principal_id = principal_id
        self.role_definition_id = role_definition_id


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates managed application is not able to process the incoming request. The reason is provided in the error message.

    :param http_status: Http status code.
    :type http_status: str
    :param error_code: Error code.
    :type error_code: str
    :param error_message: Error message indicating why the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        http_status: Optional[str] = None,
        error_code: Optional[str] = None,
        error_message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.http_status = http_status
        self.error_code = error_code
        self.error_message = error_message


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :ivar type: The identity type. Default value: "SystemAssigned".
    :vartype type: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'constant': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "SystemAssigned"

    def __init__(
        self,
        **kwargs
    ):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None


class Operation(msrest.serialization.Model):
    """Microsoft.Solutions operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.resource.managedapplications.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Solutions.
    :type provider: str
    :param resource: Resource on which the operation is performed: Application, JitRequest, etc.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Microsoft.Solutions operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Microsoft.Solutions operations.
    :type value: list[~azure.mgmt.resource.managedapplications.models.Operation]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Plan(msrest.serialization.Model):
    """Plan for the managed application.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The plan name.
    :type name: str
    :param publisher: Required. The publisher ID.
    :type publisher: str
    :param product: Required. The product code.
    :type product: str
    :param promotion_code: The promotion code.
    :type promotion_code: str
    :param version: Required. The plan's version.
    :type version: str
    """

    _validation = {
        'name': {'required': True},
        'publisher': {'required': True},
        'product': {'required': True},
        'version': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        publisher: str,
        product: str,
        version: str,
        promotion_code: Optional[str] = None,
        **kwargs
    ):
        super(Plan, self).__init__(**kwargs)
        self.name = name
        self.publisher = publisher
        self.product = product
        self.promotion_code = promotion_code
        self.version = version


class PlanPatchable(msrest.serialization.Model):
    """Plan for the managed application.

    :param name: The plan name.
    :type name: str
    :param publisher: The publisher ID.
    :type publisher: str
    :param product: The product code.
    :type product: str
    :param promotion_code: The promotion code.
    :type promotion_code: str
    :param version: The plan's version.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        publisher: Optional[str] = None,
        product: Optional[str] = None,
        promotion_code: Optional[str] = None,
        version: Optional[str] = None,
        **kwargs
    ):
        super(PlanPatchable, self).__init__(**kwargs)
        self.name = name
        self.publisher = publisher
        self.product = product
        self.promotion_code = promotion_code
        self.version = version


class Sku(msrest.serialization.Model):
    """SKU for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name.
    :type name: str
    :param tier: The SKU tier.
    :type tier: str
    :param size: The SKU size.
    :type size: str
    :param family: The SKU family.
    :type family: str
    :param model: The SKU model.
    :type model: str
    :param capacity: The SKU capacity.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        name: str,
        tier: Optional[str] = None,
        size: Optional[str] = None,
        family: Optional[str] = None,
        model: Optional[str] = None,
        capacity: Optional[int] = None,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
        self.size = size
        self.family = family
        self.model = model
        self.capacity = capacity
