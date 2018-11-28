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
view.addClickEventHandler(putVote, menu.getSelected(args));
view.addToDocument();

rating = new Label();
rating.createLabel("Loading...", "rLabel");
rating.addToDocument();

/*but = new Button();
but.createButton("UP", "theButton");
but.addClickEventHandler(putVote, args[1]);
but.addToDocument();*/

imag = new Image();
imag.createImage("", "", "theImage", "{Movie Image}");
imag.addToDocument();

inp = new Input();
inp.createInput("Enter a Pokemon", "theInput");
inp.addToDocument();

load_movie();

imag.show404();

function load_movie(){
    console.log(inp.getValue());
    imag.setImage("scizor", "Normal");
    var xhrM = new XMLHttpRequest() // 1 - creating request object

    xhrM.open("GET", "http://student04.cse.nd.edu:52047/pokemon/" + 'scizor', true) // 2 - associates request attributes with xhr

    xhrM.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrM.responseText);
        mData = JSON.parse(xhrM.responseText);
        myImg = mData.img;
        imag.setImage("scizor", "Normal");
    }

    xhrM.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrM.statusText);
    }

    xhrM.send(null) // last step - this actually makes the request

    var xhrR = new XMLHttpRequest() // 1 - creating request object

    xhrR.open("GET", "http://student04.cse.nd.edu:51047/ratings/" + curr.toString(), true) // 2 - associates request attributes with xhr

    xhrR.onload = function(e) { // triggered when response is received
        // must be written before send
        console.log(xhrR.responseText);
        rData = JSON.parse(xhrR.responseText);
        console.log(rData)
        rating.setText("scizor");
    }

    xhrR.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhrR.statusText);
    }

    xhrR.send(null) // last step - this actually makes the request
}


function putVote(args){
    vote = dict[menu.getSelected(args)];
    console.log(vote);
    
    var xhrV = new XMLHttpRequest() // 1 - creating request object

    xhrV.open("POST", "http://student04.cse.nd.edu:52047" + vote + inp.getValue(), true) // 2 - associates request attributes with xhr

    var toSend = {"pokemon": vote};

    xhrV.send(JSON.stringify(toSend));
    load_movie();
}
