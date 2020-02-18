/************************************************************************************************************************************************************************************
* Activivy represent a log.

* activity_id: the unique id of this log (can be the log in the original dataset or a new id).
    ** activity_id create itself at the row creation (auto_increment)

* date: the creation time of this log in Unix Time Stamp.

* subject_id: it's the id of the actor who initiate/create the log. This id is a copy of the id in the original dataset.
    **subject_id is an element that can be null => not in constructor

* subject_type: it's the type of the actor who initiate/create the log. The possible value are listed in EnumItemType.
    **subject_type is an element that can be null => not in constructor

* activity_type: it's the type of action in this log. The possible value are listed in EnumActivityType.

* object_id: it's the id of the object created or used with this action. This id is a copy of the id in the original dataset or a new id if it doesn't exist in the original dataset.
    **object_id is an element that can be null => not in constructor

* object_type: it's the type of the object created or used with this action. The possible value are listed in EnumActivityType.
    **object_type is an element that can be null => not in constructor
************************************************************************************************************************************************************************************/

export class Activity {


    //Constructor with only not null emlements
    //id is creating itself at the row creation
    constructor(activity_type, date) {
        this.activity_type = activity_type;
        this.date = date;
    }

    //GETTERS AND SETTERS

    getActivityType() {
        return this.activity_type;
    }

    setActivityType(new_activity_type) {
        this.activity_type = new_activity_type;
    }

    getDate() {
        return this.date;
    }

    setDate(new_date) {
        this.date = new_date;
    }

}