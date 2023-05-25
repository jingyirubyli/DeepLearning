clear all
format compact
format short

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% don't expect the same requence of random numbers as 
% for the python programs
      
nexpo=5
for iexpo=1:nexpo
  ntimes=10^iexpo;
  randvec=rand(ntimes,1);
  mean_vec(iexpo)=mean(randvec);
  var_vec(iexpo)=var(randvec);
  ntimes_vec(iexpo)=ntimes;
end
format long
average_diff=abs(mean_vec-.5)
variance_diff=abs(var_vec-(1/12))

subplot(2,1,1)
loglog(ntimes_vec,average_diff,'+-','Linewidth',2,'Markersize',16)
xlabel('# MC sweeps')
ylabel('Deviation theoretical average')
title('MC Error bars')
set(gca,'Fontsize',16)

subplot(2,1,2)
loglog(ntimes_vec,average_diff,'+-','Linewidth',2,'Markersize',16)
xlabel('# MC sweeps')
ylabel('Deviation theoretical variance')
title('MC Error bars')
set(gca,'Fontsize',16)

return




