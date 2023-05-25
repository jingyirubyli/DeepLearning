clear all
format compact
format short
% Simulate an Lx x Ly Ising spin system 
% with interaction between all spins which
% has a smiley as groundstate 
%  for cooling down from T=3 to T=1.5 in steps of -0.05

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42)  % uncomment to use different random numbers every time

Lx=20
Ly=20
J=1


% Create the Interaction
initialstate=ones(Lx,Ly);
% make the round face
theta_vec=linspace(0,2*pi,4*(Lx+Ly));
for itheta=1:length(theta_vec)
  theta=theta_vec(itheta);
  ix=round(Lx/2+cos(theta)*.9*Lx/2)
  iy=round(Ly/2+sin(theta)*.9*Ly/2)
  initialstate(ix,iy)=-initialstate(ix,iy);
end

format +

initialstate


return
    




max_mcs_discard = 10000
max_mcs = 50000


ising=round(rand(Lx,Ly))*2-1;

% First set up neighborhood tables for MC-move computation 
% and energy computation
for ix=1:Lx-1
  ixright(ix)=ix+1;
end
ixright(Lx)=1;
for ix=2:Lx
  ixleft(ix)=ix-1;
end
ixleft(1)=Lx;

for iy=1:Ly-1
  iyup(iy)=iy+1;
end
iyup(Ly)=1;
for iy=2:Ly
  iydo(iy)=iy-1;
end
iydo(1)=Ly;

Tmax=4
Tmin=1
Tstep=0.1

% set up X- and Y-coordinates for graphics
[Xpos,Ypos]=meshgrid(1:Lx,1:Ly);
xcoord=[0 1 1 0 0]+.5;
ycoord=[0 0 1 1 0]+.5;

M_temp=zeros(size([Tmax:-Tstep:Tmin]));
E_temp=zeros(size([Tmax:-Tstep:Tmin]));
T_temp=zeros(size([Tmax:-Tstep:Tmin]));
itemp=0;
% Temperature loop
for kbT=Tmax:-Tstep:Tmin
kbT    
itemp=itemp+1;

% MC-Loop 
imeas=0;
Mvec=zeros(max_mcs-max_mcs_discard,1);
Evec=zeros(max_mcs-max_mcs_discard,1);
for imc=1:max_mcs
% One MC-sweep: Lx times Ly trials to make a spin change
  for ixsweep=1:Lx
    for iysweep=1:Ly
%     Select spin randomly          
      ix=round(rand*Lx+0.5);
      iy=round(rand*Ly+0.5);  
%     Compute sum over neighboring spins 
      sumspin=ising(ixright(ix),iy)+ising(ixleft(ix),iy)+... 
              ising(ix,iyup(iy))+ising(ix,iydo(ix)); 
%     Compute energy
      E_old=-J*ising(ix,iy)*sumspin;
      E_new=-E_old; % Spinflip reverses the energy
%     Compute Energy change: DeltaE=Enew-Eold
      DeltaE_ixiy=E_new-E_old;
      P=exp(-DeltaE_ixiy/kbT);
      if P>rand
        ising(ix,iy)=-ising(ix,iy);
      end  
    end
  end 
% MC-measurement only if  imc>max_mcs_discard

  if imc>max_mcs_discard
    imeas=imeas+1;
     
    M_total=0;
% 1.1 Computation of the average magnetization per spin
    m=mean(ising(:));
% 1.2 Save the magnetization value in a vector for later averaging    
    Mvec(imeas)=m;
    
% 2.1 Then sum the energy over every second interaction,
%     i.e. the energies to the right and upward to avoid double counting
   E_total=0;
   for ix=1:Lx
     for iy=1:Ly
% Energy contribution for spin (ix,iy) from all four
% nearest neighbors
        DeltaE=-J*ising(ix,iy)*ising(ixright(ix),iy)...  
               -J*ising(ix,iy)*ising(ix,iyup(ix)); 
        E_total=E_total+DeltaE;
      end
    end
    ener=E_total/(Lx*Ly);   
% 2.2 Save the energy value in a vector for later averaging    
    Evec(imeas)=ener;
  end

  
end
  figure(1)
  clf 
  hold on
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
drawnow
% Averages for a given temperature
 T_temp(itemp)=kbT; 
 M_temp(itemp)=mean(Mvec);
 E_temp(itemp)=mean(Evec);


end

figure(2)
subplot(2,1,1)
plot(T_temp,M_temp)
xlabel('Temperature kbT')
ylabel('Magnetization')
subplot(2,1,2)
plot(T_temp,E_temp)
xlabel('Temperature kbT')
ylabel('Energy per site')

return



