with Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO, Ada.Integer_Text_IO;

procedure fibonacci is
	n:INTEGER;
begin
	Put("Enter fib num: ");
	Get(n);
	fib(n);
end fibonacci;



procedure fib (n) is
begin
    if n < 2 then
        Put(n);
    elsif n = 2 then
        Put(1);
    elsif n mod 2 = 0 then
        Put( (fib(n/2-1) + fib(n/2+1)) * fib(n/2) );
    else
        Put( fib(n/2)**2 + fib(n/2+1)**2 );
    end if;
end fib;
