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

minsize=15 % minimal size in pixels

BW=imread('Matuttis.jpg');
subplot(1,4,1)
imshow(BW)
axis on
title('Original graphics')


logicalBW=(sum(double(BW),3)<350);

subplot(1,4,2)
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
title('Converted to logical, all \newline regionprops centers marked')


% Try to eliminate the rubbish
% by only retaining objects of more than minsize pixels
% and draw a circle
phicircle=linspace(0,2*pi,150);
xcircle=cos(linspace(0,2*pi,150));
ycircle=sin(linspace(0,2*pi,150));

subplot(1,4,3)
hold on
spy(logicalBW)
nreduced=0;
for i=1:n1
 if minsize<table2array(stats(i,3))
   nreduced=nreduced+1
   object(1,nreduced)=centroid(i,1);
   object(2,nreduced)=centroid(i,2);
   radi=.5*(table2array(stats(i,2))+table2array(stats(i,3)));
   object(3,nreduced)=radi;
   plot(centroid(i,1),centroid(i,2),'x',...
       'Markersize',25,'Linewidth',3);
   plot(radi*xcircle+object(1,nreduced),...
        radi*ycircle+object(2,nreduced),'r-');
 end
end
title('centers >minsize radius \newline 0.5*(MinorAxisLength+MinorAxisLength)')

subplot(1,4,4)
[nhor,nver,n3]=size(BW);
hold on
% copy all pixels which are in the recognized circles
copyimage=uint8(255+zeros(size(BW)));
% Index Nr 1 is the whole face, cannot be used!
for ireduced=2:nreduced
  radius=object(3,ireduced);
  horcenter=object(2,ireduced);
  vercenter=object(1,ireduced);
  for ihor=round(horcenter-radius):round(horcenter+radius)
    for iver=round(vercenter-radius):round(vercenter+radius)
      if (ihor>0)&(ihor<=nhor)
        if (iver>0)&(iver<=nver)
          deltahor=horcenter-ihor;  
          deltaver=vercenter-iver;
          if sqrt(deltahor^2+deltaver^2)<radius
            copyimage(ihor,iver,:)=BW(ihor,iver,:); 
          end
        end
      end
    end
  end
end
imshow(copyimage)
axis on
axis tight
title('Copied parts')


set(gca,'LooseInset',get(gca,'TightInset'));
print -depsc regionprops_Matuttis.eps

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