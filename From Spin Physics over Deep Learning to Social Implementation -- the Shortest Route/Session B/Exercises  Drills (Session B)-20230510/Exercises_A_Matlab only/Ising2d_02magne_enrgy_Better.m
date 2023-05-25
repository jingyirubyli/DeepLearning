clear all
format compact
format short
% Set up Ising spin randomly or ordered
% Compute the physical observables 
% - Total magnetization 
%   M_total=∑_i si 
% - Average magnetization per spin `m`: [-1, 1]
%    m = M_total / (Lx*Ly) = ∑_i si / (Lx*Ly)
% - Average energy ener per spin 2>=ener>=-1
%    ener = E_total / (L^2) = -J∑_<i,j> si*sj / (L^2), (J = 1).
%    for nearest-neighbor interaction  <i,j>
%    and periodic boundary conditions: 
%    - leftmost spin interacts with rightmost spin in the same row, 
%    - nethermost spin interact with uppermost spin in the same column
%
% All these observable computations have  complexity O(L=Lx*Ly) 
% 
% REVISION HISTORY:"Better version" with neighborhood tables and without
% redundant summations in the energy

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% ^^^^^^ uncomment if you want different random numbers 
% every time

Lx=10
Ly=10
J=1

 ordered=0
%ordered=1

if ordered==1
  ising=ones(Lx,Ly);
elseif ordered==0
  ising=round(rand(Lx,Ly))*2-1;
else
  error('This option does not exist')
end

M_total=0;
E_total=0;

% 1. Computation of the average magnetization per spin
for ix=1:Lx
  for iy=1:Ly
    M_total=M_total+ising(ix,iy); 
  end
end
m=M_total/(Lx*Ly)



% 2. Computation of the average energy per spin
% 2.1 First set up neighborhood tables:
for ix=1:Lx-1
  ixright(ix)=ix+1;
end
ixright(Lx)=1;

for iy=1:Ly-1
  iyup(iy)=iy+1;
end
iyup(Ly)=1;

% 2.2 Then sum the energy over every second interaction,
%     i.e. the energies to the right and upward
for ix=1:Lx
  for iy=1:Ly
% Energy contribution for spin (ix,iy) from all four
% nearest neighbors
    DeltaE=-J*ising(ix,iy)*ising(ixright(ix),iy)...  
           -J*ising(ix,iy)*ising(ix,iyup(ix)); 
    E_total=E_total+J*DeltaE;
  end
end
ener=E_total/(Lx*Ly)

% Comments:
% 1. In principle, it would be sufficient to sum the energy only over
%    every second spin, because the interaction energy is symmetric
%    from one spin i to anothe spin j
%    The double-counding makes a division /(2Lx*Ly) instead of  /(Lx*Ly)
%    necessary.
%    In that case, two different loops for the computation of the
%    magnetization (which has to be computed over all sites) are necessary.
% 2. The Python-programs use a neighborhood-table where for every
%    ix  the right neighbor and for every iy the upper neighbor is computed


return

