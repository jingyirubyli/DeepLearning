function [patterns]=...
    ReadinFontOutputPatternsBlockschrift(nquad1,nquad2)
% Display all patterns in a 3x9-Diagram
% No interruption
ipattern=0
figure(1)
[Allet,map]=imread('blockschrift.gif');
Allet=sum(Allet,3)/3;
image(Allet)
hold on
[ny,nx]=size(Allet);
startheight1=45
height=100
startheight2=172


plot([0, nx],startheight1+[0 0],'k-')
plot([0, nx],startheight1+height+[0 0],'k-')
plot([0, nx],startheight2+[0 0],'k-')
plot([0, nx],startheight2+height+[0 0],'k-')



Firstline=Allet(startheight1:startheight1+height,:);
 

figure(3)
Firstlineis0=(Firstline==0);
intersect_hor=sum(Firstlineis0,1);
semilogy(intersect_hor,'+-')
intersect_ver=sum(Firstlineis0,2);
for i=1:length(intersect_ver)-1
  if (intersect_ver(i)==0)&(intersect_ver(i+1)>0)
    starty=startheight1+i-2;
  end
  if (intersect_ver(i+1)==0)&(intersect_ver(i)>0)
    endy=startheight1+i+1;
  end
end


figure(1)
ipat=0;
for i=1:nx-1
  if (intersect_hor(i)==0)&(intersect_hor(i+1)>0)
    ipat=ipat+1;
    startx(ipat)=i;
    plot(i+[0 0],[startheight1 startheight1+height],'kx-')
  end
  if (intersect_hor(i+1)==0)&(intersect_hor(i)>0)
    endx(ipat)=i+1;
    plot(i+1+[0 0],[startheight1 startheight1+height],'ko-')
  end
end

figure(4)
npat=ipat;
nletter=0
for ipat=1:npat
  subplot(4,7,ipat)
  image(Allet(starty:endy,startx(ipat):endx(ipat)))
  axis image
  nletter=nletter+1;
  letterquad(nletter)={Allet(starty:endy,startx(ipat):endx(ipat))==0};
end


 Secline=Allet(startheight2:startheight2+height,:);
 Seclineis0=(Secline==0);
intersect_hor=sum(Seclineis0,1);
%semilogy(intersect_hor,'+-')
intersect_ver=sum(Firstlineis0,2);
for i=1:length(intersect_ver)-1
  if (intersect_ver(i)==0)&(intersect_ver(i+1)>0)
    starty=startheight2+i-2;
  end
  if (intersect_ver(i+1)==0)&(intersect_ver(i)>0)
    endy=startheight2+i+1;
  end
end


figure(1)
ipat=0;
for i=1:nx-1
  if (intersect_hor(i)==0)&(intersect_hor(i+1)>0)
    ipat=ipat+1;
    startx(ipat)=i;
    plot(i+[0 0],[startheight2 startheight2+height],'kx-')
  end
  if (intersect_hor(i+1)==0)&(intersect_hor(i)>0)
    endx(ipat)=i+1;
    plot(i+1+[0 0],[startheight2 startheight2+height],'ko-')
  end
end

figure(5)
npat=ipat;
for ipat=1:npat
  subplot(4,7,ipat)
  image(Allet(starty:endy,startx(ipat):endx(ipat)))
  axis image
  nletter=nletter+1;
  letterquad(nletter)={Allet(starty:endy,startx(ipat):endx(ipat))==0};
end


maxheight1=0
maxheight2=0

for i=1:nletter
  [n1,n2]=size(cell2mat(letterquad(i)))
  if n1>maxheight1
    maxheight1=n1;
  end    
  if n2>maxheight2
    maxheight2=n2;
  end    
end
halfmaxheight1=round(maxheight1/2+.5)
halfmaxheight2=round(maxheight2/2+.5)

  figure(2)
  clf
for i=1:length(letterquad)
  fullquad=zeros(maxheight1,maxheight2);
%   subplot(1,2,1)
%   spy(fullquad)
  innerpattern=cell2mat(letterquad(i));
%   subplot(1,2,2)
%  spy(innerpattern)
  [height1,height2]=size(innerpattern)
  start1=round(halfmaxheight1-height1/2);
  start2=round(halfmaxheight2-height2/2);
  fullquad(start1+1:start1+height1,...
           start2+1:start2+height2)=innerpattern;
%  subplot(3,9,i)
%  spy(fullquad)
%coarsen   
  Coarsequad=zeros(nquad1,nquad2);
  for i1=1:maxheight1
    for i2=1:maxheight2
      if  fullquad(i1,i2)==1
         Coarsequad(floor(i1*nquad1/maxheight1),...
                    floor(i2*nquad2/maxheight2))=1; 
      end
    end
  end
  Coarsequad=Coarsequad(1:nquad1,1:nquad2);
  subplot(3,9,i)
  spy(Coarsequad)  
%  input('continue?')
  patterns(i)={Coarsequad};
end    


return
    