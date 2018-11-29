Label.prototype = new Item();
Button.prototype = new Item();
Image.prototype = new Item();
Input.prototype = new Item();
Dropdown.prototype = new Item();

var curr = 47
args = [1, 5]; // change this to your name //no u
var dict = {"Show all pokemon": "/pokemon/", "Show one pokemon": "/pokemon/", "Show a specific stat for a pokemon": "/pokemon/", "Show compatible pokemon to breed": "/breedable/", "Recommend a pokemon": "/recommend/", "Input a new pokemon": "/pokemon/", "Delete a created pokemon": "/pokemon/"};

l = new Label();
l.createLabel("Please choose an option:", "mLabel");
l.addToDocument();

menu = new Dropdown();
menu.createDropdown(dict, "theMenu", "Awesome!");
menu.addToDocument();

view = new Button();
view.createButton("Go!", "menuBut");
view.addClickEventHandler(processSelection, menu.getSelected(args));
view.addToDocument();

spacing = new Label(); //feel free to remove all spacings, done for my own sanity
spacing.createLabel("", "rLabel");
spacing.addToDocument();

inp = new Input();
inp.createInput("Enter a pokemon", "theInput");
inp.addToDocument();
inp.hide();

oBut = new Button();
oBut.createButton("Find!", "theButton");
oBut.addClickEventHandler(show_one, inp.getValue());
oBut.addToDocument();
oBut.hide();

bBut = new Button();
bBut.createButton("Find!", "theButton");
bBut.addClickEventHandler(breed, inp.getValue());
bBut.addToDocument();
bBut.hide();

rBut = new Button();
rBut.createButton("Find!", "theButton");
rBut.addClickEventHandler(recommend, inp.getValue());
rBut.addToDocument();
rBut.hide();

aBut = new Button();
aBut.createButton("Go!", "theButton");
aBut.addClickEventHandler(create_new, inp.getValue());
aBut.addToDocument();
aBut.hide();

dBut = new Button();
dBut.createButton("Go!", "theButton");
dBut.addClickEventHandler(delete_custom, inp.getValue());
dBut.addToDocument();
dBut.hide();

statInp = new Input();
statInp.createInput("Enter a stat", "sInput");
statInp.addToDocument();
statInp.hide();

sBut = new Button();
sBut.createButton("Find!", "theButton");
sBut.addClickEventHandler(show_stat, [inp.getValue(), statInp.getValue()]);
sBut.addToDocument();
sBut.hide();

spacing = new Label();
spacing.createLabel("", "rLabel");
spacing.addToDocument();

imag = new Image();
imag.createImage("scizor", "Normal", "theImage", "{Movie Image}");
imag.addToDocument();
imag.hide();

desc = new Label();
desc.createLabel("", "description");
desc.addToDocument();
desc.hide();

function processSelection(args){
    vote = menu.getSelected(args);
    ext = dict[vote];
    console.log(ext);

    dBut.hide();
    aBut.hide();
    rBut.hide();
    oBut.hide();
    bBut.hide();
    sBut.hide();
    inp.hide();
    statInp.hide();
    imag.hide();
    desc.hide();

    if(vote == "Show one pokemon"){
        inp.reveal();
        oBut.reveal();
    }
    else if(vote == "Show a specific stat for a pokemon"){
        inp.reveal();
        statInp.reveal();
        sBut.reveal();
    }
    else if(vote == "Show compatible pokemon to breed"){
        inp.reveal();
        bBut.reveal();
    }
    else if(vote == "Recommend a pokemon"){
        inp.reveal();
        rBut.reveal();
    }
    else if(vote == "Input a new pokemon"){
        inp.reveal();
        aBut.reveal();
    }
    else if(vote == "Delete a created pokemon"){
        inp.reveal();
        dBut.reveal();
    }
    else{
        show_all(args);
    }
}

function show_all(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/pokemon/", true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        var txt = "";
        var i;
        for(i=0; i<807; i++){
            txt += (mData.pokemon[i]['Dex #'] + ' ' + mData.pokemon[i]['Pokemon'] + '<br />');
        }
        console.log(txt);
        desc.setHTML(txt);
        desc.reveal();
        //imag.setImage(mData.pokemon['Pokemon'], mData.pokemon['Forme']);
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}

function show_one(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/pokemon/" + inp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        var txt = "";
        for(var key in mData.pokemon){
            txt += (key + ': ' + mData.pokemon[key] + '<br />');
        }
        console.log(txt);
        desc.setHTML(txt);
        desc.reveal();
        imag.setImage(mData.pokemon['Pokemon'], mData.pokemon['Forme']);
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}

function show_stat(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/pokemon/" + inp.getValue() + '/' + statInp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        var txt = mData.stat[0][1] + ' ' + statInp.getValue().charAt(0).toUpperCase() + statInp.getValue().slice(1) + ': ' + mData.stat[0][2];
        console.log(txt);
        desc.setHTML(txt);
        desc.reveal();
        imag.setImage(mData.stat[0][1], 'Normal');
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}

function breed(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/breedable/" + inp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        var i;
        var txt = inp.getValue().charAt(0).toUpperCase() + inp.getValue().slice(1) + " can breed with: <br />";
        for(i=0; i<mData.breed_list.length; i++){
            txt += (mData.breed_list[i] + '<br />');
        }
        console.log(txt);
        desc.setHTML(txt);
        desc.reveal();
        imag.setImage(inp.getValue(), "Normal");
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}

function recommend(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/recommend/" + inp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        desc.setHTML("For " + inp.getValue().charAt(0).toUpperCase() + inp.getValue().slice(1) + ", I'd recommend using " + mData.recommendation);
        desc.reveal();
        imag.setImage(mData.recommendation, "Normal");
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}

function create_new(args){
    vote = dict[menu.getSelected(args)];
    console.log(vote);
    
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("POST", "http://student04.cse.nd.edu:52047/pokemon/" + inp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    var toSend = {"pokemon": vote};

    xhrM.send(JSON.stringify(toSend));

    desc.setHTML("Success!");
    desc.reveal();
    imag.setImage("Custom", "Normal");
    imag.reveal();
}

function delete_custom(args){
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    /*xhrM.open("GET", "http://student04.cse.nd.edu:52047/pokemon/" + inp.getValue(), true) // 2 - associates request attributes with xhr
    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        imag.setImage("Delete", "Normal");
        imag.reveal();
    }*/
    xhrM.open("DELETE", "http://student04.cse.nd.edu:52047/pokemon/" + inp.getValue(), true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        desc.setHTML("Success!");
        desc.reveal();
        imag.setImage("Delete", "Normal");
        imag.reveal();
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
        desc.setHTML("Error 404: Not Found");
        desc.reveal();
        imag.show404();
        imag.reveal();
    }

    xhrM.send(null) // last step - this actually makes the request
}
