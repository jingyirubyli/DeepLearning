function Ene_sum = compute_EnergySpinglas(is,J)
% COMPUTE_ENERGY of a spinglas with NN-Interactions
%   for a system lx x ly ising spins and Hamiltonian
%   -J sum si_sj
% Error in the sign  HG  06-Sep-2022
% magic numbers 17 and 16 fixed
Ene_sum=0;
[lx,ly]=size(is);

for ix=1:lx
    for iy=1:ly
      ixp1=ix+1;  % neighbor to the right
      if ixp1>lx   % periodic bound.
        ixp1=1;
      end
      ixm1=ix-1;  % neighbor to the left
      if ixm1<1   % periodic bound.
        ixm1=lx;
      end
      iyp1=iy+1;   % neighbor above
      if iyp1>ly   % periodic bound.
        iyp1=1;
      end
      iym1=iy-1;  % neighbor below
      if iym1<1   % periodic bound.
        iym1=ly;
      end
       Eadd=-is(ix,iy)*...
      (J(ix,iy,ix,iyp1)*is(ix,iyp1)+...
       J(ix,iy,ix,iym1)*is(ix,iym1)+...
	   J(ix,iy,ixp1,iy)*is(ixp1,iy)+...
       J(ix,iy,ixm1,iy)*is(ixm1,iy))/2;
       Ene_sum=Ene_sum+Eadd;
    end
end
Ene_sum=Ene_sum/(lx*ly);


end

