# HttpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_timeout** | **int** | The connection timeout in milliseconds. | [optional] 
**content_type** | **str** | The content type of the http call. Defaults to &#x60;application/json&#x60;. | [optional] 
**headers** | **object** | Http headers to add to the configuration. | [optional] 
**method** | **str** | The HTTP method to use. Defaults to &#x60;POST&#x60;. | [optional] 
**read_timeout** | **int** | The read timeout in milliseconds when waiting for a reply. | [optional] 
**url** | **str** | The url of the endpoint to contact. The value should be https. | 

## Example

```python
from citypay.models.http_config import HttpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConfig from a JSON string
http_config_instance = HttpConfig.from_json(json)
# print the JSON string representation of the object
print(HttpConfig.to_json())

# convert the object into a dict
http_config_dict = http_config_instance.to_dict()
# create an instance of HttpConfig from a dict
http_config_from_dict = HttpConfig.from_dict(http_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


