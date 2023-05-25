clear all
format compact
format short
% PURPOSE: Read in a ``Black and white''
% graphics and show the color gradation at the edges
% USAGE: Standalone Example Program

Asmildata=imread('MatlabIcon.jpeg');

clf
%surfc(Asmildata(:,:,3))
%shading interp
%return
subplot(1,4,1)
imshow(Asmildata)  
axis image
title('original image')

subplot(1,4,2)
surf(Asmildata(:,:,1))
axis image
title('Red channel with surf,\newline shading palette')

subplot(1,4,3)
surf(Asmildata(:,:,2))
shading interp
axis image
title('Green channel with surf, \newline shading interpolated')

subplot(1,4,4)
surfc(Asmildata(:,:,3))
shading interp
axis image
title('Blue channel with surfc, \newline shading interpolated')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc OtherGraphingStyles.eps
grid
return
