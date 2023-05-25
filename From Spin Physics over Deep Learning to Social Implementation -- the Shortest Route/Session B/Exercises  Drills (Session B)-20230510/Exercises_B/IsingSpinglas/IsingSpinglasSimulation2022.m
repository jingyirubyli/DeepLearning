clear all 
format compact
format short
% random flipping
% Main Loop
lx=8
ly=8
nsweep=40000 % 10000*16*16 
ntherm=20000  % number of sweeps
             % where I start measuring

nrepeat=lx%lx
nvis=nsweep
Temp=[5:-0.01:.1]
% Random initialization T=infinity
is=round(rand(lx,ly))*2-1
% Set up interaction

J=zeros(lx,ly,lx,ly);

for ix=1:lx
  for iy=1:ly 
      if ix+1>lx
        ixp1=1;  % Period. bound
      else
        ixp1=ix+1; % neighbor to the right
      end
      Jnow=2*round(rand)-1;
      J(ix,iy,ixp1,iy)=Jnow;
      J(ixp1,iy,ix,iy)=Jnow;
      
%       if ix-1==0
%         ixm1=lx;
%       else
%         ixm1=ix-1;
%       end
%       Jnow=2*round(rand)-1;
%       J(ix,iy,ixm1,iy)=Jnow;
%       J(ixm1,iy,ix,iy)=Jnow;
      
      if iy+1>ly
        iyp1=1;
      else
        iyp1=iy+1;
      end
      Jnow=2*round(rand)-1;
      J(ix,iy,ix,iyp1)=Jnow;
      J(ix,iyp1,ix,iy)=Jnow;
      
%       if iy-1==0
%         iym1=ly;
%       else
%         iym1=iy-1;
%       end
%       Jnow=2*round(rand)-1;
%       J(ix,iy,ix,iym1)=Jnow;
%       J(ix,iym1,ix,iy)=Jnow;
  end
end


% Temperature Loop
for itemp=1:length(Temp)
  T=Temp(itemp)
  for isweep=1:nsweep
    for il=1:lx*ly
      for irepeat=1:nrepeat
      ix=round(rand*lx+.5);
      iy=round(rand*ly+.5);
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
      Eold=-is(ix,iy)*...
      (J(ix,iy,ix,iyp1)*is(ix,iyp1)+...
       J(ix,iy,ix,iym1)*is(ix,iym1)+...
	   J(ix,iy,ixp1,iy)*is(ixp1,iy)+...
       J(ix,iy,ixm1,iy)*is(ixm1,iy));
      Enew=-Eold;
      DeltaE=Enew-Eold;
      p=exp(-DeltaE/T);
      if p>rand
        is(ix,iy)=-is(ix,iy);
      end
      end
    end
% Visualization	
%     if (nvis*round(isweep/nvis)==isweep)
%       figure(1)
%       clf
%       hold on
%       xrel=[-.5 .5 .5 -.5];
%       yrel=[-.5 -.5 .5 .5];
%       for ix=1:lx
%         for iy=1:ly
%           if (is(ix,iy)==1)
%             fill(ix+xrel,iy+yrel,'w')
%           else
%             fill(ix+xrel,iy+yrel,'k')
%           end
%           axis image
%           axis([0 lx+1 0 ly+1])
%         end
%       end 
%       title(['T=' num2str(T)])
%       drawnow
%     end   
% Computation of averages
% after a single sweep	
    if isweep>ntherm
      m(isweep-ntherm)=(mean(is(:)));
      m2(isweep-ntherm)=mean(is(:)).^2;
      Ecurr=compute_EnergySpinglas(is,J);
      E(isweep-ntherm)=Ecurr;
    end
  end
% Averages at each temperature 
  Maver(itemp)=mean(m);
  M2aver(itemp)=mean((m-mean(m)).^2)/T;
  Eaver(itemp)=mean(E); 
  Xi(itemp)=var(m)/T;
  C(itemp)=var(E)/T^2;
end
% Output of the temperature-
% dependent averages
figure(2)
subplot(4,1,1)
plot(Temp,abs(Maver),'*-')
axis tight
title('aver Magnetization  per site')
subplot(4,1,2)
plot(Temp,Xi,'*-')
axis tight
title('Susceptibility')
subplot(4,1,3)
plot(Temp,Eaver,'*-')
axis tight
title('Average Energy per site')
subplot(4,1,4)
plot(Temp,C,'*-')
axis tight
title('Heat capacity')
return

