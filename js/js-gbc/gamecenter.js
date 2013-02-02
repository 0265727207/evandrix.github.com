var windowingInitialized = false;
var shortcutHashes = [
	["PokemonRed", 25, "PokemonRed.gb"],
	["PokemonBlue", 26, "PokemonBlue.gb"],
	["PokemonYellow", 27, "PokemonYellow.gbc"],
	["PokemonSilver", 28, "PokemonSilver.gbc"],
	["PokemonGold", 29, "PokemonGold.gbc"],
	["PokemonCrystal", 30, "PokemonCrystal.gbc"]
]
function windowingPreInitUnsafe() {
	if (!windowingInitialized) {
		windowingInitialized = true;
		windowingInitialize();
	}
}
function windowingPreInitSafe() {
	if (typeof document.readyState == "undefined" || document.readyState == "complete") {
		windowingPreInitUnsafe();
	}
}
function windowingInitUnload() {
	removeEvent("DOMContentLoaded", document, windowingPreInitUnsafe);
	removeEvent("readystatechange", document, windowingPreInitSafe);
	removeEvent("load", document, windowingPreInitUnsafe);
}
function windowingInitialize() {
	windowingInitUnload();
	try {
		//Hook the GUI controls.
		registerGUIEvents();
		matchHashbang();
	}
	catch (error) {
		alert("Fatal initialization error: \"" + error.message + "\" file:" + error.fileName + " line: " + error.lineNumber, 2);
	}
}
function matchHashbang() {
	var length = shortcutHashes.length;
	for (var index = 0; index < length; ++index) {
		if (window.location.hash == "#" + shortcutHashes[index][0]) {
			runShortcut(shortcutHashes[index]);
			return;
		}
	}
	document.getElementById("dropdown_select").selectedIndex = 0;
}
function runShortcut(ROMDetails) {
	document.getElementById("dropdown_select").selectedIndex = ROMDetails[1];
	try {
		document.getElementById("dropdown_progress").style.display = "block";
		new Ajax({
			URL:"http://" + location.host + "/" + ROMDetails[2] + ".txt",
			Accept:"TEXT",
			Cached:true,
			Complete:function () {
				try {
					start(document.getElementById("game_canvas"), base64_decode(arguments[1]));
					initPlayer();
				}
				catch (error) {
					alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
				}
			}
		});
	}
	catch (error) {
		alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
	}
}
function registerGUIEvents() {
	document.getElementById("enable_sound").checked = settings[0];
	document.getElementById("gb_boot_rom_utilized").checked = settings[20];
	addEvent("keydown", document, function (event) {
		//Control keys / other
		GameBoyKeyDown(event);
	});
	addEvent("keyup", document, GameBoyKeyUp);
	addEvent("MozOrientation", window, GameBoyGyroSignalHandler);
	addEvent("deviceorientation", window, GameBoyGyroSignalHandler);
	var selectForm = document.getElementById("dropdown_select");
	selectForm.value = "none";
	addEvent("change", selectForm, function () {
		var valueAddr = this.value;
		if (valueAddr == "none") {
			return;
		}
		try {
			document.getElementById("dropdown_progress").style.display = "block";
			new Ajax({
				URL:"http://" + location.host + "/romStorage/" + valueAddr + ".txt",
				Accept:"TEXT",
				Cached:true,
				Complete:function () {
					try {
						start(document.getElementById("game_canvas"), base64_decode(arguments[1]));
						initPlayer();
					}
					catch (error) {
						alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
					}
				}
			});
			selectForm.blur();
		}
		catch (error) {
			alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
		}
	});
	addEvent("dragover", document.getElementById("gameboy"), stopDragPropagation);
	addEvent("drop", document.getElementById("gameboy"), function (dragEvent) {
		stopDragPropagation(dragEvent);
		if (dragEvent.dataTransfer && dragEvent.dataTransfer.files && dragEvent.dataTransfer.files.length > 0) {
			try {
				var reader = new FileReader();
				reader.readAsBinaryString(dragEvent.dataTransfer.files[0]);
				reader.onload = function (readerEvent) {
					try {
						document.getElementById("dropdown_progress").style.display = "block";
						start(document.getElementById("game_canvas"), readerEvent.target.result);
						initPlayer();
					}
					catch (error) {
						alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
					}
				}
			}
			catch (error) {
				alert(error.message + " file: " + error.fileName + " line: " + error.lineNumber);
			}
		}
	});
	addEvent("click", document.getElementById("enable_sound"), function () {
		settings[0] = document.getElementById("enable_sound").checked;
		if (GameBoyEmulatorInitialized()) {
			gameboy.initSound();
		}
	});
	addEvent("click", document.getElementById("gb_boot_rom_utilized"), function () {
		settings[20] = document.getElementById("gb_boot_rom_utilized").checked;
	});
	addEvent("unload", window, function () {
		autoSave();
	});
	addEvent("MozBeforePaint", window, MozVBlankSyncHandler);
}
function stopDragPropagation(dragEvent) {
	dragEvent.stopPropagation();
	dragEvent.preventDefault();
}
function initNewCanvasSize() {
	if (!settings[18]) {
		if (gameboy.width != 160 || gameboy.height != 144 || gameboy.canvas.width != 160 || gameboy.canvas.height != 144) {
			gameboy.canvas.width = gameboy.width = 160;
			gameboy.canvas.height = gameboy.height = 144;
		}
	}
	else {
		if (gameboy.width != gameboy.canvas.clientWidth || gameboy.height != gameboy.canvas.clientHeight || gameboy.canvas.width != gameboy.canvas.clientWidth || gameboy.canvas.height != gameboy.canvas.clientHeight) {
			gameboy.canvas.width = gameboy.width = gameboy.canvas.clientWidth;
			gameboy.canvas.height = gameboy.height = gameboy.canvas.clientHeight;
		}
		gameboy.initLCD();
	}
}
function initPlayer() {
	document.getElementById("dropdown_progress").style.display = "none";
	if (GameBoyEmulatorInitialized()) {
		initNewCanvasSize();
	}
}
//Wrapper for localStorage getItem, so that data can be retrieved in various types.
function findValue(key) {
	try {
		if (window.localStorage.getItem(key) != null) {
			return JSON.parse(window.localStorage.getItem(key));
		}
	}
	catch (error) {
		//An older Gecko 1.8.1/1.9.0 method of storage (Deprecated due to the obvious security hole):
		if (window.globalStorage[location.hostname].getItem(key) != null) {
			return JSON.parse(window.globalStorage[location.hostname].getItem(key));
		}
	}
	return null;
}
//Wrapper for localStorage setItem, so that data can be set in various types.
function setValue(key, value) {
	try {
		window.localStorage.setItem(key, JSON.stringify(value));
	}
	catch (error) {
		//An older Gecko 1.8.1/1.9.0 method of storage (Deprecated due to the obvious security hole):
		window.globalStorage[location.hostname].setItem(key, JSON.stringify(value));
	}
}
//Some wrappers and extensions for non-DOM3 browsers:
function addEvent(sEvent, oElement, fListener) {
	try {	
		oElement.addEventListener(sEvent, fListener, false);
		cout("In addEvent() : Standard addEventListener() called to add a(n) \"" + sEvent + "\" event.", -1);
	}
	catch (error) {
		oElement.attachEvent("on" + sEvent, fListener);	//Pity for IE.
		cout("In addEvent() : Nonstandard attachEvent() called to add an \"on" + sEvent + "\" event.", -1);
	}
}
function removeEvent(sEvent, oElement, fListener) {
	try {	
		oElement.removeEventListener(sEvent, fListener, false);
		cout("In removeEvent() : Standard removeEventListener() called to remove a(n) \"" + sEvent + "\" event.", -1);
	}
	catch (error) {
		oElement.detachEvent("on" + sEvent, fListener);	//Pity for IE.
		cout("In removeEvent() : Nonstandard detachEvent() called to remove an \"on" + sEvent + "\" event.", -1);
	}
}
function cout(message, colorIndex) {
	switch (colorIndex) {
		case 0:
			outputMessage("<DEBUG>: " + message, "white");
			break;
		case 1:
			outputMessage("<WARNING>: " + message, "yellow");
			break;
		case 2:
			outputMessage("<ERROR>: " + message, "red");
	}
}
function outputMessage(message, styleText) {
	var log_container = document.getElementById("debug_log");
	var new_line = document.createTextNode(message);
	var new_wrap = document.createElement("div");
	new_wrap.appendChild(new_line);
	new_wrap.style.color = styleText;
	log_container.appendChild(new_wrap);
	log_container.style.display = "block";
}