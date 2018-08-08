/**
 * Created by zzg on 16/9/27.
 */
var canvas;
var stage;
var txt;
var count = 0;
window.onload = function ()
{
    canvas = document.getElementById("canvas");
    stage = new createjs.Stage(canvas);
    txt = new createjs.Text("number->", "20px Arial", "#ff7700");
    stage.addChild(txt);

    createjs.Ticker.setFPS(40);
    createjs.Ticker.addEventListener("tick", tick);
}

function tick(exception)
{
    count++;
    txt.text = "number->"+count+"!";
    // stage.update();
}

function cboxGetUserStatus(userid,verifycode)
{
    var thisUserId = userid;
    var thisVerifycode = verifycode;

    //Make something to login verify.
}