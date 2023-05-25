clear all
format compact
format short
% PURPOSE: Read a smiley with inhomogeneous color gradation
%  run regionprops 
%  retain only those regions with a minimal size minsize
%  draw circles 
% USAGE: Standalone Example Program
% TODO: Extract only data of reasonable size

clf      

minsize=5 % minimal size in pixels

BW=imread('SmileyBW.jpeg');
subplot(1,3,1)
imshow(BW)
axis on
title('Original graphics')

logicalBW=(BW==0);

subplot(1,3,2)
hold on
spy(logicalBW)
% Locate all regions, including the rubbish
stats = regionprops("table",logicalBW,"Centroid", ...
    "MajorAxisLength","MinorAxisLength")

[n1,n2]=size(stats)
centroid= table2array(stats(:,1));
% Draw the centers of all regions, including the rubbish
for i=1:n1
  plot(centroid(i,1),centroid(i,2),'x')
end
title('Converted to logical, all centers  \newline of all regionprops marked with \times')


% Try to eliminate the rubbish
% by only retaining objects of more than minsize pixels
% and draw a circle
phicircle=linspace(0,2*pi,150);
xcircle=cos(linspace(0,2*pi,150));
ycircle=sin(linspace(0,2*pi,150));

subplot(1,3,3)
hold on
spy(logicalBW)
ireduced=0;
for i=1:n1
 if minsize<table2array(stats(i,3))
   ireduced=ireduced+1
   object(1,ireduced)=centroid(i,1);
   object(2,ireduced)=centroid(i,2);
   radi=table2array(stats(i,2));
   object(3,ireduced)=radi;
   plot(centroid(i,1),centroid(i,2),'x',...
       'Markersize',25,'Linewidth',3);
   plot(radi*xcircle+object(1,ireduced),...
        radi*ycircle+object(2,ireduced),'r-');
 end
end
title('Only centers for MinorAxisLength>minsize \newline marked with \times and circled with MajorAxisLength')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc regionprops_smiley.eps

return

mesh(Asmildata)
%shading interp
grid
return
subplot(1,2,1)
imshow(Asmildata)

subplot(1,2,2)
hold on
  [B,L,N,A] = bwboundaries(Asmildata);
        for k = 1:N
           % Boundary k is the parent of a hole if the k-th column
           % of the adjacency matrix A contains a non-zero element
           if nnz(A(:,k)) > 0
               boundary = B{k};
               plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2);
               % Loop through the children of boundary k
               for l = find(A(:,k))'
                   boundary = B{l};
                   plot(boundary(:,2), boundary(:,1), 'g', 'LineWidth', 2);
               end
           end
       end
whos

return


      BW = imread('blobs.png');
       [B,L,N,A] = bwboundaries(BW);
       figure; imshow(BW); hold on;
       % Loop through object boundaries
       for k = 1:N
           % Boundary k is the parent of a hole if the k-th column
           % of the adjacency matrix A contains a non-zero element
           if nnz(A(:,k)) > 0
               boundary = B{k};
               plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2);
               % Loop through the children of boundary k
               for l = find(A(:,k))'
                   boundary = B{l};
                   plot(boundary(:,2), boundary(:,1), 'g', 'LineWidth', 2);
               end
           end
       end
       
       return