# BinLookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **int** | A bin value to use for lookup. | 

## Example

```python
from citypay.models.bin_lookup import BinLookup

# TODO update the JSON string below
json = "{}"
# create an instance of BinLookup from a JSON string
bin_lookup_instance = BinLookup.from_json(json)
# print the JSON string representation of the object
print(BinLookup.to_json())

# convert the object into a dict
bin_lookup_dict = bin_lookup_instance.to_dict()
# create an instance of BinLookup from a dict
bin_lookup_from_dict = BinLookup.from_dict(bin_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


