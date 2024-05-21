# RepositoryBean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from lsf_client.models.repository_bean import RepositoryBean

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryBean from a JSON string
repository_bean_instance = RepositoryBean.from_json(json)
# print the JSON string representation of the object
print(RepositoryBean.to_json())

# convert the object into a dict
repository_bean_dict = repository_bean_instance.to_dict()
# create an instance of RepositoryBean from a dict
repository_bean_from_dict = RepositoryBean.from_dict(repository_bean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


