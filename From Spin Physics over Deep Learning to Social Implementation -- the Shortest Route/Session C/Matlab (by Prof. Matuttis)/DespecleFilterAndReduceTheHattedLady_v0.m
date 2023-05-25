clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale and run a Laplace filter 
% USAGE: Standalone Example Program

Acolordata=imread('HattedLady.png');
%Acolordata=imread('SpecledEggs.jpg');
Agraydata=rgb2gray(Acolordata);

nstep=2

clf
axes('position',[0+.012,.53,1/3,0.4])
%subplot(2,3,1)
imshow(Agraydata)
axis on
title('greyscale original')

axes('position',[1/3+.012,.53,1/3,0.4])
Aoriginalreduced=Agraydata(1:nstep:end,1:nstep:end,:);
imshow(Aoriginalreduced)
axis on
title('every 2nd pixel of original')

axes('position',[2/3+.012,.53,1/3,0.4])
Aoriginalreduced2=Aoriginalreduced(1:nstep:end,1:nstep:end,:);
imshow(Aoriginalreduced2)
axis on
title('every 4th pixel of original')


A_filter=[ 1/16  1/8 1/16
          1/8   1/4  1/8  
          1/16  1/8 1/16]
% A_filter=[21 31 21 
%           31 48 31 
%           21 31 21]/256
%Afiltered=conv2(Agraydata,A_filter);
Afiltered=imfilter(Agraydata,A_filter,'corr');
axes('position',[0+.012,0.045,1/3,0.4])
imshow(Afiltered)
axis on
title('filtered (blurred) once')

axes('position',[1/3+.012,0.045,1/3,0.4])
Afilteredreduced=Afiltered(1:nstep:end,1:nstep:end,:);
imshow(Afilteredreduced)
axis on
title('every 2nd pixel of filtered')

axes('position',[2/3+.012,0.045,1/3,0.4])
Afiltered2=imfilter(Afilteredreduced,A_filter,'corr');
Afilteredreduced2=Afiltered2(1:nstep:end,1:nstep:end,:);
imshow(Afilteredreduced2)
axis on
title('blurred again, every 2nd pixel')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc SmoothedCompressedLady.eps

return
A_Laplace=[40 31 39
           50 31 36
           45 31 65]/100
