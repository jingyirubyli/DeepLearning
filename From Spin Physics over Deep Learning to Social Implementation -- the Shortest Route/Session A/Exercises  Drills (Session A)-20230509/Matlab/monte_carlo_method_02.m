clear all
format compact
format short

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% don't expect the same requence of random numbers as 
% for the python programs
      
nexpo=7
for iexpo=1:nexpo
  ntimes=10^iexpo;
  n_inside=0;
  for itimes=1:ntimes
    x=rand;
    y=rand;
    if (x^2+y^2)<=1
      n_inside=n_inside+1;
    end
  end
  n_circle(iexpo)=n_inside;
  n_total(iexpo)=ntimes;
end

format long
pi_approx=4*n_circle./n_total
deviation_from_pi=abs(pi_approx-pi)
% deviations are usually taken as absolute value 
loglog(n_total,deviation_from_pi,'+-','Linewidth',2,'Markersize',16)
xlabel('# MC sweeps')
ylabel('Deviation from Pi')
title('MC Error bars')
set(gca,'Fontsize',16)



return

