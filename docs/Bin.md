# Bin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_commercial** | **bool** | Defines whether the card is a commercial card. | [optional] 
**bin_corporate** | **bool** | Defines whether the card is a corporate business card. | [optional] 
**bin_country_issued** | **str** | The determined country where the card was issued. | [optional] 
**bin_credit** | **bool** | Defines whether the card is a credit card. | [optional] 
**bin_currency** | **str** | The default currency determined for the card. | [optional] 
**bin_debit** | **bool** | Defines whether the card is a debit card. | [optional] 
**bin_description** | **str** | A description of the bin on the card to identify what type of product the card is. | [optional] 
**bin_eu** | **bool** | Defines whether the card is regulated within the EU. | [optional] 
**scheme** | **str** | The scheme that issued the card. | [optional] 

## Example

```python
from citypay.models.bin import Bin

# TODO update the JSON string below
json = "{}"
# create an instance of Bin from a JSON string
bin_instance = Bin.from_json(json)
# print the JSON string representation of the object
print Bin.to_json()

# convert the object into a dict
bin_dict = bin_instance.to_dict()
# create an instance of Bin from a dict
bin_form_dict = bin.from_dict(bin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


