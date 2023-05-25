function [patterns]=...
    ReadinFontOutputPatterns(nquad1,nquad2)
% Display all patterns in a 3x9-Diagram
% No interruption
%   spy(fullquad)


ipattern=0
figure(1)
Alllet=imread('BerkeliumScreen.png');
image(Alllet)
hold on
ny=89
nx=96
firoffs=13
firhi=69
sechi=72

secoffs=7
for ifir=0:9
  for isec=0:3
    plot(firoffs+[ifir*ny ifir*ny],secoffs+[isec*nx (isec+1)*nx],'r-') 
    plot(firoffs+[ifir*ny (ifir+1)*ny],secoffs+[isec*nx isec*nx],'b-') 
    plot(firoffs+[ifir*ny ifir*ny]+firhi,secoffs+[isec*nx (isec+1)*nx],'r-','Linewidth',2) 
    plot(firoffs+[ifir*ny (ifir+1)*ny],secoffs+[isec*nx isec*nx]+sechi,'b-','Linewidth',2)  

  end
end
%return
% Make n-by-n fonts, surrounding rows empty
% For 16x16 fonts, let 1 right- left- upper- lower row empty

[n1,n2,n3]=size(Alllet);

[maxheight1,maxheight2] =determinequad(Alllet,nx,ny)

figure(2)
% embed the letters in the quad of dimension maxheight1,maxheight2
for ix=0:2 
  for iy=0:8
 % Cut out the quad for the letter    
%    Letterquad=Alllet(ix*nx+1:(ix+1)*nx,iy*ny+1:(iy+1)*ny-2,:);
    Letterquad=Alllet(ix*nx+1:(ix+1)*nx,iy*ny+1:(iy+1)*ny-2,:);
    Letterquad=Letterquad(:,:,1);
    Letterblack=sum(Letterquad,3)<32;
% Identify the letter quad
    Quadsum1=sum(Letterblack,1);
    Quadsum2=sum(Letterblack,2);
    for i1=1:length(Quadsum1)
      if Quadsum1(i1)>4 % remove small bits
        start1=i1;
        break    
      end
    end
    for i1=length(Quadsum1):-1:1
      if Quadsum1(i1)>4 % remove small bits
        end1=i1;
        break    
      end
    end

    for i1=1:length(Quadsum2)
      if Quadsum2(i1)>4 % remove small bits
        start2=i1;
        break    
      end
    end
    for i1=length(Quadsum2):-1:1
      if Quadsum2(i1)>4 % remove small bits
        end2=i1;
        break    
      end
    end
    height2=end2-start2+1;
    height1=end1-start1+1;
    Letterquad(start2:end2,start1:end1)=Letterquad(start2:end2,start1:end1)<=10;
%    spy(Letterquad(start2:end2,start1:end1))
    Bufferquad=zeros(maxheight2,maxheight1);
%    subplot(2,2,2)
    Bufferquad(1:height2,1:height1)=Letterquad(start2:end2,start1:end1);
%    spy(Bufferquad)
%    subplot(2,2,3)
% Align center of letter with center bit
    offset1=floor(.5*(maxheight1-height1));
    Bufferquadc=zeros(maxheight2,maxheight1);
% Align heigest pixel with the height
    Bufferquadc(1:height2,1+offset1:height1+offset1)=Letterquad(start2:end2,start1:end1);
%    spy(Bufferquadc)

% Rescale:     
    Coarsequad=zeros(nquad2,nquad1);
% To use: only the quad with coordinates 2:n2-1, 2:n1-1
    d2=floor(maxheight2/(nquad2-2));
    d1=floor(maxheight1/(nquad1-2));
    
    icoarse2=0;
    for i2=1:d2:maxheight2-1
      icoarse2=icoarse2+1;
      icoarse1=0;
      for i1=1:d1:maxheight1-1
        icoarse1=icoarse1+1;
        maxind1=i1+d1-1;
        if maxind1>maxheight1
           maxind1=maxheight1;
        end        
        minind1=i1-1;
        if minind1<1
           minind1=1;
        end 
        maxind2=i2+d2-1;
        if maxind2>maxheight2
           maxind2=maxheight2;
        end 
        minind2=i2-1;
        if minind2<1
           minind2=1;
        end 

        Bufferquadcut=Bufferquadc(minind2:maxind2,minind1:maxind1);
        Bufferquadcut1=Bufferquadcut*0+1;
        Coarsequad(icoarse2,icoarse1)=...
        round(sum(Bufferquadcut(:))/sum(Bufferquadcut1(:)));
      end
    end

    Coarsequad=Coarsequad(1:nquad2,1:nquad1);
    
    ipattern=ipattern+1
    if ipattern<27
        subplot(3,9,ipattern)
        spy(Coarsequad)
        axis off
        title(ipattern)
        patterns(ipattern)={Coarsequad};
    end
%    Nin=input('Next?')
  end
end

return
