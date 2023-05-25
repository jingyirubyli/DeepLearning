clear all
format compact
format short
% Program to set up ising spings randomly or ordered
% and display them in different ways

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% ^^^^^^ uncomment if you want different random numbers 
% every time

Lx=10
Ly=10

 ordered=0
%ordered=1

if ordered==1
  ising=ones(Lx,Ly);
elseif ordered==0
  ising=round(rand(Lx,Ly))*2-1;
else
  error('This option does not exist')
end
% if the next line is uncommentedthis isdisplays
% format +  
ising 

% set up X- and Y-coordinates
[Xpos,Ypos]=meshgrid(1:Lx,1:Ly);

figure(1)
% Display as arrows
clf
hold on
plot(Xpos,Ypos,'o') % mark the sites
quiver(Xpos,Ypos-.25*ising,0*Xpos,0*Xpos+ising,0.5,'Linewidth',2)
% shift y-position ^^^^^  rescale arrow length^^^^    
axis image

figure(2)
% Display as black-white, which will also be useful for 
% displaying results for pattern recognition
clf
hold on
xcoord=[0 1 1 0 0]+.5;
ycoord=[0 0 1 1 0]+.5;
for ix=1:Lx
  for iy=1:Ly
    if ising(ix,iy)==1
      fill(ix+xcoord,iy+ycoord,'k')  
    else
      fill(ix+xcoord,iy+ycoord,'w')  
    end  
  end
end
axis image

return

