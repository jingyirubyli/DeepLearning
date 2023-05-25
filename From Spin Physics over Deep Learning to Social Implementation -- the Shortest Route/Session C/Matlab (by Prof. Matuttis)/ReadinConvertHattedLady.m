clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale 
% USAGE: Standalone Example Program

Acolordata=imread('HattedLady.png');
Agraydata=rgb2gray(Acolordata);

subplot(2,2,1)
imshow(Acolordata)
% image(Acolordata)
axis image
title('original image')
subplot(2,2,2)
imshow(Agraydata)
axis image
title('greyscale conversion image')
subplot(2,3,4)
imshow(Acolordata(:,:,1))
axis image
title('R-Channel')
subplot(2,3,5)
imshow(Acolordata(:,:,2))
axis image
title('G-Channel')
subplot(2,3,6)
imshow(Acolordata(:,:,3))
axis image
title('B-Channel')

whos

return

