С использованием теорем сочетания построить НА, который аннулирует все слова вида x$x, где x in{a,b}*, а $ not in {a, b}.

^ - вместо $
% - alpha
+ - beta
& - gamma
x - a or b or ^
L - a or b
?


НА:

A$a -> $
B$b -> $
Aa -> aA
Ab -> bA
Ba -> aB
Bb -> bB
%a -> %A
%b -> %B
%$ => 
->%


---------------------------------------------------------------

A&a -> a&
B&b -> b&
Aa -> aA
Ab -> bA
A^ -> ^A
Ba -> aB
Bb -> bB
B^ -> ^B
%a -> a%A
%b -> b%B
#a -> a#
#b -> b#
#&a => a
#&b => b
a@ -> @
b@ -> @
$@ -> @
@ => 
#& -> @
a< -> <a
A< -> <
B< -> <
b< -> <b
$< -> <$
%< -> <
< =>
A& -> <
B& -> <
%^ -> $#
$ -> ^&
a -> %a
b -> %b
^& => 
^ => 


Пример 1: 

aba$aba:

aba$aba -> (8) aba^&aba -> (9) %aba^&aba -> (5) -> a%Aba^&aba -> (3...) a%ba^A&aba -> (1) a%ba^a&ba ->  ab%Ba^a&ba -> ab%a^aB&ba -> ab%a^ab&a -> aba%A^ab&a ->aba%^abA&a -> aba%^aba& ->
aba%^aba# -> ... # ->! empty

Пример 2:

aba$abad

aba$abad -> (8) aba^&abad -> (9) %aba^&abad -> (5) -> a%Aba^&abad -> (3...) a%ba^A&abad -> ...
-> aba%^aba&d -> aba$abad

Пример 3:

abad$aba -> abad^&aba -> 