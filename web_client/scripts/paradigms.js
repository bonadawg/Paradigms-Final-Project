//James Bonadonna, Daily15

function Item() {
    this.addToDocument = function(){ document.body.appendChild(this.myItem); }
}

function Label() {
    this.createLabel = function(text, id){
        this.myItem = document.createElement("p");
        this.myItem.setAttribute("id", id);
        this.myItem.appendChild(document.createTextNode(text));
    },
    this.setText = function(text){
        this.myItem.innerHTML = text;
    }
}

function Button() {
    this.createButton = function(text, id){
        this.myItem = document.createElement("button");
        this.myItem.setAttribute("id", id);
        this.myItem.innerHTML = text;
    },
    this.addClickEventHandler = function(handler, args){
        this.myItem.onmouseup = function(){ handler(args); } // inner function
    }
}

function Image() {
    this.createImage = function(mon, form, id, title){
        mon = mon.toLowerCase();
        form = form.toLowerCase();
        if(form == 'own tempo' or form == '50% forme'){
            form = 'normal';
        }
        else if(form == 'schooling'){
            form = 'school';
        }
        else if(form == '10% forme'){
            form = '10';
        }
        else if(form == 'complete forme'){
            form = 'complete';
        }

        if(form != 'normal' && mon != 'pumpkaboo' && mon != "gourgeist"){
            form = form.replace(/\s+/g, '-').toLowerCase();
            mon = mon + '-' + form
        }

        this.myItem = document.createElement("img");
        this.myItem.setAttribute("src", "https://img.pokemondb.net/artwork/" + mon + ".jpg");
        this.myItem.setAttribute("id", id);
        this.myItem.setAttribute("alt", title);
        this.myItem.setAttribute("width", 360);
        this.myItem.setAttribute("height", 360);
    }
    this.setImage = function(src){
        this.myItem.setAttribute("src", "https://img.pokemondb.net/artwork/" + src + ".jpg");
    }
}
