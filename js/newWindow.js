function newWindow(){
    var links = document.getElementsByTagName("a");
    for (var i=0; i<links.length; i++){
        links[i].target = "target1";
    }
}
