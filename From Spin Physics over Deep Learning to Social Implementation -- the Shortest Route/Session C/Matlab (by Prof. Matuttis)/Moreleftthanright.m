clear all
format compact
format short
% PURPOSE: perceptron to decide whether there are 
%   more 1s (pixels)on the left than on the right
% USAGE: Standalone Program, set your input as matrix
%   with 1s and 0s
% ALGORITHM: Use  weights -1 for the left pixels and
%   +1 for the right pixels,
%    convert the patterns into vectors
% LITERATUR: None, I had to come up with that myself
% AUTHOR: Hans-Georg Matuttis
% REVISION HISTORY: 
%   Mo Apr  3 19:06:34 JST 2023
%   dot-product instead of elementwise matrix multiplication
% CAVEAT: Needs a modification for odd number of columns 
% TODO/EXERCISE: Decide which weights should be used 
%  if the number of columns is not even as in the program
%  but odd
% Rewrite for a general-sized matrix
% Rewrite for arbitrary non-zero entries into the matrix



xin_1=[0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1
       0 0 0 0 1 1 1 1]
   
xin_2=[1 1 1 1 0 0 0 0 
       1 1 1 1 0 0 0 0
       1 1 1 1 0 0 0 0
       1 1 1 1 0 0 0 0
       1 1 1 1 0 0 0 0
       1 1 1 1 0 0 0 0
       1 1 1 1 0 0 0 0]
  
xin_3=[1 1 1 1 0 0 0 0 
       1 1 1 1 0 0 0 1
       1 0 1 1 0 1 0 0
       1 1 1 1 0 0 0 0
       1 1 1 1 0 1 0 0
       1 1 1 1 0 0 0 1
       1 1 1 1 0 0 0 0]
  
w=[-1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1
   -1 -1 -1 -1 1 1 1 1]
  
% A(:) converts a matrix A to a vector
% try out by yourself whether it is a row- or a column-vector
Totalsum_1=dot(xin_1(:),w(:))
sign(Totalsum_1)
if sign(Totalsum_1)<0
  disp('more pixels on the left')
elseif sign(Totalsum_1)>0
  disp('more pixels on the right')
elseif sign(Totalsum_1)==0
  disp('Same number of pixels on the right as to the left')
else
  disp('This is impossible')
end
  
Totalsum_2=dot(xin_2(:),w(:))
sign(Totalsum_2)
if sign(Totalsum_2)<0
  disp('more pixels on the left')
elseif sign(Totalsum_2)>0
  disp('more pixels on the right')
elseif sign(Totalsum_2)==0
  disp('Same number of pixels on the right as to the left')
else
  disp('This is impossible')
end    
 
  
return

