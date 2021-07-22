function viewLink(){
	var sd = document.getElementsByClassName("uri");
	for (var i = 0; i < sd.length; i++) {
		sd[i].target = "view_frame";
	}
}