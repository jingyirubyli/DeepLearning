clear all 
format compact
format short
% random flipping
% Main Loop
lx=8
ly=8
nsweep=60000 % 10000*16*16 
ntherm=20000  % number of sweeps
             % where I start measuring

nrepeat=1%lx
nvis=nsweep
Temp=[10:-0.1:1]
% Random initialization T=infinity
is=round(rand(lx,ly))*2-1
% Set up interaction
isvec=is(:)
clear is

J=randn(lx*ly,lx*ly)
J=triu(J)
J=J+J.'
J=J-diag(diag(J))



% Temperature Loop
for itemp=1:length(Temp)
  T=Temp(itemp)
  for isweep=1:nsweep
    for il=1:lx*ly
      for irepeat=1:nrepeat
      ixy=round(rand*lx*ly+.5);
       
% wrong      Eold=-isvec(ixy)*sum(J*isvec);
      Eold=-isvec(ixy)*J(ixy,:)*isvec;
      Enew=-Eold;
      DeltaE=Enew-Eold;
      p=exp(-DeltaE/T);
      if p>rand
        isvec(ixy)=-isvec(ixy);
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
      m(isweep-ntherm)=(mean(isvec(:)));
      m2(isweep-ntherm)=mean(isvec(:)).^2;
      Ecurr=compute_EnergyinfrangeSpinglas(isvec,J);
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

