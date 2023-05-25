clear all
format compact
format short
% Simulate an Lx x Ly Ising spin system 
% with interaction between all spins which
% has a smiley as groundstate 
%  for cooling down from T=3 to T=1.5 in steps of -0.05
% We are not interested in the average values, 
% We are only interested in the result with the lowest interaction

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',12)  % uncomment to use different random numbers every time

Lx=40
Ly=40
J=1

Tmax=3
Tmin=.001
Nstep=150
% Linear cooling schedule
%Tcool=linspace(Tmin,Tmax,Nstep);
%Tcool=Tcool(end:-1:1);
% Logarithmic cooling schedule (not as good)
Tcool=logspace(log10(Tmax),log10(Tmin),Nstep)
% not needed for simulated annealing:
% max_mcs_discard = 10000 
max_mcs = 10000


% Create the Interaction
Interaction_conf=J*ones(Lx,Ly);
% Set up the round face outline
for ix=1:Lx
  for iy=1:Ly
    if ( (sqrt((ix-Lx/2)^2+(iy-Ly/2)^2))<(Lx/2-2)  )&...
       ( (sqrt((ix-Lx/2)^2+(iy-Ly/2)^2))>(Lx/2-3.5)  )
       Interaction_conf(ix,iy)=-1;
    end
  end
end

% Set up the round eyes 
for ix=1:Lx
  for iy=1:Ly
    if ( (sqrt((ix-Lx*2/3)^2+(iy-Ly*2/3)^2))<3.5 )
       Interaction_conf(ix,iy)=-1;
    end
    if ( (sqrt((ix-Lx*1/3)^2+(iy-Ly*2/3)^2))<3.5 )
       Interaction_conf(ix,iy)=-1;
    end
  end
end

% Set up the mouth
for ix=1:Lx
  for iy=1:Ly
    if abs(iy-Lx/3)<2 
      if (ix>Lx/3)&(ix<Lx*2/3)
        Interaction_conf(ix,iy)=-1;
      end
    end
  end
end

% set up X- and Y-coordinates for graphics
[Xpos,Ypos]=meshgrid(1:Lx,1:Ly);
xcoord=[0 1 1 0 0]+.5;
ycoord=[0 0 1 1 0]+.5;

figure(1)
clf 
hold on
for ix=1:Lx
  for iy=1:Ly
    if Interaction_conf(ix,iy)==1
      fill(ix+xcoord,iy+ycoord,'k')  
    else
      fill(ix+xcoord,iy+ycoord,'w')  
    end  
  end
end
axis image

% Set up the nearest neighbor 
% spinglas interaction from Interaction_conf  

Jij_ri=zeros(Lx,Ly);
Jij_le=zeros(Lx,Ly);
Jij_up=zeros(Lx,Ly);
Jij_do=zeros(Lx,Ly);

for ix=1:Lx-1
  for iy=1:Ly
    if Interaction_conf(ix,iy)==Interaction_conf(ix+1,iy)
      Jij_ri(ix+1,iy)=1;
    else
      Jij_ri(ix+1,iy)=-1;
    end
  end
end
for ix=2:Lx
  for iy=1:Ly
    if Interaction_conf(ix,iy)==Interaction_conf(ix-1,iy)
      Jij_le(ix-1,iy)=1;
    else
      Jij_le(ix-1,iy)=-1;
    end
  end
end

for ix=1:Lx
  for iy=1:Ly-1
    if Interaction_conf(ix,iy)==Interaction_conf(ix,iy+1)
      Jij_up(ix,iy+1)=1;
    else
      Jij_up(ix,iy+1)=-1;
    end
  end
end
for ix=1:Lx
  for iy=2:Ly
    if Interaction_conf(ix,iy)==Interaction_conf(ix,iy-1)
      Jij_do(ix,iy-1)=1;
    else
      Jij_do(ix,iy-1)=-1;
    end
  end
end


for iy=1:Ly
  if Interaction_conf(Lx,iy)==Interaction_conf(1,iy)
    Jij_ri(Lx,iy)=1;
    Jij_le(1,iy)=1;
  else
    Jij_ri(Lx,iy)=-1;
    Jij_le(1,iy)=-1;
  end  
end
Jij_ri(1,:)=Jij_ri(end,:);
Jij_le(end,:)=Jij_le(1,:);


for ix=1:Lx
  if Interaction_conf(ix,Ly)==Interaction_conf(ix,1)
    Jij_up(ix,Ly)=1;
    Jij_do(ix,1)=1;
  else
    Jij_up(ix,Ly)=-1;
    Jij_do(ix,1)=-1;
  end  
end
Jij_do(:,end)=Jij_do(:,1);
Jij_up(:,1)=Jij_up(:,end);


%error('only up to here')
% All interactions which are not defined
% are set to zero
   

% Start with random configuration
ising=round(rand(Lx,Ly))*2-1;

% Set up neighborhood tables for MC-move computation 
% and energy computation
for ix=1:Lx-1
  ixri(ix)=ix+1;
end
ixri(Lx)=1;
for ix=2:Lx
  ixle(ix)=ix-1;
end
ixle(1)=Lx;

for iy=1:Ly-1
  iyup(iy)=iy+1;
end
iyup(Ly)=1;
for iy=2:Ly
  iydo(iy)=iy-1;
end
iydo(1)=Ly;


itemp=0;
% Temperature loop
for itemp=1:length(Tcool);
kbT=Tcool(itemp)


figure(2)
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
      sumspin=Jij_ri(ixri(ix),iy)*ising(ixri(ix),iy)+...
              Jij_le(ixle(ix),iy)*ising(ixle(ix),iy)+... 
              Jij_up(ix,iyup(iy))*ising(ix,iyup(iy))+...
              Jij_do(ix,iydo(iy))*ising(ix,iydo(ix)); 
          
          
%     Compute energy
      E_old=-ising(ix,iy)*sumspin;
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

  
end
 
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


end

