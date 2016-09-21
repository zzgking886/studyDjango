/**
 * Created by zzg on 16/9/19.
 */
var CANVAS_WIDTH = 500
var CANVAS_HEIGHT = 500
var mycanvas,context;
window.onload = function ()
{
    creatCanvas();
    drawRect();
    // drawImage();
}

function creatCanvas()
{
    document.body.innerHTML = "<canvas id=\"mycanvas\" width=\""+CANVAS_WIDTH+"\" height=\""+CANVAS_HEIGHT+"\"></canvas>"
    mycanvas = document.getElementById("mycanvas");
    context = mycanvas.getContext('2d');
}

function drawRect()
{
    context.translate(200,200);
    context.fillRect(0,0,100,200);
}

function drawImage()
{
    var image = new Image();
    image.onload = function ()
    {
        context.drawImage(image,0,0);
    }
    image.src = "static/htmlImg/icon.png";
}