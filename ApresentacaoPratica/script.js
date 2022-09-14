var c = document.getElementById("myCanvas");
var cnv = c.getContext("2d");

var moveXLeft = 0;
var moveXRight = 0;
var moveYUp = 0;
var moveYDown = 0;

var x = 100;
var y = 100;
var raio = 100;

var xStatic = 400;
var yStatic = 400;
var raioStatic = 100;

var velocidade = 2;

window.addEventListener('keydown', function(event){
    if (event.defaultPrevented) {
        return; // Do nothing if event already handled
    }
    if(event.code ==  "KeyW") {
        moveYUp = -velocidade;
    }
    if(event.code == "KeyS") {
        moveYDown = velocidade;
    }
    if(event.code == "KeyD") {
        moveXRight = velocidade;
    }
    if(event.code ==  "KeyA") {
        moveXLeft = -velocidade;
    }
})

window.addEventListener('keyup', function(event){
    switch(event.code) {
        case "KeyW":
            moveYUp = 0;
        break;
        case "KeyS":
            moveYDown = 0;
        break;
        case "KeyD":
            moveXRight = 0;
        break;
        case "KeyA":
            moveXLeft = 0;
        break;
    }
})

function render() {
    var color = "";

    var distancia = Math.sqrt(Math.pow(x-xStatic,2) + Math.pow(y-yStatic,2))

    if(distancia <= raio+raioStatic) color = "red";
    else color = "blue";

    cnv.clearRect(0,0,c.width,c.height);

    cnv.beginPath();
    cnv.arc(xStatic,yStatic,raioStatic,0,2*Math.PI);
    cnv.stroke();
    cnv.fillStyle = color;
    cnv.fill();
    cnv.beginPath();
    cnv.arc(x,y,raio,0,2*Math.PI);
    cnv.fillStyle = color;
    cnv.fill();
    cnv.stroke();
}

function loop() {
    requestAnimationFrame(loop);
    render();
    if(x <= c.width - raio - velocidade) x += moveXRight;
    if(x >= raio + velocidade) x += moveXLeft;
    if(y >= raio + velocidade) y += moveYUp;
    if(y <= c.height - raio - velocidade)y += moveYDown
}

loop();
