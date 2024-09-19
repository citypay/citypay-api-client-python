# PaylinkAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The first line of the address. | [optional] 
**address2** | **str** | The second line of the address. | [optional] 
**address3** | **str** | The third line of the address. | [optional] 
**area** | **str** | The area such as city, department, town or parish. | [optional] 
**country** | **str** | The country code in ISO 3166 format. The country code should be an ISO-3166 2 or 3 digit country code. | [optional] 
**label** | **str** | A label for the address such as Head Office, Home Address. | [optional] 
**postcode** | **str** | The postcode or zip code of the address. | [optional] 

## Example

```python
from citypay.models.paylink_address import PaylinkAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkAddress from a JSON string
paylink_address_instance = PaylinkAddress.from_json(json)
# print the JSON string representation of the object
print(PaylinkAddress.to_json())

# convert the object into a dict
paylink_address_dict = paylink_address_instance.to_dict()
# create an instance of PaylinkAddress from a dict
paylink_address_from_dict = PaylinkAddress.from_dict(paylink_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


