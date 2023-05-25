clear all
format compact
format short
npoints=5000
hmax=20000
p0=1013.25
M =0.0289644 % kg/mol
R=8.3144598 % J/(mol·K)
T=290 % K
g=9.81;
h=linspace(0,hmax,hmax);
p=p0*exp(-M*g/(R*T)*h);
figure(1)
clf
subplot(1,3,1)
n=0
while n<npoints
  htest=hmax*rand;
  xtest=rand;
  p=exp(-M*g/(R*T)*htest);
%  p=1-exp(-M*g/(R*T)*htest);
  if (rand<p)
    n=n+1;
    hvec(n)=htest;
    xvec(n)=xtest;
  end
end  
plot(xvec,hvec,'.','Markersize',4)
xlabel('Distribution')
 subplot(1,3,2)
    [pn,xbin]=hist(hvec,[0:25:hmax]);
    stairs(pn,xbin)
      xlabel('Relative frequency')

  subplot(1,3,3)
  hvecp=[0:hmax]
  pvec=p0*exp(-M*g/(R*T)*hvecp);
  plot(pvec,hvecp)
  xlabel('Atmospheric pressure')
%  print -depsc ThreePlotsDistFreqPre.eps
%return
clf 
%mcsteps=npoints*10
mcsteps=npoints*10%.01
trials=0
accept=0
tried=0;
for imcsteps=1:mcsteps/50
  imcsteps
  for innermc=1:5000  
    iselect=round(npoints*rand+0.5);
    trials=trials+1;
    h_old=hvec(iselect);
%    deltah=100*(rand-.5);
    deltah=100*(rand-.5);
    htest=h_old+deltah;
%    htest=hmax*rand
    p=exp(-M*g/(R*T)*(htest-hvec(iselect)));
    tried=tried+1;
    htestvec(tried)=htest;
    if rand < p
      accept=accept+1;
      hvec(iselect)=htest;
      xvec(iselect)=rand;
    end
  end
  clf
  subplot(1,2,1)
  plot(xvec,hvec,'.','Markersize',4)
  axis([0 1 0 hmax])
  yticks([0:5000:20000])
  yticklabels(['    0'
               ' 5000'
               '10000'
               '15000' 
               '20000'])
  ylabel('h [m]')

    subplot(1,2,2)
    hold on
    plot(pvec,hvecp)
% This histogram is rubbish in the first and last bin.
% which have only half of the entries:
    [pn,xbin]=hist(hvec,[0:250:hmax]);
% This is the better normalization    
    stairs(pn*max(pvec)/(0.5*(pn(2)+pn(3))),xbin)
    legend(' Atmospheric \newline pressure',' Relative \newline frequency')
    legend box off
    yticklabels([])
    axis([0 1200 0 hmax ])
    drawnow
end
acceptance_rate=accept/trials

figure(2)
subplot(4,1,1)
 stem(htestvec,1+0*htestvec,'Linewidth',0.01)
   yticks([])
   xticks([0:5000:20000])
  xticklabels(['    0'
               ' 5000'
               '10000'
               '15000' 
               '20000'])

print -depsc tried_states_imp_samp.eps 
return 
