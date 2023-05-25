function [maxheight1,maxheight2] = determinequad(Alllet,nx,ny)
% Determine the maximal height and widht of the letters
maxheight1=0 
maxheight2=0
for iy=0:8
  for ix=0:2 
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
      Quadsum1(i1)  
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
%     figure(2)
%     spy(Letterquad(start2:end2,start1:end1)<=10)
    height2=end2-start2+1;
    height1=end1-start1+1;
    if height2>maxheight2
        maxheight2=height2;
    end
    if height1>maxheight1
        maxheight1=height1;
    end

%    Nin=input('Next?')
  end
end


return
