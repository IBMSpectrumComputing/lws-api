# ReturnMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from lsf_client.models.return_message import ReturnMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnMessage from a JSON string
return_message_instance = ReturnMessage.from_json(json)
# print the JSON string representation of the object
print(ReturnMessage.to_json())

# convert the object into a dict
return_message_dict = return_message_instance.to_dict()
# create an instance of ReturnMessage from a dict
return_message_from_dict = ReturnMessage.from_dict(return_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


