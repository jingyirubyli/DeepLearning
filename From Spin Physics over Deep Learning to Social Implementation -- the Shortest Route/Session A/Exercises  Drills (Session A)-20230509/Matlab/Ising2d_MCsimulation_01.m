clear all
format compact
format short
% Simulate an Lx x Ly Ising spin system 
%  at a given inverse temperature  
% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42)  % uncomment to use different random numbers every time
% all this could be much more obtimized:
% - Not using random updates, but checkerboard updates (alternating
%   Trials of "white" and "black" squares
% - N computing the exponential every time but using a lookup table
%   for the 5 possible values, and not using a random number
%   for lower energies anyway ....

Lx=10
Ly=10
J=1

max_mcs_discard = 10000
max_mcs = 50000

kbT = 3.0 % ferromagnetic if kbt < 2.2692..., paramagnetic if kbt > 2.2692...
% Initial configuration: Random, because the initial temperature 
%  T>2.2692
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

% MC-Loop 
imeas=0;
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
    imeas=imeas+1
     
    M_total=0;
% 1.1 Computation of the average magnetization per spin
    for ix=1:Lx
      for iy=1:Ly
        M_total=M_total+ising(ix,iy); 
      end
    end
    m=M_total/(Lx*Ly);
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
        E_total=E_total+J*DeltaE;
      end
    end
    ener=E_total/(Lx*Ly);   
% 2.2 Save the energy value in a vector for later averaging    
    Evec(imeas)=ener;
  end
end
mean(Mvec)
mean(Evec)


return



