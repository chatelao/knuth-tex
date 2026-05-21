{11:}memmax=30000;maxinternal=100;bufsize=500;errorline=79;
halferrorline=50;maxprintline=79;screenwidth=1024;screendepth=800;
stacksize=30;maxstrings=3000;stringvacancies=18000;poolsize=42000;
movesize=5000;maxwiggle=300;gfbufsize=800;filenamesize=1024;
poolname='mf.pool';pathsize=300;bistacksize=785;headersize=100;
ligtablesize=5000;maxkerns=500;maxfontdimen=50;{:11}{13:}bad:integer;
{:13}{18:}ASCIIcode=0..255;{:18}{19:}i:integer;
{:19}{20:}xord:array[char]of ASCIIcode;xchr:array[ASCIIcode]of char;
{:20}{21:}xchr[32]:=' ';xchr[33]:='!';xchr[34]:='"';xchr[35]:='#';
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
{:21}{22:}for i:=0 to 31 do xchr[i]:=chr(i);
for i:=127 to 255 do xchr[i]:=chr(i);
{:22}{23:}for i:=0 to 255 do xord[chr(i)]:=127;
for i:=128 to 255 do xord[xchr[i]]:=i;
for i:=0 to 126 do xord[xchr[i]]:=i;{:23}{24:}eightbits=0..255;
alphafile=text;bytefile=packed file of-128..127;
{:24}{25:}nameoffile,realnameoffile:packed array[1..filenamesize]of char
;namelength:0..filenamesize;{:25}{26:}function aopenin(var f:alphafile;
pathspecifier:integer):boolean;var ok:boolean;
begin if testaccess(4,pathspecifier)then begin reset(f,realnameoffile);
ok:=true end else ok:=false;aopenin:=ok;end;
function aopenout(var f:alphafile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,realnameoffile);
ok:=true end else ok:=false;aopenout:=ok;end;
function bopenout(var f:bytefile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,realnameoffile);
ok:=true end else ok:=false;bopenout:=ok;end;
function wopenin(var f:wordfile):boolean;var ok:boolean;
begin if testaccess(4,4)then begin reset(f,realnameoffile);
ok:=true end else ok:=false;wopenin:=ok;end;
function wopenout(var f:wordfile):boolean;var ok:boolean;
begin if testaccess(2,0)then begin rewrite(f,nameoffile);
ok:=true end else ok:=false;wopenout:=ok;end;
{:26}{27:}procedure aclose(var f:alphafile);begin closea(f);end;
procedure bclose(var f:bytefile);begin closeb(f);end;
procedure wclose(var f:wordfile);begin closew(f);end;
{:27}{29:}buffer:array[0..bufsize]of ASCIIcode;first:0..bufsize;
last:0..bufsize;maxbufstack:0..bufsize;
{:29}{30:}function inputln(var f:alphafile;bypasseoln:boolean):boolean;
label 30;begin last:=first;
if testeof(f)then inputln:=false else begin last:=first;
lineread(f,bufsize);if last>maxbufstack then begin maxbufstack:=last;
if maxbufstack>=bufsize then{34:}if baseident=0 then begin writeln(
output,'Buffer size exceeded!');goto 9999;
end else begin curinput.locfield:=first;curinput.limitfield:=last-1;
overflow(256,bufsize);end{:34};end;
while true do begin if last=first then goto 30;
if buffer[last-1]<>32 then goto 30;last:=last-1;end;30:inputln:=true;
end;end;{:30}{36:}function initterminal:boolean;label 10;
var dummy,i,j,k:integer;arg:packed array[1..100]of char;begin;
if argc>1 then begin last:=first;
for i:=1 to argc-1 do begin argv(i,arg);j:=1;k:=100;
while(k>1)and(arg[k]=' ')do k:=k-1;
while(j<=k)do begin buffer[last]:=xord[arg[j]];j:=j+1;last:=last+1;end;
if k>1 then begin buffer[last]:=xord[' '];last:=last+1;end;end;
if last>first then begin curinput.locfield:=first;initterminal:=true;
goto 10;end;end;while true do begin;write(output,'**');flush(output);
if not inputln(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
program MF(input program MF(input program MF(input program MF(input
