# TreeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**directory** | **bool** |  | [optional] 
**owner** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 
**file_permission_str** | **str** |  | [optional] 
**escape_absolute_path** | **str** |  | [optional] 
**file_size** | **str** |  | [optional] 
**children** | [**List[TreeNode]**](TreeNode.md) |  | [optional] 

## Example

```python
from openapi_client.models.tree_node import TreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of TreeNode from a JSON string
tree_node_instance = TreeNode.from_json(json)
# print the JSON string representation of the object
print(TreeNode.to_json())

# convert the object into a dict
tree_node_dict = tree_node_instance.to_dict()
# create an instance of TreeNode from a dict
tree_node_from_dict = TreeNode.from_dict(tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


