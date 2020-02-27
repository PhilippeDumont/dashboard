/*
* Project represents a project

* id : auto_increment id to define a project
    ** id create itself at the row creation (auto_increment)
* name : name given to a project

* creation_date : date of creation of the project

*last_opening_date : the last date when the user has opened the project

* nb_activities : the number of activities that contains the project

*nb_items : the number of items that contains the project
*/


export class Project {


    //Constructor with only not null emlements
    //id is creating itself at the row creation
    constructor(id, name, creation_date, last_opening_date, nb_activities, nb_items) {
        this.id = id;
        this.name = name;
        this.creation_date = creation_date;
        this.last_opening_date = last_opening_date;
        this.nb_activities = nb_activities;
        this.nb_items = nb_items;
    }

    //GETTERS AND SETTERS

    getId() {
        return this.id;
    }

    setId(new_id) {
        this.id = new_id;
    }

    getName() {
        return this.name;
    }

    setName(new_name) {
        this.name = new_name;
    }

    getCreationDate() {
        return this.creation_date;
    }

    setCreationdate(new_creation_date) {
        this.creation_date = new_creation_date;
    }

    getLastOpeningdate() {
        return this.last_opening_date;
    }

    setLastopeningDate(new_last_opening_date) {
        this.last_opening_date = new_last_opening_date;
    }

    getNbActivities() {
        return this.nb_activities;
    }

    setNbActivities(new_nb_activities) {
        this.nb_activities = new_nb_activities;
    }

    getNbItems() {
        return this.nb_items;
    }

    setNbItems(new_nb_items) {
        this.nb_items = new_nb_items;
    }
}