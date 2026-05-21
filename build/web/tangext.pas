function argc: Integer;
begin
  argc := ParamCount + 1;
end;

procedure Argv(no: Integer; var str: UNIXfile_name);
var
  s: string;
  i: Integer;
begin
  s := ParamStr(no);
  for i := 1 to 60 do
    if i <= Length(s) then
      str[i] := s[i]
    else
      str[i] := ' ';
end;

procedure Flushstdout;
begin
  flush(output);
end;

function trim(s: UNIXfile_name): string;
var
  i: Integer;
  res: string;
begin
  res := '';
  for i := 1 to 60 do
    if s[i] <> ' ' then
      res := res + s[i];
  trim := res;
end;

procedure Lineread(var f: Text);
var
  c: char;
  cnb: Integer;
begin
  limit := 0;
  cnb := 0;
  while not eoln(f) do
  begin
    read(f, c);
    if limit < bufsize then
    begin
      buffer[limit] := xord[c];
      if buffer[limit] <> xord[' '] then
        cnb := limit + 1;
      limit := limit + 1;
    end;
  end;
  if not eof(f) then readln(f);
  limit := cnb;
end;

function Testeof(var f: Text): Boolean;
begin
  Testeof := eof(f);
end;
