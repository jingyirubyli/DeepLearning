clear all
format compact
format short

nsweep=200
nout=10

format +
A=[-1 -1 +1 +1 -1 -1 
   -1 +1 -1 -1 +1 -1
   +1 -1 -1 -1 -1 +1
   +1 +1 +1 +1 +1 +1
   +1 -1 -1 -1 -1 +1
   +1 -1 -1 -1 -1 +1]

B=[+1 +1 +1 +1 -1 -1 
   +1 -1 -1 -1 +1 -1
   +1 +1 +1 +1 -1 -1
   +1 -1 -1 -1 +1 -1
   +1 -1 -1 -1 +1 -1
   +1 +1 +1 +1 -1 -1]

C=[-1 +1 +1 +1 -1 -1 
   +1 -1 -1 -1 +1 -1
   +1 -1 -1 -1 -1 -1
   +1 -1 -1 -1 -1 -1
   +1 -1 -1 -1 +1 -1
   -1 +1 +1 +1 -1 -1]

D=[+1 +1 +1 +1 -1 -1 
   +1 -1 -1 -1 +1 -1
   +1 -1 -1 -1 +1 -1
   +1 -1 -1 -1 +1 -1
   +1 -1 -1 -1 +1 -1
   +1 +1 +1 +1 -1 -1]

sA=A(:);
sB=B(:);
sC=C(:);
sD=D(:);

Patternmat=[sA sB sC sD]


Jij=-Patternmat*Patternmat';
for i=1:length(Jij)
  Jij(i,i)=0;
end
Jij


[Lx,Ly]=size(A)
% set up X- and Y-coordinates for graphics
[Xpos,Ypos]=meshgrid(1:Lx,1:Ly);
xcoord=[0 1 1 0 0]+.5;
ycoord=[0 0 1 1 0]+.5;

Ain=B;
v=Ain(:)'

Energy=v*Jij*v'

vnew=v;


for isweep=1:nsweep
  iselect=round(length(v)*rand+.5); 
  vnew(iselect)=-vnew(iselect); 
  Energynew=vnew*Jij*vnew';
  if (Energynew<=Energy) % T=0
    Energy=Energynew;
    v=vnew;
  else
    vnew=v;
  end
  
  if nout*round(isweep/nout)==isweep
    reshape(v,6,6) % terminal output
  end
  
% Graphic window output  
    figure(1)
  clf 
  hold on
% Rows and columns wright order for terminal output
% but in the wrong order for graphics output, 
% manipulation necessary 
   ising=flipud(fliplr(rot90(reshape(v,6,6))));
  for ix=1:Lx
    for iy=1:Ly
      if ising(ix,iy)==1
        fill(ix+xcoord,iy+ycoord,'k')  
      else
        fill(ix+xcoord,iy+ycoord,'w')  
      end  
    end 
  end
  title(['isweep=' num2str(isweep)])
  axis image
  drawnow
end



return