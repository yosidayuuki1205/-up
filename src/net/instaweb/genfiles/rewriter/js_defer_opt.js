(function(){var d=!1,f=window,g=document;function h(a,b){return a.addEventListener=b}function i(a,b){return a.attachEvent=b}
var l="push",m="addUrl",n="querySelector",o="addEventListener",p="setAttribute",r="attachEvent",s="documentElement",t="length",u="prototype",v="call",w="getAttribute",x="querySelectorAll",y="fireEvent",z="parentNode",B="",aa="\n",ba='");',C="*",ca=":not([psa_not_processed])",da="<div>_</div>",ea='=document.getElementById("',fa="Add to queue str: ",ga="Add to queue url: ",ha="DOMContentLoaded",ia="Evaluated: ",D="Exception while evaluating.",ja="Exception while overriding document.readyState.",ka=
"Executed: ",la="Firefox",ma="Firing Event: ",na="HTMLEvents",oa="PSA ERROR: ",E="SCRIPT",pa="Unable to insert nodes, no context element found",qa="[psa_current_node]",ra="[psa_not_processed]",sa='[type="text/psajs"]',ta="application/ecmascript",ua="application/javascript",va="application/x-ecmascript",wa="application/x-javascript",xa="complete",ya="data:text/javascript,",za="div",Aa="dw: ",F="error",Ba="handle_dw: ",G="id",H="language",I="load",Ca="loaded",Da="loading",J="on",Ea="onDOMContentLoaded",
K="onafterscripts",L="onbeforescripts",M="onload",Fa="onload: ",Ga="onreadystatechange",N="orig_src",Ha="orig_type",O="psa_current_node",Ia="psa_dw_target",P="psa_not_processed",Q="psanode",Ja="readyState",Ka="readystatechange",R="script",S="src",La="text/",Ma="text/ecmascript",T="text/javascript",Na="text/javascript1.0",Oa="text/javascript1.1",Pa="text/javascript1.2",Qa="text/javascript1.3",Ra="text/javascript1.4",Sa="text/javascript1.5",Ta="text/jscript",Ua="text/livescript",U="text/psajs",Va="text/x-ecmascript",
Wa="text/x-javascript",Xa="true",V="type",Ya="var ",W;f.pagespeed=f.pagespeed||{};var X=f.pagespeed,Y=function(){this.j=[];this.g=[];this.d=this.f=0;this.i=[];this.b=B;this.k={};this.w=[ta,ua,va,wa,Ma,T,Na,Oa,Pa,Qa,Ra,Sa,Ta,Ua,Va,Wa];this.r=g.getElementById;this.m=g.getElementsByTagName;this.L=g.write;this.M=g.writeln;this.K=g.open;this.J=g.close;this.s=g[o];this.u=f[o];this.t=g[r];this.v=f[r];this.e=g.createElement;this.a=0},Z=d;W=Y[u];
W.log=function(a,b){this.g&&(this.g[l](B+a),b&&(this.g[l](b),"undefined"!=typeof console&&"undefined"!=typeof console.log&&console.log(oa+a+b.message)))};W.B=function(a,b){this.j.splice(b?b:this.j[t],0,a)};W.D=function(a){var b=this.e[v](g,R);b.text=a;b[p](V,T);a=this.q();a[z].insertBefore(b,a)};
W.N=function(){for(var a=g.getElementsByTagName(C),b=B,c=0;c<a[t];c++)if(a[c].hasAttribute(G)){var e=a[c][w](G);if(e&&-1==e.search(/[-:.]/)&&-1==e.search(/^[0-9]/))try{f[e]&&f[e].tagName&&(b+=Ya+e+ea+e+ba)}catch(k){this.log(D,k)}}b&&this.D(b)};W.H=function(a,b){var c=a[w](N)||a[w](S);if(c)if(Z){var e;e=new Image;e.src=c;e.loaded=d;var k=this;e.onerror=e.onload=function(){e.loaded=!0;e.b&&(e.b=d,k.l())};this[m](c,a,b,e)}else this[m](c,a,b);else(c=a.innerHTML||a.textContent||a.data)&&this.F(c,a,b)};
W.F=function(a,b,c){if(this.S())this[m](ya+encodeURIComponent(a),b,c);else{this.g[l](fa+a);var e=this;this.B(function(){e.o(b);e.A()[p](O,B);try{e.D(a)}catch(c){e.log(D,c)}e.log(ia+a);e.l()},c)}};Y[u].addStr=Y[u].F;
Y[u].addUrl=function(a,b,c,e){this.g[l](ga+a);var k=this;this.B(function(){if(this.fa&&e&&!e.loaded)k.f--,e.b=!0;else{k.o(b);var c=k.e[v](g,R);c[p](V,T);var q=function(){k.log(ka+a);k.l()};X.n(c,q);X.h(c,F,q);9>k.c()&&X.h(c,Ka,function(){if(c.readyState==xa||c.readyState==Ca)c.onreadystatechange=null,q()});c[p](S,a);var A=b.innerHTML||b.textContent||b.data;A&&c.appendChild(g.createTextNode(A));A=k.A();A[p](O,B);A[z].insertBefore(c,A)}},c)};Y[u].addUrl=Y[u][m];W=Y[u];
W.o=function(a){if(g[x]&&!(8>=this.c()))for(var b=g[x](ra),c=0;c<b[t];c++){var e=b.item(c);if(e==a)break;e[w](V)!=U&&e.removeAttribute(P)}};W.O=function(){for(var a=this.m[v](g,C),b=0;b<a[t];b++)a.item(b)[p](P,B)};W.A=function(){var a=null;g[n]&&(a=g[n](sa));return a};W.q=function(){var a;g[n]&&(a=g[n](qa));return a||this.m[v](g,Q)[0]};W.R=function(){var a=this.q();a.nodeName==E&&a[z].removeChild(a)};
W.p=function(){4!=this.a&&(this.o(),this.c()&&g[s].originalDoScroll&&(g[s].doScroll=g[s].originalDoScroll),Object.defineProperty&&delete g.readyState,g.getElementById=this.r,g[x]&&!(8>=this.c())&&(g.getElementsByTagName=this.m),Z&&(g.createElement=this.e),this.Q(),g.open=this.K,g.close=this.J,g.write=this.L,g.writeln=this.M,this[y](0),g.onreadystatechange&&this.exec(g.onreadystatechange,g),f.onload&&$(f,M,f.onload),this[y](1),this.a=4,this[y](3))};
W.l=function(){this.z();this.R();if(this.f<this.j[t])this.f++,this.j[this.f-1][v](f);else if(Z){this.a=3;if(0!=this.d)for(var a=this.i[t],b=0;b<a;++b)(!this.i[b][z]||this.i[b].src==B)&&this.d--;0>=this.d&&this.p()}else this.p()};W.I=function(a){for(var b=[],c=a[t],e=0;e<c;++e)b[l](a.item(e));return b};
W.U=function(){var a=g.createElement(Q);a[p](Ia,Xa);g.body.appendChild(a);this.c()&&this.N();this.O();if(Object.defineProperty)try{Object.defineProperty(g,Ja,{configurable:!0,get:function(){return Da}})}catch(b){this.log(ja,b)}this.c()&&(g[s].originalDoScroll=g[s].doScroll,g[s].doScroll=function(){throw"psa exception";});this.P();var c=this;g.writeln=function(a){c.C(a+aa)};g.write=function(a){c.C(a)};g.open=function(){};g.close=function(){};g.getElementById=function(a){c.z();return c.r[v](g,a)};g[x]&&
!(8>=c.c())&&(g.getElementsByTagName=function(a){return g[x](a+ca)});Z&&(g.createElement=function(a){var b=c.e[v](g,a);if(a.toLowerCase()==R){c.i[l](b);c.d++;a=function(){c.d--;c.d==0&&c.a==3&&c.p()};X.n(b,a);X.h(b,F,a)}return b})};W.da=function(){2<=this.a||(this[y](2),this.a=2,this.U(),this.l())};Y[u].run=Y[u].da;W=Y[u];W.X=function(a){var b=this.e[v](g,za);b.innerHTML=da+a;b.removeChild(b.firstChild);return b};W.Z=function(a){var b=a[z];b&&b.removeChild(a)};
W.W=function(a,b){for(var c=this.I(a),e=c[t],k=b[z],j=0;j<e;++j){var q=c[j];this.Z(q);k.insertBefore(q,b)}};W.Y=function(a){return a.nodeName!=E?d:a.hasAttribute(V)?(a=a[w](V),!a||-1!=this.w.indexOf(a)):a.hasAttribute(H)?(a=a[w](H),!a||-1!=this.w.indexOf(La+a.toLowerCase())):!0};W.G=function(a,b){if(a.childNodes)for(var c=this.I(a.childNodes),e=c[t],k=0;k<e;++k){var j=c[k];1==j.nodeType&&j[p](P,B);j.nodeName==E?this.Y(j)&&(b[l](j),j[p](Ha,j.type),j[p](V,U),j[p](N,j.src),j[p](S,B)):this.G(j,b)}};
W.V=function(a,b){for(var c=a[t],e=0;e<c;++e)this.H(a[e],b+e)};W.T=function(a,b,c){var a=this.X(a),e=[];this.G(a,e);c?this.W(a.childNodes,c):this.log(pa);this.V(e,b)};W.z=function(){if(this.b!=B){this.log(Ba+this.b);var a=this.b;this.b=B;var b=this.q();this.T(a,this.f,b)}};W.C=function(a){this.log(Aa+a);this.b+=a};W.$=function(a,b){this.log(Fa+b.toString());4==this.a?b[v](a):$(a,M,b)};Y[u].addOnloadListeners=Y[u].$;Y[u].ca=function(a){$(f,L,a)};Y[u].addBeforeDeferRunFunctions=Y[u].ca;
Y[u].ba=function(a){$(f,K,a)};Y[u].addAfterDeferRunFunctions=Y[u].ba;Y[u].fireEvent=function(a){this.log(ma+a);for(var a=this.k[a]||[],b=0;b<a[t];++b)this.exec(a[b]);a.length=0};Y[u].exec=function(a,b){try{a[v](b||f)}catch(c){this.log(D,c)}};Y[u].P=function(){var a=this;f[o]?(h(g,function(b,c,e){$(g,b,c,e,a.s)}),h(f,function(b,c,e){$(f,b,c,e,a.u)})):f[r]&&(i(g,function(b,c){$(g,b,c,void 0,a.t)}),i(f,function(b,c){$(f,b,c,void 0,a.v)}))};
Y[u].Q=function(){f[o]?(h(g,this.s),h(f,this.u)):f[r]&&(i(g,this.t),i(f,this.v))};var $=function(a,b,c,e,k){var j=X.deferJs;if(!(4<=j.a)){if(b==ha||b==Ka||b==Ea||b==Ga)b=0;else if(b==I||b==M)b=1;else if(b==L)b=2;else if(b==K)b=3;else{k&&k[v](a,b,c,e);return}var q;1==b&&!(8>=j.c())&&(q=g.createEvent(na),q.initEvent(I,d,d));j.k[b]||(j.k[b]=[]);j.k[b][l](function(){c[v](a,q)})}};
Y[u].ea=function(){if(!(1<=this.a)){this.a=1;for(var a=g.getElementsByTagName(R),b=a[t],c=0;c<b;++c){var e=a[c];e[w](V)==U&&this.H(e)}}};Y[u].registerScriptTags=Y[u].ea;X.n=function(a,b){X.h(a,I,b)};X.addOnload=X.n;X.h=function(a,b,c){if(a[o])a[o](b,c,d);else if(a[r])a[r](J+b,c);else{var e=a[J+b];a[J+b]=function(){c[v](this);e&&e[v](this)}}};X.addHandler=X.h;X.outerHTML=function(a){return a.outerHTML||(new XMLSerializer).serializeToString(a)};Y[u].S=function(){return-1!=navigator.userAgent.indexOf(la)};
Y[u].c=function(){var a=/(?:MSIE.(\d+\.\d+))/.exec(navigator.userAgent);return a&&a[1]?g.documentMode||parseFloat(a[1]):NaN};X.aa=function(){X.deferJs||(f.localStorage&&(Z=f.localStorage.defer_js_experimental),X.deferJs=new Y)};X.deferInit=X.aa;})();
