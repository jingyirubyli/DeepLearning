clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale and run a Laplace filter 
% USAGE: Standalone Example Program

Acolordata=imread('UECmain.jpeg');
Agraydata=rgb2gray(Acolordata);

clf
axes('position',[0,.4,1/4,0.26])
imshow(Acolordata)
% image(Acolordata)
axis image
title('original image')

axes('position',[1/4,.4,1/4,0.26])
imshow(Agraydata)
axis image
title('greyscale conversion image')

A_Laplace=-[0  1 0
           1 -4 1 
           0  1 0]
Afiltered1=conv2(Agraydata,A_Laplace);
Afiltered2=imfilter(Agraydata,A_Laplace,'corr');

axes('position',[2/4,.4,1/4,0.26])
imshow(Afiltered1)
axis image
title('Laplace-Filter, corr2')

axes('position',[3/4,.4,1/4,0.26])
imshow(Afiltered2)
axis image
title('Laplace-Filter, imfilter')

set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc LaplacefilteredUEC.eps

return

