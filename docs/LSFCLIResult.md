# LSFCLIResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | [optional] 
**exitcode** | **int** |  | [optional] 
**job_dir** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from lsf_client.models.lsfcli_result import LSFCLIResult

# TODO update the JSON string below
json = "{}"
# create an instance of LSFCLIResult from a JSON string
lsfcli_result_instance = LSFCLIResult.from_json(json)
# print the JSON string representation of the object
print(LSFCLIResult.to_json())

# convert the object into a dict
lsfcli_result_dict = lsfcli_result_instance.to_dict()
# create an instance of LSFCLIResult from a dict
lsfcli_result_from_dict = LSFCLIResult.from_dict(lsfcli_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


