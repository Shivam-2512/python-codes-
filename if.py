Python 3.7.0rc1 (v3.7.0rc1:dfad352267, Jun 12 2018, 07:05:25) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=int(input())
if a>4
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'if a>4'
>>> a=int(input())
if a>4;
SyntaxError: multiple statements found while compiling a single statement
>>> a=int(input())
if a>4:
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'if a>4:'
>>> a=int(input())
if a>4 : {
	
SyntaxError: multiple statements found while compiling a single statement
>>> a = int(input())
if a>4:{  print(+a+'is greater than 4.')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: "if a>4:{  print(+a+'is greater than 4.')"
>>> a=int(input())
	  
4
>>> if a>4 :
	  {
		  print(+a+' is greater than 4.')
		  }
	  
