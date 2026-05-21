{8:}{21:}xchr[32]:=' ';xchr[33]:='!';xchr[34]:='"';xchr[35]:='#';
xchr[36]:='$';xchr[37]:='%';xchr[38]:='&';xchr[39]:='''';xchr[40]:='(';
xchr[41]:=')';xchr[42]:='*';xchr[43]:='+';xchr[44]:=',';xchr[45]:='-';
xchr[46]:='.';xchr[47]:='/';xchr[48]:='0';xchr[49]:='1';xchr[50]:='2';
xchr[51]:='3';xchr[52]:='4';xchr[53]:='5';xchr[54]:='6';xchr[55]:='7';
xchr[56]:='8';xchr[57]:='9';xchr[58]:=':';xchr[59]:=';';xchr[60]:='<';
xchr[61]:='=';xchr[62]:='>';xchr[63]:='?';xchr[64]:='@';xchr[65]:='A';
xchr[66]:='B';xchr[67]:='C';xchr[68]:='D';xchr[69]:='E';xchr[70]:='F';
xchr[71]:='G';xchr[72]:='H';xchr[73]:='I';xchr[74]:='J';xchr[75]:='K';
xchr[76]:='L';xchr[77]:='M';xchr[78]:='N';xchr[79]:='O';xchr[80]:='P';
xchr[81]:='Q';xchr[82]:='R';xchr[83]:='S';xchr[84]:='T';xchr[85]:='U';
xchr[86]:='V';xchr[87]:='W';xchr[88]:='X';xchr[89]:='Y';xchr[90]:='Z';
xchr[91]:='[';xchr[92]:='\';xchr[93]:=']';xchr[94]:='^';xchr[95]:='_';
xchr[96]:='`';xchr[97]:='a';xchr[98]:='b';xchr[99]:='c';xchr[100]:='d';
xchr[101]:='e';xchr[102]:='f';xchr[103]:='g';xchr[104]:='h';
xchr[105]:='i';xchr[106]:='j';xchr[107]:='k';xchr[108]:='l';
xchr[109]:='m';xchr[110]:='n';xchr[111]:='o';xchr[112]:='p';
xchr[113]:='q';xchr[114]:='r';xchr[115]:='s';xchr[116]:='t';
xchr[117]:='u';xchr[118]:='v';xchr[119]:='w';xchr[120]:='x';
xchr[121]:='y';xchr[122]:='z';xchr[123]:='{';xchr[124]:='|';
xchr[125]:='}';xchr[126]:='~';
{:21}{23:}for i:=0 to 31 do xchr[i]:=chr(i);
for i:=127 to 255 do xchr[i]:=chr(i);
{:23}{24:}for i:=0 to 255 do xord[chr(i)]:=127;
for i:=128 to 255 do xord[xchr[i]]:=i;
for i:=0 to 126 do xord[xchr[i]]:=i;{:24}{74:}interaction:=3;
{:74}{77:}deletionsallowed:=true;setboxallowed:=true;errorcount:=0;
{:77}{80:}helpptr:=0;useerrhelp:=false;{:80}{97:}interrupt:=0;
OKtointerrupt:=true;{:97}{166:}{wasmemend:=memmin;waslomax:=memmin;
washimin:=memmax;panicking:=false;}{:166}{215:}nestptr:=0;
maxneststack:=0;curlist.modefield:=1;curlist.headfield:=29999;
curlist.tailfield:=29999;curlist.auxfield.int:=-65536000;
curlist.mlfield:=0;curlist.pgfield:=0;shownmode:=0;
{991:}pagecontents:=0;pagetail:=29998;mem[29998].hh.rh:=-32768;
lastglue:=32767;lastpenalty:=0;lastkern:=0;pagesofar[7]:=0;
pagemaxdepth:=0{:991};
{:215}{254:}for k:=7163 to 8006 do xeqlevel[k]:=-127;
{:254}{257:}nonewcontrolsequence:=true;hash[514].lh:=0;hash[514].rh:=0;
for k:=515 to 4780 do hash[k]:=hash[514];{:257}{272:}saveptr:=0;
curlevel:=-127;curgroup:=0;curboundary:=0;maxsavestack:=0;
{:272}{287:}magset:=0;{:287}{383:}curmark[0]:=-32768;curmark[1]:=-32768;
curmark[2]:=-32768;curmark[3]:=-32768;curmark[4]:=-32768;
{:383}{439:}curval:=0;curvallevel:=0;radix:=0;curorder:=0;
{:439}{481:}for k:=0 to 16 do readopen[k]:=2;
{:481}{490:}condptr:=-32768;iflimit:=0;curif:=0;ifline:=0;
{:490}{521:}TEXformatdefault:='plain.fmt';
{:521}{551:}for k:=0 to fontmax do fontused[k]:=false;
{:551}{556:}nullcharacter.b0:=-128;nullcharacter.b1:=-128;
nullcharacter.b2:=-128;nullcharacter.b3:=-128;{:556}{593:}totalpages:=0;
maxv:=0;maxh:=0;maxpush:=0;lastbop:=-1;doingleaders:=false;
deadcycles:=0;curs:=-1;{:593}{596:}halfbuf:=dvibufsize div 2;
dvilimit:=dvibufsize;dviptr:=0;dvioffset:=0;dvigone:=0;
{:596}{606:}downptr:=-32768;rightptr:=-32768;
{:606}{648:}adjusttail:=-32768;lastbadness:=0;
{:648}{662:}packbeginline:=0;{:662}{685:}emptyfield.rh:=0;
emptyfield.lh:=-32768;nulldelimiter.b0:=0;nulldelimiter.b1:=-128;
nulldelimiter.b2:=0;nulldelimiter.b3:=-128;{:685}{771:}alignptr:=-32768;
curalign:=-32768;curspan:=-32768;curloop:=-32768;curhead:=-32768;
curtail:=-32768;{:771}{928:}for z:=0 to 307 do begin hyphword[z]:=0;
hyphlist[z]:=-32768;end;hyphcount:=0;{:928}{990:}outputactive:=false;
insertpenalties:=0;{:990}{1033:}ligaturepresent:=false;
cancelboundary:=false;lfthit:=false;rthit:=false;insdisc:=false;
{:1033}{1267:}aftertoken:=0;{:1267}{1282:}longhelpseen:=false;
{:1282}{1300:}formatident:=0;
{:1300}{1343:}for k:=0 to 17 do writeopen[k]:=false;
{:1343}{164:}for k:=-32766 to-32748 do mem[k].int:=0;k:=-32767;
while k<=-32748 do begin mem[k].hh.rh:=-32767;mem[k].hh.b0:=0;
mem[k].hh.b1:=0;k:=k+4;end;mem[-32761].int:=65536;mem[-32763].hh.b0:=1;
mem[-32757].int:=65536;mem[-32759].hh.b0:=2;mem[-32753].int:=65536;
mem[-32755].hh.b0:=1;mem[-32752].int:=65536;mem[-32755].hh.b1:=1;
mem[-32749].int:=-65536;mem[-32751].hh.b0:=1;rover:=-32747;
mem[rover].hh.rh:=32767;mem[rover].hh.lh:=1000;
mem[rover+1].hh.lh:=rover;mem[rover+1].hh.rh:=rover;
lomemmax:=rover+1000;mem[lomemmax].hh.rh:=-32768;
mem[lomemmax].hh.lh:=-32768;
for k:=29987 to 30000 do mem[k]:=mem[lomemmax];
{790:}mem[29990].hh.lh:=8614;{:790}{797:}mem[29991].hh.rh:=128;
mem[29991].hh.lh:=-32768;{:797}{820:}mem[29993].hh.b0:=1;
mem[29994].hh.lh:=32767;mem[29993].hh.b1:=0;
{:820}{981:}mem[30000].hh.b1:=127;mem[30000].hh.b0:=1;
mem[30000].hh.rh:=30000;{:981}{988:}mem[29998].hh.b0:=10;
mem[29998].hh.b1:=0;{:988};avail:=-32768;memend:=30000;himemmin:=29987;
varused:=20;dynused:=14;{:164}{222:}eqtb[4781].hh.b0:=101;
eqtb[4781].hh.rh:=-32768;eqtb[4781].hh.b1:=-128;
for k:=1 to 4780 do eqtb[k]:=eqtb[4781];
{:222}{228:}eqtb[4782].hh.rh:=-32767;eqtb[4782].hh.b1:=-127;
eqtb[4782].hh.b0:=117;for k:=4783 to 5311 do eqtb[k]:=eqtb[4782];
mem[-32767].hh.rh:=mem[-32767].hh.rh+530;
{:228}{232:}eqtb[5312].hh.rh:=-32768;eqtb[5312].hh.b0:=118;
eqtb[5312].hh.b1:=-127;for k:=5313 to 5577 do eqtb[k]:=eqtb[4781];
eqtb[5578].hh.rh:=-32768;eqtb[5578].hh.b0:=119;eqtb[5578].hh.b1:=-127;
for k:=5579 to 5833 do eqtb[k]:=eqtb[5578];eqtb[5834].hh.rh:=0;
eqtb[5834].hh.b0:=120;eqtb[5834].hh.b1:=-127;
for k:=5835 to 5882 do eqtb[k]:=eqtb[5834];eqtb[5883].hh.rh:=0;
eqtb[5883].hh.b0:=120;eqtb[5883].hh.b1:=-127;
for k:=5884 to 7162 do eqtb[k]:=eqtb[5883];
for k:=0 to 255 do begin eqtb[5883+k].hh.rh:=12;
eqtb[6907+k].hh.rh:=k-32768;eqtb[6651+k].hh.rh:=1000;end;
eqtb[5896].hh.rh:=5;eqtb[5915].hh.rh:=10;eqtb[5975].hh.rh:=0;
eqtb[5920].hh.rh:=14;eqtb[6010].hh.rh:=15;eqtb[5883].hh.rh:=9;
for k:=48 to 57 do eqtb[6907+k].hh.rh:=k-4096;
for k:=65 to 90 do begin eqtb[5883+k].hh.rh:=11;
eqtb[5883+k+32].hh.rh:=11;eqtb[6907+k].hh.rh:=k-3840;
eqtb[6907+k+32].hh.rh:=k-3808;eqtb[6139+k].hh.rh:=k+32;
eqtb[6139+k+32].hh.rh:=k+32;eqtb[6395+k].hh.rh:=k;
eqtb[6395+k+32].hh.rh:=k;eqtb[6651+k].hh.rh:=999;end;
{:232}{240:}for k:=7163 to 7473 do eqtb[k].int:=0;eqtb[7180].int:=1000;
eqtb[7164].int:=10000;eqtb[7204].int:=1;eqtb[7203].int:=25;
eqtb[7208].int:=92;eqtb[7211].int:=13;
for k:=0 to 255 do eqtb[7474+k].int:=-1;eqtb[7520].int:=0;
{:240}{250:}for k:=7730 to 8006 do eqtb[k].int:=0;
{:250}{258:}hashused:=4514;cscount:=0;eqtb[4523].hh.b0:=116;
hash[4523].rh:=501;{:258}{552:}fontptr:=0;fmemptr:=7;fontname[0]:=798;
fontarea[0]:=337;hyphenchar[0]:=45;skewchar[0]:=-1;bcharlabel[0]:=0;
fontbchar[0]:=128;fontfalsebchar[0]:=128;fontbc[0]:=1;fontec[0]:=0;
fontsize[0]:=0;fontdsize[0]:=0;charbase[0]:=0;widthbase[0]:=0;
heightbase[0]:=0;depthbase[0]:=0;italicbase[0]:=0;ligkernbase[0]:=0;
kernbase[0]:=0;extenbase[0]:=0;fontglue[0]:=-32768;fontparams[0]:=7;
parambase[0]:=-1;for k:=0 to 6 do fontinfo[k].int:=0;
{:552}{946:}for k:=-trieopsize to trieopsize do trieophash[k]:=0;
for k:=0 to 255 do trieused[k]:=-128;trieopptr:=0;
{:946}{951:}trienotready:=true;triel[0]:=0;triec[0]:=0;trieptr:=0;
{:951}{1216:}hash[4514].rh:=1187;{:1216}{1301:}formatident:=1254;
{:1301}{1369:}hash[4522].rh:=1293;eqtb[4522].hh.b1:=-127;
eqtb[4522].hh.b0:=113;eqtb[4522].hh.rh:=-32768;
{:1369}{:8}{11:}memmax=30000;memmin=-32767;bufsize=5000;errorline=79;
halferrorline=50;maxprintline=79;stacksize=200;maxinopen=15;fontmax=127;
fontmemsize=40000;paramsize=60;nestsize=40;maxstrings=3000;
stringvacancies=8000;poolsize=60000;savesize=600;triesize=8000;
trieopsize=500;dvibufsize=800;filenamesize=1024;poolname='tex.pool';
{:11}{13:}bad:integer;{:13}{18:}ASCIIcode=0..255;{:18}{19:}i:integer;
{:19}{20:}xord:array[char]of ASCIIcode;xchr:array[ASCIIcode]of char;
{:20}{25:}eightbits=ByteCard;alphafile=text;
bytefile=packed file of eightbits;
{:25}{26:}nameoffile,realnameoffile:external UNIXfilename;
namelength:0..filenamesize;{:26}{27:}function aopenin(var f:alphafile;
pathspecifier:integer):boolean;var ok:boolean;
begin if testaccess(4,pathspecifier)then begin reset(f,realnameoffile);
ok:=true end else ok:=false;aopenin:=ok;end;
function aopenout(var f:alphafile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,realnameoffile);
ok:=true end else ok:=false;aopenout:=ok;end;
function bopenin(var f:bytefile):boolean;var ok:boolean;
begin if testaccess(4,3)then begin reset(f,realnameoffile);
ok:=true end else ok:=false;bopenin:=ok;end;
function bopenout(var f:bytefile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,realnameoffile);
ok:=true end else ok:=false;bopenout:=ok;end;
function wopenin(var f:wordfile):boolean;var ok:boolean;
begin if testaccess(4,4)then begin reset(f,realnameoffile);
ok:=true end else ok:=false;wopenin:=ok;end;
function wopenout(var f:wordfile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,nameoffile);
ok:=true end else ok:=false;wopenout:=ok;end;
{:27}{28:}procedure aclose(var f:alphafile);begin closea(f);end;
procedure bclose(var f:bytefile);begin closeb(f);end;
procedure wclose(var f:wordfile);begin closew(f);end;
{:28}{30:}buffer:array[0..bufsize]of ASCIIcode;first:0..bufsize;
last:0..bufsize;maxbufstack:0..bufsize;
{:30}{31:}function inputln(var f:alphafile;bypasseoln:boolean):boolean;
var lastnonblank:0..bufsize;
begin if bypasseoln then if not eof(f)then get(f);last:=first;
if eof(f)then inputln:=false else begin lastnonblank:=first;
while not eoln(f)do begin if last>=maxbufstack then begin maxbufstack:=
last+1;
if maxbufstack=bufsize then{35:}if formatident=0 then begin writeln(
output,'Buffer size exceeded!');goto 9999;
end else begin curinput.locfield:=first;curinput.limitfield:=last-1;
overflow(256,bufsize);end{:35};end;buffer[last]:=xord[f^];get(f);
last:=last+1;if buffer[last-1]<>32 then lastnonblank:=last;end;
last:=lastnonblank;inputln:=true;end;end;
{:31}{37:}function initterminal:boolean;label 10;begin;
while true do begin;write(output,'**');flushstdout;
if not inputln(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
input program TEX(input program TEX(input program TEX(input program TEX(
