/********************************************************************************************************************************
* Item represent a subject or an object.

* item_id: the copy of the id in the original dataset.
    ** item_id create itself at the row creation (auto_increment)

* item_type: it's the type of this item. The possible value are listed in EnumActivityType.

* parent_id: it's the parent element of this item. For example if it's a comment the parent is the original post. (Item) (optional)
    **parent_id is an element that can be null => not in constructor

* parent_type: it's the type of the parent element. The possible value are listed in EnumActivityType. (optional)
    **parent_type is an element that can be null => not in constructor

* value: the value of this item. For example the content of a comment.
    **value is an element that can be null => not in constructor
********************************************************************************************************************************/

export class Item {


    //Constructor with only not null emlements
    //id is creating itself at the row creation
    constructor(item_type) {
        this.item_type = item_type;
    }

    //GETTERS AND SETTERS

    getItemType() {
        return this.item_type;
    }

    setItemType(new_item_type) {
        this.item_type = new_item_type;
    }
}