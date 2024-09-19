# AirlineSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival_location_code** | **str** | A standard airline routing code (airport code or location identifier) applicable to the arrival portion of this segment.  | 
**carrier_code** | **str** | This field contains the two character airline designator code (air carrier code or airline code) that corresponds to the airline carrier applicable for up to four flight segments of this trip itinerary.  | 
**class_service_code** | **str** | This field contains a code that corresponds to the fare class (A, B, C, D, Premium, Discounted, etc.) within the overall class of service (e.g., First Class, Business, Economy) applicable to this travel segment, as specified in the IATA Standard Code allocation table.  | 
**departure_date** | **date** | The Departure Date for the travel segment in ISO Date Format (yyyy-MM-dd). | 
**departure_location_code** | **str** | A standard airline routing code (airport code or location identifier) applicable to the departure portion of this segment.  | [optional] 
**flight_number** | **str** | This field contains the carrier-assigned Flight Number for this travel segment. | 
**segment_fare** | **int** | This field contains the total Fare for this travel segment. | [optional] 
**stop_over_indicator** | **str** | O &#x3D; Stopover allowed, X &#x3D; Stopover not allowed. | [optional] 

## Example

```python
from citypay.models.airline_segment import AirlineSegment

# TODO update the JSON string below
json = "{}"
# create an instance of AirlineSegment from a JSON string
airline_segment_instance = AirlineSegment.from_json(json)
# print the JSON string representation of the object
print(AirlineSegment.to_json())

# convert the object into a dict
airline_segment_dict = airline_segment_instance.to_dict()
# create an instance of AirlineSegment from a dict
airline_segment_from_dict = AirlineSegment.from_dict(airline_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


