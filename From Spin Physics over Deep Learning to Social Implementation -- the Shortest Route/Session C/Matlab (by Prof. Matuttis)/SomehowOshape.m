clear all
format compact
format short
% PURPOSE: perceptron to decide whether the input-shape
%   is somehow an "O" shape
% USAGE: Standalone Program, set your input as matrix
%   with 1s and 0s
% ALGORITHM: Use  weights -1 for the left pixels and
%   +1 for the right pixels,
%    convert the patterns into vectors
% LITERATURE: None, I had to come up with that myself
% AUTHOR: Hans-Georg Matuttis
% REVISION HISTORY: 
%   Mo Apr  3 19:06:34 JST 2023
%   dot-product instead of elementwise matrix multiplication
% CAVEAT: If this one works properly, I will be very suprised,
%   I cobbled together the weights after a hard day 
%   in the office
% TODO/EXERCISE: Decide which weights should be used 
%  if the number of columns is not even as in the program
%  but odd
% Rewrite for a general-sized matrix
% Rewrite for arbitrary non-zero entries into the matrix



xin_2=[0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1]
   
xin_1=[0 1 1 1 1 1 1 0 
       1 1 1 1 0 1 1 1
       1 0 0 0 0 0 1 1
       1 1 1 1 1 1 1 1
       1 1 0 0 0 0 1 1
       1 1 0 0 0 0 1 1
       1 1 1 1 0 1 1 0]

  
xin_1=[0 1 1 1 1 1 1 0 
       1 1 1 1 0 1 1 1
       1 0 1 0 0 1 1 1
       1 1 0 0 0 0 1 1
       1 1 0 0 0 0 1 1
       1 1 0 0 0 0 1 1
       1 1 1 1 0 1 1 0]
  


w=[-1  1   1  1  1  1  1 -1
    1  1   1  1  1  1  1  1
    1  1  -4 -4 -4 -4  1  1
    1  1  -4 -4 -4 -4  1  1
    1  1  -4 -4 -4 -4  1  1
    1  1   1  1  1  1  1  1
   -1  1   1  1  1  1  1 -1]
% If you want to "absolutely forbid" that there are
% any pixels in the Middle, you can replace -4 by 
% negative numbers of even greater magnitude


% A(:) converts a matrix A to a vector
% try out by yourself whether it is a row- or a column-vector
Totalsum_1=dot(xin_1(:),w(:))
sign(Totalsum_1)
if sign(Totalsum_1)<0
  disp('Not an O')
elseif sign(Totalsum_1)>0
  disp('An O')
elseif sign(Totalsum_1)==0
  disp('Bordercase O')
else
  disp('This is impossible')
end
  
 
 
  
return

