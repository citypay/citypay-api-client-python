# ExternalMPI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authen_result** | **str** | The authentication result available from the MPI. | [optional] 
**cavv** | **str** | A value determining the cardholder verification value supplied by the card scheme. | [optional] 
**eci** | **int** | The obtained e-commerce indicator from the MPI. | [optional] 
**enrolled** | **str** | A value determining whether the card holder was enrolled. | [optional] 
**xid** | **str** | The XID used for processing with the MPI. | [optional] 

## Example

```python
from citypay.models.external_mpi import ExternalMPI

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMPI from a JSON string
external_mpi_instance = ExternalMPI.from_json(json)
# print the JSON string representation of the object
print(ExternalMPI.to_json())

# convert the object into a dict
external_mpi_dict = external_mpi_instance.to_dict()
# create an instance of ExternalMPI from a dict
external_mpi_from_dict = ExternalMPI.from_dict(external_mpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


