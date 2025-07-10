# PaylinkCustomParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_meta_data** | **bool** | Determines if the custom parameter is stored as meta data against an authorisation allowing for that authorisation to be searched and queried by the result of this value. Defaults to false. | [optional] 
**entry_mode** | **str** | The type of entry mode. A value of &#x60;pre&#x60; will pre-render the custom parameter before the payment screen. Any other value will result in the custom parameter being displayed on the payment screen. | [optional] 
**field_type** | **str** | The type of html field, defaulting to &#x60;text&#x60;. Options are:   - &#x60;dob&#x60;      A date of birth field as a series of select list entries  - &#x60;text&#x60;     Allows the user to enter any text.  - &#x60;password&#x60; A field where the characters are masked to protect the input, typically used for passwords.  - &#x60;email&#x60;    Used for input fields that should contain an email address.  - &#x60;number&#x60;   For numeric input, can include controls for incrementing or decrementing the number.  - &#x60;tel&#x60;      For telephone numbers.  - &#x60;url&#x60;      A text field for entering a URL.  - &#x60;hidden&#x60;   Not visible to the user, but its value is sent when the form is submitted.  - &#x60;checkbox&#x60; A check box allowing single values to be selected/deselected.  - &#x60;radio&#x60;    Allows the user to select one of a limited number of choices.  - &#x60;select&#x60;   Renders as select items  Select Options:  Select options are constructed by providing a list of values in the value custom parameter field. Each value is delimited by a pipe character &#x60;|&#x60;. Value items can also be delimited with &#x60;:&#x60; as a value label pair.  For instance, a sports club requires identifying it&#39;s age group for membership entry:  &lt;CodeGroup title&#x3D;\&quot;Select Examples\&quot; label&#x3D;\&quot;ProcessBatchRequest\&quot;&gt;    &#x60;&#x60;&#x60;json {{ title: &#39;Basic Values&#39; }}      { \&quot;label\&quot; : \&quot;Age Group\&quot;,        \&quot;fieldType\&quot;: \&quot;select\&quot;,        \&quot;value\&quot; : \&quot;Under 18|18-30|30-50|50+\&quot; }...       &lt;select&gt;          &lt;option value&#x3D;\&quot;Under 18\&quot;&gt;Under 18&lt;/option&gt;          &lt;option value&#x3D;\&quot;18-30\&quot;&gt;18-30&lt;/option&gt;          &lt;option value&#x3D;\&quot;30-50\&quot;&gt;30-50&lt;/option&gt;          &lt;option value&#x3D;\&quot;50+\&quot;&gt;50+&lt;/option&gt;      &lt;/select&gt;    &#x60;&#x60;&#x60;    &#x60;&#x60;&#x60;json {{ title: &#39;Label and Values&#39; }}      { \&quot;label\&quot; : \&quot;Age Group\&quot;,        \&quot;fieldType\&quot;: \&quot;select\&quot;,        \&quot;value\&quot; : \&quot;0:Under 18|1:18-30|2:30-50|3:50+\&quot; }...       &lt;select&gt;          &lt;option value&#x3D;\&quot;0\&quot;&gt;Under 18&lt;/option&gt;          &lt;option value&#x3D;\&quot;1\&quot;&gt;18-30&lt;/option&gt;          &lt;option value&#x3D;\&quot;2\&quot;&gt;30-50&lt;/option&gt;          &lt;option value&#x3D;\&quot;3\&quot;&gt;50+&lt;/option&gt;      &lt;/select&gt;    &#x60;&#x60;&#x60; &lt;/CodeGroup&gt;  Fields may be requested as optional. If a select is required to be optional, provide a value such as &#x60;:Select an Option|options...&#x60; at the front of the list.  | [optional] 
**group** | **str** | A value which groups items for layout. The value should be a string title for rendering such as \&quot;Your Account Info\&quot;. If no value is provided, the parameter is added to a default parameter group. Group names are ordered alphabetically when rendered. | [optional] 
**label** | **str** | A label to show alongside the input. If this value is not supplied, the name value will be used. | [optional] 
**locked** | **bool** | States whether the field is locked, preventing entry or amendment by the person completing the form. | [optional] 
**name** | **str** | Refers to the rendered HTML form element name. The value of this field is used in the postback and redirect dataset. | 
**order** | **int** | A value which allows you to order the position of elements in a grouping. Values will order in ascending order. Negative values are possible. | [optional] 
**pattern** | **str** | A string value which specifies the validation logic of the form element, for example a value of QA[0-9]{3,4} will require a value such as QA221 or QA4433. | [optional] 
**placeholder** | **str** | A value to set as the placeholder attribute which will render in the browser. | [optional] 
**required** | **bool** | A boolean value that states whether the field is required or optional. When an element is required, validation will be performed on the end user&#39;s input form. | [optional] 
**value** | **str** | An initial value for the parameter as it appears on the Form. If your parameter is hidden, the value will be required. | [optional] 

## Example

```python
from citypay.models.paylink_custom_param import PaylinkCustomParam

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkCustomParam from a JSON string
paylink_custom_param_instance = PaylinkCustomParam.from_json(json)
# print the JSON string representation of the object
print(PaylinkCustomParam.to_json())

# convert the object into a dict
paylink_custom_param_dict = paylink_custom_param_instance.to_dict()
# create an instance of PaylinkCustomParam from a dict
paylink_custom_param_from_dict = PaylinkCustomParam.from_dict(paylink_custom_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


