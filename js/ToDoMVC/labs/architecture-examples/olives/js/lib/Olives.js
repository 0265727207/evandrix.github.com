/*
 Olives http://flams.github.com/olives
 The MIT License (MIT)
 Copyright (c) 2012 Olivier Scherrer <pode.fr@gmail.com> - Olivier Wietrich <olivier.wietrich@gmail.com>
*/
define("Olives/DomUtils",function(){return{getNodes:function(f,g){return f instanceof HTMLElement?(f.parentNode||document.createDocumentFragment().appendChild(f),f.parentNode.querySelectorAll(g||"*")):false},getDataset:function(f){var g=0,i,k={},d,a;if(f instanceof HTMLElement)if(f.hasOwnProperty("dataset"))return f.dataset;else{for(i=f.attributes.length;g<i;g++)d=f.attributes[g].name.split("-"),d.shift()=="data"&&(k[a=d.join("-")]=f.getAttribute("data-"+a));return k}else return false}}});
define("Olives/Event-plugin",function(){return function(f){this.listen=function(g,i,k,d){g.addEventListener(i,function(a){f[k].call(f,a,g)},d=="true")}}});
define("Olives/LocalStore",["Store","Tools"],function(f,g){function i(){var f=null,d=localStorage,a=function(){d.setItem(f,this.toJSON())};this.setLocalStorage=function(c){return c&&c.setItem instanceof Function?(d=c,true):false};this.getLocalStorage=function(){return d};this.sync=function(c){return typeof c=="string"?(f=c,c=JSON.parse(d.getItem(c)),g.loop(c,function(c,a){this.has(a)||this.set(a,c)},this),a.call(this),this.watch("added",a,this),this.watch("updated",a,this),this.watch("deleted",a,
this),true):false}}return function(g){i.prototype=new f(g);return new i}});
define("Olives/Model-plugin",["Store","Observable","Tools","Olives/DomUtils"],function(f,g,i,k){return function(d,a){var c=null,e={},j={};this.observers={};this.setModel=function(l){return l instanceof f?(c=l,true):false};this.getModel=function(){return c};this.ItemRenderer=function(l,a){var b=null,e=null,d=null,j=null,g=null;this.setRenderer=function(a){b=a;return true};this.getRenderer=function(){return b};this.setRootNode=function(b){return b instanceof HTMLElement?(d=b,b=d.querySelector("*"),
this.setRenderer(b),b&&d.removeChild(b),true):false};this.getRootNode=function(){return d};this.setPlugins=function(b){e=b;return true};this.getPlugins=function(){return e};this.items=new f([]);this.setStart=function(b){return j=parseInt(b,10)};this.getStart=function(){return j};this.setNb=function(b){return g=b=="*"?b:parseInt(b,10)};this.getNb=function(){return g};this.addItem=function(b){var a;return typeof b=="number"&&!this.items.get(b)?(a=this.create(b))?((b=this.getNextItem(b))?d.insertBefore(a,
b):d.appendChild(a),true):false:false};this.getNextItem=function(b){return this.items.alter("slice",b+1).filter(function(b){if(b instanceof HTMLElement)return true})[0]};this.removeItem=function(b){var a=this.items.get(b);return a?(d.removeChild(a),this.items.set(b),true):false};this.create=function(a){if(c.has(a)){var l=b.cloneNode(true),h=k.getNodes(l);i.toArray(h).forEach(function(b){b.setAttribute("data-"+e.name+"_id",a)});this.items.set(a,l);e.apply(l);return l}};this.render=function(){var b=
g=="*"?c.getNbItems():g,a=[];if(g!==null&&j!==null){this.items.loop(function(l,h){(h<j||h>=j+b||!c.has(h))&&a.push(h)},this);a.sort(i.compareNumbers).reverse().forEach(this.removeItem,this);for(var l=j,h=b+j;l<h;l++)this.addItem(l);return true}else return false};this.setPlugins(l);this.setRootNode(a)};this.setItemRenderer=function(a,h){j[a||"default"]=h};this.getItemRenderer=function(a){return j[a]};this.foreach=function(a,h,b,d){var e=new this.ItemRenderer(this.plugins,a);e.setStart(b||0);e.setNb(d||
"*");e.render();c.watch("added",e.render,e);c.watch("deleted",function(b){e.render();this.observers[b]&&this.observers[b].forEach(function(b){c.unwatchValue(b)},this);delete this.observers[b]},this);this.setItemRenderer(h,e)};this.updateStart=function(a,h){var b=this.getItemRenderer(a);return b?(b.setStart(h),true):false};this.updateNb=function(a,h){var b=this.getItemRenderer(a);return b?(b.setNb(h),true):false};this.refresh=function(a){return(a=this.getItemRenderer(a))?(a.render(),true):false};this.bind=
function(a,h,b){var b=b||"",e=a.getAttribute("data-"+this.plugins.name+"_id"),d=b.split("."),j=e||d.shift(),f=e?b:d.join("."),e=i.getNestedProperty(c.get(j),f),g=i.toArray(arguments).slice(3);if(e||e===0||e===false)this.execBinding.apply(this,[a,h,e].concat(g))||(a[h]=e);this.hasBinding(h)||a.addEventListener("change",function(){c.has(j)&&(f?c.update(j,b,a[h]):c.set(j,a[h]))},true);this.observers[j]=this.observers[j]||[];this.observers[j].push(c.watchValue(j,function(b){this.execBinding.apply(this,
[a,h,i.getNestedProperty(b,f)].concat(g))||(a[h]=i.getNestedProperty(b,f))},this))};this.set=function(a){return a instanceof HTMLElement&&a.name?(c.set(a.name,a.value),true):false};this.form=function h(h){if(h&&h.nodeName=="FORM"){var b=this;h.addEventListener("submit",function(a){i.toArray(h.querySelectorAll("[name]")).forEach(b.set,b);a.preventDefault()},true);return true}else return false};this.addBinding=function(a,b){return a&&typeof a=="string"&&typeof b=="function"?(e[a]=b,true):false};this.execBinding=
function(a,b){return this.hasBinding(b)?(e[b].apply(a,Array.prototype.slice.call(arguments,2)),true):false};this.hasBinding=function(a){return e.hasOwnProperty(a)};this.getBinding=function(a){return e[a]};this.addBindings=function(a){return i.loop(a,function(a,e){this.addBinding(e,a)},this)};this.setModel(d);this.addBindings(a)}});
define("Olives/OObject",["StateMachine","Store","Olives/Plugins","Olives/DomUtils","Tools"],function(f,g,i,k,d){return function(a){var c=function(a){var b=j||document.createElement("div");if(a.template){typeof a.template=="string"?b.innerHTML=a.template.trim():a.template instanceof HTMLElement&&b.appendChild(a.template);if(b.childNodes.length>1)throw Error("UI.template should have only one parent node");else a.dom=b.childNodes[0];a.plugins.apply(a.dom)}else throw Error("UI.template must be set prior to render");
},e=function b(a,b,e){b&&(e?b.insertBefore(a.dom,e):b.appendChild(a.dom),j=b)},j=null,l=new f("Init",{Init:[["render",c,this,"Rendered"],["place",function(a,j){c(a);e.apply(null,d.toArray(arguments))},this,"Rendered"]],Rendered:[["place",e,this],["render",c,this]]});this.model=a instanceof g?a:new g;this.plugins=new i;this.dom=this.template=null;this.place=function(a,e){l.event("place",this,a,e)};this.render=function(){l.event("render",this)};this.setTemplateFromDom=function(a){return a instanceof
HTMLElement?(this.template=a,true):false};this.alive=function(a){return a instanceof HTMLElement?(this.setTemplateFromDom(a),this.place(a.parentNode,a.nextElementSibling),true):false}}});
define("Olives/Plugins",["Tools","Olives/DomUtils"],function(f,g){return function(){var i={},k=function(a){return a.trim()},d=function(a,c,e){c.split(";").forEach(function(c){var d=c.split(":"),c=d[0].trim(),d=d[1]?d[1].split(",").map(k):[];d.unshift(a);i[e]&&i[e][c]&&i[e][c].apply(i[e],d)})};this.add=function(a,c){var e=this;return typeof a=="string"&&typeof c=="object"&&c?(i[a]=c,c.plugins={name:a,apply:function(){return e.apply.apply(e,arguments)}},true):false};this.addAll=function(a){return f.loop(a,
function(a,e){this.add(e,a)},this)};this.get=function(a){return i[a]};this.del=function(a){return delete i[a]};this.apply=function(a){var c;return a instanceof HTMLElement?(c=g.getNodes(a),f.loop(f.toArray(c),function(a){f.loop(g.getDataset(a),function(c,f){d(a,c,f)})}),a):false}}});
define("Olives/Transport",["Observable","Tools"],function(f,g){return function(i,k){var d=null,a=null,c=new f;this.setIO=function(e){return e&&typeof e.connect=="function"?(a=e,true):false};this.getIO=function(){return a};this.connect=function(e){return typeof e=="string"?(d=a.connect(e),true):false};this.getSocket=function(){return d};this.on=function(a,c){d.on(a,c)};this.once=function(a,c){d.once(a,c)};this.emit=function(a,c,f){d.emit(a,c,f)};this.request=function(a,c,f,h){var b=Date.now()+Math.floor(Math.random()*
1E6),g=function(){f&&f.apply(h||null,arguments)};d[c.keptAlive?"on":"once"](b,g);c.__eventId__=b;d.emit(a,c);if(c.keptAlive)return function(){d.emit("disconnect-"+b);d.removeListener(b,g)}};this.listen=function(a,d,f,h){var b=a+"/"+d.path,i,k;c.hasTopic(b)||(g.mixin({method:"GET",keptAlive:true},d),k=this.request(a,d,function(a){c.notify(b,a)},this));i=c.watch(b,f,h);return function(){c.unwatch(i);c.hasTopic(b)||k()}};this.getListenObservable=function(){return c};this.setIO(i);this.connect(k)}});
define("Olives/UI-plugin",["Olives/OObject","Tools"],function(f,g){return function(i){var k={};this.place=function(d,a){if(k[a]instanceof f)k[a].place(d);else throw Error(a+" is not an OObject UI in place:"+a);};this.set=function(d,a){return typeof d=="string"&&a instanceof f?(k[d]=a,true):false};this.setAll=function(d){g.loop(d,function(a,c){this.set(c,a)},this)};this.get=function(d){return k[d]};this.setAll(i)}});
