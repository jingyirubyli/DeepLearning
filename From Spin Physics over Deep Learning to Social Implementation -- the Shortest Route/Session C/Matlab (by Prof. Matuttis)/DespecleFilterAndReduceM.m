clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale and run a Laplace filter 
% USAGE: Standalone Example Program

Acolordata=imread('М_With_Serifs.png');
%Acolordata=imread('SpecledEggs.jpg');
Agraydata=rgb2gray(Acolordata);

nstep=2

clf
axes('position',[0+.04,.53,1/4,0.38])
%subplot(2,3,1)
imshow(Agraydata)
axis on
title('greyscale original')

axes('position',[1/4+1.6*.04,.53,1/4,0.38])
Aoriginalreduced=Agraydata(1:nstep:end,1:nstep:end,:);
imshow(Aoriginalreduced)
axis on
title('every 2nd pixel of original')

axes('position',[2/4+4*.022,.53,1/4,0.38])
Aoriginalreduced2=Aoriginalreduced(1:nstep:end,1:nstep:end,:);
imshow(Aoriginalreduced2)
axis on
title('every 4th pixel of original')

axes('position',[3/4+4*.022,.53+6*.012,1.4/8,0.23])
%axes('position',[3/4+5*.022,.53+6*.012,1/8,0.2])
imshow(Aoriginalreduced2)

title('every 4th \newline pixel of original \newline downsized')


% A_filter=[ 1/16  1/8 1/16
%           1/8   1/4  1/8  
%           1/16  1/8 1/16]

% A_filter=...
% [0 0  1   2   1   0  0 
%  0 3  13  22  13  3  0 
%  1 13 59  97  59  13 1 
%  2 22 97  159 97  22 2 
%  1 13 59  97  59  13 1 
%  0 3  13  22  13  3  0 
%  0 0  1   2   1   0  0] / 1003
      
% A_filter=[21 31 21 
%           31 48 31 
%           21 31 21]/256

A_filter=[1 2 1 
          1 2 1 
          1 2 1 ]

%Afiltered=conv2(Agraydata,A_filter);
Afiltered=imfilter(Agraydata,A_filter,'corr');
axes('position',[0+.04,0.045,1/4,0.38])
imshow(Afiltered)
axis on
title('filtered (blurred) once')

axes('position',[1/4+1.6*.04,0.045,1/4,0.38])
%axes('position',[1/4+2*.012,0.045,1/4,0.4])
Afilteredreduced=Afiltered(1:nstep:end,1:nstep:end,:);
imshow(Afilteredreduced)
axis on
title('every 2nd pixel of filtered')

axes('position',[2/4+4*.022,0.045,1/4,0.38])
%axes('position',[1/4+1.6*.04,0.045,1/4,0.38])
Afiltered2=imfilter(Afilteredreduced,A_filter,'corr');
Afilteredreduced2=Afiltered2(1:nstep:end,1:nstep:end,:);
imshow(Afilteredreduced2)
axis on
title('blurred again, every 2nd pixel')

axes('position',[3/4+4*.022,0.045+6*.012,1.4/8,0.23])
imshow(Afilteredreduced2)
title('every 4th \newline pixel of original \newline downsized')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc  SmoothedCompressed_M.eps

return
A_Laplace=[40 31 39
           50 31 36
           45 31 65]/100
