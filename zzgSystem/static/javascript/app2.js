/**
 * Created by zzg on 16/9/27.
 */
var canvas;
var stage;
// var img = new Image();
var sprite;
window.onload = function ()
{
    canvas = document.getElementById("canvas");
    stage = new createjs.Stage(canvas);

    stage.addEventListener("stagemousedown",clickCanvas);
    stage.addEventListener("stagemousemove",movemouse);

    var data = {
        images:["/static/htmlImg/icon.png"],
        frames:{width:85,height:85,regX:10,regY:10}
    }
    sprite = new createjs.Sprite(new createjs.SpriteSheet(data));
    createjs.Ticker.setFPS(20);
    createjs.Ticker.addEventListener("tick", tick);
}

function tick(exception)
{
    var t = stage.getNumChildren();
    for (var i = t -1; i >= 0; i--)
    {
        var s = stage.getChildAt(i);
        s.vY += 2;
        s.vX += 1;
        s.x += s.vX;
        s.y += s.vY;

        s.scaleX = s.scaleY = s.vS;
        s.alpha += s.vA;

        if (s.alpha <= 0 || s.y >= canvas.height)
        {
            stage.removeChildAt(i);
        }
    }
    stage.update(exception);
}

function clickCanvas(exception)
{
    adds(200,stage.mouseX,stage.mouseY,2);
}

function movemouse(exception)
{
    adds(50,stage.mouseX,stage.mouseY,1);
}

function adds(count,x,y,speed)
{
    for (var i = 0; i < count; i++)
    {
        var s = sprite.clone();
        s.x = x;
        s.y = y;
        s.alpha = Math.random() * 0.5 + 0.5;
        s.scaleX = s.scaleY = Math.random() * 0.3;

        var a = Math.PI * 2 + Math.random();
        var v = (Math.random() - 0.5) * 30 * speed;
        s.vX = Math.cos(a) * v;
        s.vY = Math.sin(a) * v;
        s.vS = (Math.random() - 0.5) * 0.2;
        s.vA = -Math.random() * 0.05 - 0.01;
        stage.addChild(s);
    }
}