clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale and run a Laplace filter 
% USAGE: Standalone Example Program

Acolordata=imread('HattedLady.png');
%Acolordata=imread('SpecledEggs.jpg');
Agraydata=rgb2gray(Acolordata);

subplot(1,3,1)
imshow(Acolordata)
% image(Acolordata)
axis image
title('original image')
subplot(1,3,2)
imshow(Agraydata)
axis image
title('greyscale conversion image')

A_filter=[ 1/16  1/8 1/16
           1/8   1/4  1/8  
           1/16  1/8 1/16]
%Afiltered=conv2(Agraydata,A_filter);
Afiltered=imfilter(Agraydata,A_filter,'corr');

subplot(1,3,3)
imshow(Afiltered)
axis image
title('with D-Filter')

set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc LaplacefilteredLady.eps

return
A_Laplace=[40 31 39
           50 31 36
           45 31 65]/100
