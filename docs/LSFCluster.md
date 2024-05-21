# LSFCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobid_range** | **str** |  | [optional] 
**cluster_index** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from lsf_client.models.lsf_cluster import LSFCluster

# TODO update the JSON string below
json = "{}"
# create an instance of LSFCluster from a JSON string
lsf_cluster_instance = LSFCluster.from_json(json)
# print the JSON string representation of the object
print(LSFCluster.to_json())

# convert the object into a dict
lsf_cluster_dict = lsf_cluster_instance.to_dict()
# create an instance of LSFCluster from a dict
lsf_cluster_from_dict = LSFCluster.from_dict(lsf_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


