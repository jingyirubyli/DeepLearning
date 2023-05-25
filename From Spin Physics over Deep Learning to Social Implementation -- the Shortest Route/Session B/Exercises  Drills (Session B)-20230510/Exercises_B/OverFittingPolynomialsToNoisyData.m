clear
format compact
randn('seed',16)

l=24
x=linspace(-3,3,l);
aparabola=[3 2 1];
y=polyval(aparabola,x)
xline=linspace(-3.15,3.15,400);
yline=polyval(aparabola,xline)
% create y-data 1*x^2+2*x+3
randn('seed',5)
ytofit=y+2*randn(size(y));
axis tight
afitted=polyfit(x,ytofit,11)
ylinefitted=polyval(afitted,xline)

subplot(2,2,1)
plot(x,y,'o',x,ytofit,'*',...
    xline,yline,':',...
    xline,ylinefitted,'-','Linewidth',1.5)
axis tight
legend('original data','noisy data',...
    'original parabola','fitted straight line',...
    'location','north')

print -depsc2 incorrect_overfit.eps

return