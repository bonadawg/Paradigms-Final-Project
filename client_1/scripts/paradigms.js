//James Bonadonna, Daily15

function Item() {
    this.addToDocument = function () { document.body.appendChild(this.myItem); },
    this.addToDiv = function () { document.getElementById('text').appendChild(this.myItem); },
    this.hide = function(){
        this.myItem.style.display = 'none'
    },
    this.reveal = function(){
        this.myItem.style.display = 'block'; 
    }
}

function Label() {
    this.createLabel = function(text, id){
        this.myItem = document.createElement("p");
        this.myItem.setAttribute("id", id);
        this.myItem.appendChild(document.createTextNode(text));
    },
    this.setText = function(text){
        this.myItem.innerHTML = text;
    },
    this.setHTML = function(text){
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

function Dropdown() {
    this.createDropdown = function(dict, id, selected){
        this.myItem = document.createElement("select");
        this.myItem.setAttribute("id", id);
        for(var key in dict){
            this.myItem.add(new Option(key));
        }
    },
    this.getSelected = function(args){
        selected = this.myItem.options[this.myItem.selectedIndex].text;
        return selected;
    }
}

function Input() {
    this.createInput = function(text, id){
        this.myItem = document.createElement("INPUT");
        this.myItem.setAttribute("id", id);
        this.myItem.value = text;
    }
    this.getValue = function(){
        return this.myItem.value;
    }
}

function Image() {
    this.createImage = function(mon, form, id, title){
        if(mon != ""){
            mon = mon.toLowerCase();
            form = form.toLowerCase();
            if(form == 'own tempo' || form == '50% forme'){
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
        }

        this.myItem = document.createElement("img");
        this.myItem.setAttribute("src", "https://img.pokemondb.net/artwork/" + mon + ".jpg");
        this.myItem.setAttribute("id", id);
        this.myItem.setAttribute("alt", title);
        this.myItem.setAttribute("width", 360);
        this.myItem.setAttribute("height", 360);
    },
    this.setImage = function(mon, form){
        mon = mon.toLowerCase();
        form = form.toLowerCase();
        
        if(form == 'own tempo' || form == '50% forme'){
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

        this.myItem.setAttribute("src", "https://img.pokemondb.net/artwork/" + mon + ".jpg");

        if(mon == 'custom' || form == 'custom'){
            this.myItem.setAttribute("src", "https://www.smashbros.com/wiiu-3ds/sp/images/character/mii_fighter/main.png");
        }
        else if(mon == 'delete'){
            this.myItem.setAttribute("src", "https://vignette.wikia.nocookie.net/joke-battles/images/d/d8/MissingNo..png/revision/latest?cb=20160129051405");
        }
    },
    this.show404 = function(){
        this.myItem.setAttribute("src", "https://veekun.com/static/local/images/404a.png");
    }
    this.show404 = function(){
        this.myItem.setAttribute("src", "https://veekun.com/static/local/images/404a.png");
    }
}
