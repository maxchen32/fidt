function include(path){
    var a=document.createElement("script");
    a.type = "text/javascript";
    a.src="./js/" + path;
    var head=document.getElementsByTagName("head")[0];
    head.appendChild(a);
}

include("newWindow.js")

window.onload = function(){
    newWindow();
}