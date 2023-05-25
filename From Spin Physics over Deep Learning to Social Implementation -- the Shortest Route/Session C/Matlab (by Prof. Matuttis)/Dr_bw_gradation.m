clear all
format compact
format short
% PURPOSE: Read in a ``Black and white''
% graphics and show the color gradation at the edges
% USAGE: Standalone Example Program

Asmildata=imread('SmileyBW.jpeg');
subplot(1,2,1)
imshow(Asmildata)  
axis image
title('original image')

subplot(1,2,2)
mesh(Asmildata)
axis image
title('Actual color values')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc BW_shading.eps
grid
return
