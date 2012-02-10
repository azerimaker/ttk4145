with Ada.Text_IO;
use Ada.Text_IO;

procedure hello_world is
    
    name    :   String(1 .. 30);
    i       :   INTEGER;    
    
begin
    Put("Please enter your name: ");
    Get_Line(name, i);
    Put("The Hive Mind greets you, ");
    Put(name (1 .. i));
end hello_world;
