with Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO, Ada.Integer_Text_IO;

procedure fibonacci is
    function fib (N:Integer) return Integer is
    begin
        if n < 2 then
            return n;
        elsif n = 2 then
            return 1;
        elsif n mod 2 = 0 then
            return (fib( (n/2-1) ) + fib( (n/2+1) )) * fib(n/2);
        else
            return fib(n/2)**2 + fib(n/2+1)**2 ;
        end if;
    end fib;
    N:INTEGER;
begin
    Put("enter n");
    Get(N);
    Put(fib(N));
end fibonacci;
