# Dashboard Import Format 

29/11/2019

## Abstract

This document describes a general data structure for modelling interaction on a social platform.

## Data Structure

```javascript
Activity:
{
activity_id: string,
date: UnixTimeStamp,
subject_id: string, (Item)
subject_type: EnumItemType
activity_type: EnumActivityType,
object_id: string, (Item)
object_type: EnumItemType
}

Item:
{
item_id: string,
item_type: EnumItemType,
parent_id: string (optional),
parent_type: EnumItemType (optional),
value: string
}

EnumActivityType: ['create', 'update', 'delete', 'view', 'read']

EnumItemType: ['user', 'post', 'comment', 'directory', 'metion', 'like']
```


TODO:
mention and like are need to be in ActivityType because there are action.
I need "context" to know where the mention occur

## Details

### Activity

Activivy represent a log.

- **activity_id**: the unique id of this log (can be the log in the original dataset or a new id).
- **date**: the creation time of this log in Unix Time Stamp.
- **subject_id**: it's the id of the actor who initiate/create the log. This id is a copy of the id in the original dataset.
- **subject_type**: it's the type of the actor who initiate/create the log. The possible value are listed in EnumItemType.
- **activity_type**: it's the type of action in this log. The possible value are listed in EnumActivityType.
- **object_id**: it's the id of the object created or used with this action. This id is a copy of the id in the original dataset or a new id if it doesn't exist in the original dataset.
- **object_type**: it's the type of the object created or used with this action. The possible value are listed in EnumActivityType.

### Item
Item represent a subject or an object.

- **item_id**: the copy of the id in the original dataset.
- **item_type**: it's the type of this item. The possible value are listed in EnumActivityType.
- **parent_id**: it's the parent element of this item. For example if it's a comment the parent is the original post. (Item) (optional)
- **parent_type**: it's the type of the parent element. The possible value are listed in EnumActivityType. (optional)
- **value**: the value of this item. For example the content of a comment.