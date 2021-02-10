function buildMenu(menuPlace){
	menu = Array();

	menuObject = document.getElementById(menuPlace);
	N = menuObject.childNodes.length;
	
	for(i = 0; i < N; i++){
		if(menuObject.childNodes[i].nodeType == 1 && menuObject.childNodes[i].nodeName == 'LI') menu.push = (menuObject.childNodes[i].innerHTML);
		
	}

	alert(menu)
}