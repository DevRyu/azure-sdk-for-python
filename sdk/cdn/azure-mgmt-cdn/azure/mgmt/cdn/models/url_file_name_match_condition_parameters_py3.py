# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UrlFileNameMatchConditionParameters(Model):
    """Defines the parameters for UrlFilename match conditions.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar odatatype: Required.  Default value:
     "#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlFilenameConditionParameters" .
    :vartype odatatype: str
    :param operator: Required. Describes operator to be matched. Possible
     values include: 'Any', 'Equal', 'Contains', 'BeginsWith', 'EndsWith',
     'LessThan', 'LessThanOrEqual', 'GreaterThan', 'GreaterThanOrEqual'
    :type operator: str or ~azure.mgmt.cdn.models.UrlFileNameOperator
    :param negate_condition: Describes if this is negate condition or not
    :type negate_condition: bool
    :param match_values: Required. The match value for the condition of the
     delivery rule
    :type match_values: list[str]
    :param transforms: List of transforms
    :type transforms: list[str or ~azure.mgmt.cdn.models.Transform]
    """

    _validation = {
        'odatatype': {'required': True, 'constant': True},
        'operator': {'required': True},
        'match_values': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'negate_condition': {'key': 'negateCondition', 'type': 'bool'},
        'match_values': {'key': 'matchValues', 'type': '[str]'},
        'transforms': {'key': 'transforms', 'type': '[str]'},
    }

    odatatype = "#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlFilenameConditionParameters"

    def __init__(self, *, operator, match_values, negate_condition: bool=None, transforms=None, **kwargs) -> None:
        super(UrlFileNameMatchConditionParameters, self).__init__(**kwargs)
        self.operator = operator
        self.negate_condition = negate_condition
        self.match_values = match_values
        self.transforms = transforms
