# ContactDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | The first line of the address for the card holder. | [optional] 
**address2** | **str** | The second line of the address for the card holder. | [optional] 
**address3** | **str** | The third line of the address for the card holder. | [optional] 
**area** | **str** | The area such as city, department, parish for the card holder. | [optional] 
**company** | **str** | The company name for the card holder if the contact is a corporate contact. | [optional] 
**country** | **str** | The country code in ISO 3166 format. The country value may be used for fraud analysis and for   acceptance of the transaction.  | [optional] 
**email** | **str** | An email address for the card holder which may be used for correspondence. | [optional] 
**firstname** | **str** | The first name  of the card holder. | [optional] 
**lastname** | **str** | The last name or surname of the card holder. | [optional] 
**mobile_no** | **str** | A mobile number for the card holder the mobile number is often required by delivery companies to ensure they are able to be in contact when required. | [optional] 
**postcode** | **str** | The postcode or zip code of the address which may be used for fraud analysis. | [optional] 
**telephone_no** | **str** | A telephone number for the card holder. | [optional] 
**title** | **str** | A title for the card holder such as Mr, Mrs, Ms, M. Mme. etc. | [optional] 

## Example

```python
from citypay.models.contact_details import ContactDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ContactDetails from a JSON string
contact_details_instance = ContactDetails.from_json(json)
# print the JSON string representation of the object
print(ContactDetails.to_json())

# convert the object into a dict
contact_details_dict = contact_details_instance.to_dict()
# create an instance of ContactDetails from a dict
contact_details_from_dict = ContactDetails.from_dict(contact_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


