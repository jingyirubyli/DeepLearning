
lx=nquad2
ly=nquad1
dline=1
inputpattern=zeros(lx,ly)
figure(7)
clf
hold on
for iy=1:ly
  plot([0 lx],[iy iy],'k-')
end
for ix=1:lx
  plot([ix ix],[0 ly],'k-')
end
%plot([0 lx],ly-[27 27],'k-','Linewidth',2)
plot([0 lx],round(ly/2)+[0 0],'k-','Linewidth',2)
plot(round(lx/2)+[0 0],[0 ly],'k-','Linewidth',2)
axis image
axis([0 lx 0 ly])
[xyinput]=ginput
xdat=xyinput(:,1);
ydat=xyinput(:,2);


plot(xdat,ydat,'x-')
    
    
for i_dat=1:length(xdat)-1
  i_dat
%  Dx=[floor(xdat(i_dat)):ceil(xdat(i_dat+1))] 
%  yval=[floor(ydat(i_dat)):ceil(ydat(i_dat+1))] 
    Dys=ydat(i_dat+1)-ydat(i_dat);
    Dxs=xdat(i_dat+1)-xdat(i_dat);
    Dy=abs(Dys);
    Dx=abs(Dxs);
    if (Dx<=1)&(Dy<=1) % input single dots
      xval1=floor(xdat(i_dat));
      yval1=floor(ydat(i_dat));
      fill([0 1 1 0 0]-.5+xval1,...
           [0 0 1 1 0]-.5+yval1,'b')  
      xval2=ceil(xdat(i_dat));
      yval2=floor(ydat(i_dat));
      fill([0 1 1 0 0]-.5+xval2,...
           [0 0 1 1 0]-.5+yval2,'b')  
      xval3=floor(xdat(i_dat));
      yval3=ceil(ydat(i_dat));
      fill([0 1 1 0 0]-.5+xval3,...
           [0 0 1 1 0]-.5+yval3,'b')  
      xval4=ceil(xdat(i_dat));
      yval4=ceil(ydat(i_dat));
      fill([0 1 1 0 0]-.5+xval4,...
           [0 0 1 1 0]-.5+yval4,'b')  
       inputpattern(yval1,xval1)=1;
       inputpattern(yval2,xval2)=1;
       inputpattern(yval3,xval3)=1;
       inputpattern(yval4,xval4)=1;
       xval1=floor(xdat(i_dat));
      yval1=floor(ydat(i_dat));
      fill([0 1 1 0 0]-.85+xval1,...
           [0 0 1 1 0]-.85+yval1,'b')  
      xval2=ceil(xdat(i_dat));
      yval2=floor(ydat(i_dat));
      fill([0 1 1 0 0]-.85+xval2,...
           [0 0 1 1 0]-.85+yval2,'b')  
      xval3=floor(xdat(i_dat));
      yval3=ceil(ydat(i_dat));
      fill([0 1 1 0 0]-.85+xval3,...
           [0 0 1 1 0]-.85+yval3,'b')  
      xval4=ceil(xdat(i_dat));
      yval4=ceil(ydat(i_dat));
      fill([0 1 1 0 0]-.85+xval4,...
           [0 0 1 1 0]-.85+yval4,'b')  
       inputpattern(yval1,xval1)=1;
       inputpattern(yval2,xval2)=1;
       inputpattern(yval3,xval3)=1;
       inputpattern(yval4,xval4)=1;
   elseif (Dx>=Dy)
      if xdat(i_dat+1)>xdat(i_dat)
        Xplot=round(xdat(i_dat)-.5:1:xdat(i_dat+1)+.5);
        dy=Dys/Dxs;
        Yplot=(ydat(i_dat)+dy*[0:length(Xplot)]);
        if (length(Xplot)<length(Yplot))
          Yplot=Yplot(1:length(Xplot));
        else
          Xplot=Xplot(1:length(Yplot));
        end
%        Xplot=round([Xplot Xplot    Xplot      Xplot      Xplot  ]);
%        Yplot=round([Yplot Yplot-.5  Yplot+.5  Yplot-dline  Yplot+dline]);
        Xplot=round([Xplot Xplot    Xplot      Xplot      Xplot  ]);
        Yplot=round([Yplot Yplot-dline  Yplot+dline  Yplot-2*dline  Yplot+2*dline]);
        for iplot=1:length(Xplot)
           fill([0 1 1 0 0]-.5+Xplot(iplot),...
                [0 0 1 1 0]-.5+Yplot(iplot),'k') 
           if (Xplot(iplot)>0)&(Yplot(iplot)>0);
            inputpattern(Yplot(iplot),Xplot(iplot))=1;
          end
        end
%        plot(Xplot(1:end/2),Yplot(1:end/2),'o') 
%        plot(Xplot(end/2+1:end),Yplot(end/2+1:end),'x')
      else
        Xplot=round([xdat(i_dat)+.5:-1:xdat(i_dat+1)-.5]);
        dy=1*Dys/Dxs
        Yplot=(ydat(i_dat)-dy*[0:length(Xplot)]);  
        if (length(Xplot)<length(Yplot))
          Yplot=Yplot(1:length(Xplot));
        else
          Xplot=Xplot(1:length(Yplot));
        end
%        Xplot=round([Xplot Xplot Xplot  Xplot Xplot]);
%        Yplot=round([Yplot Yplot+.5  Yplot-.5  Yplot+dline  Yplot-dline]);
        Xplot=round([Xplot Xplot Xplot  Xplot Xplot]);
        Yplot=round([Yplot Yplot+dline  Yplot-dline  Yplot+2*dline  Yplot-2*dline]);
        for iplot=1:length(Xplot)
          fill([0 1 1 0 0]-.5+Xplot(iplot),...
               [0 0 1 1 0]-.5+Yplot(iplot),'y') 
          if (Xplot(iplot)>0)&(Yplot(iplot)>0);
            inputpattern(Yplot(iplot),Xplot(iplot))=1;
          end
        end
%        plot(Xplot(1:end/2),Yplot(1:end/2),'o') 
%        plot(Xplot(end/2+1:end),Yplot(end/2+1:end),'x') 
      end
     elseif (Dx<=Dy)
      if ydat(i_dat+1)>ydat(i_dat)
        dx=Dxs/Dys;
        Yplot=(ydat(i_dat)-.5:1:ydat(i_dat+1)+.5)
        Xplot=(xdat(i_dat)+dx*[0:length(Yplot)])
        if (length(Xplot)<length(Yplot))
          Yplot=Yplot(1:length(Xplot));
        else
          Xplot=Xplot(1:length(Yplot));
        end
%        Xplot=round([Xplot Xplot-.5 Xplot+.5  Xplot-dline Xplot+dline])
%        Yplot=round([Yplot Yplot   Yplot  Yplot   Yplot])
        Xplot=round([Xplot Xplot-dline Xplot+dline  Xplot-2*dline Xplot+2*dline])
        Yplot=round([Yplot Yplot       Yplot        Yplot         Yplot])
        for iplot=1:length(Yplot)
          fill([0 1 1 0 0]-.5+Xplot(iplot),...
               [0 0 1 1 0]-.5+Yplot(iplot),'b') 
          if (Xplot(iplot)>0)&(Yplot(iplot)>0);
            inputpattern(Yplot(iplot),Xplot(iplot))=1;
          end
        end
%        plot(Xplot(1:end/2),Yplot(1:end/2),'o') 
%        plot(Xplot(end/2+1:end),Yplot(end/2+1:end),'x')
      else
        dx=1*Dxs/Dys;
        Yplot=[ydat(i_dat)+.5:-1:ydat(i_dat+1)-.5];
        Xplot=xdat(i_dat)-dx*[0:length(Yplot)];
        if (length(Xplot)<length(Yplot))
          Yplot=Yplot(1:length(Xplot));
        else
          Xplot=Xplot(1:length(Yplot));
        end
%        Xplot=round([Xplot Xplot+.5 Xplot-.5  Xplot+dline Xplot-dline]);
%        Yplot=round([Yplot Yplot  Yplot  Yplot  Yplot]);
        Xplot=round([Xplot Xplot+dline Xplot-dline  Xplot+2*dline Xplot-2*dline]);
        Yplot=round([Yplot Yplot  Yplot  Yplot  Yplot]);
        for iplot=1:length(Yplot)
          fill([0 1 1 0 0]-.5+Xplot(iplot),...
               [0 0 1 1 0]-.5+Yplot(iplot),'g') 
          if (Xplot(iplot)>0)&(Yplot(iplot)>0);
            inputpattern(Yplot(iplot),Xplot(iplot))=1;
          end
        end
%        plot(Xplot(1:end/2),Yplot(1:end/2),'o') 
%        plot(Xplot(end/2+1:end),Yplot(end/2+1:end),'x')
      end
    else
      error('One case overlooked')  
    end    
   
   
end    
alpha(0.2)
axis image
axis([0 lx 0 ly])
grid

%figure(2)
%clf

inputpattern=flipud(inputpattern)
spy(inputpattern)
%inputpattern=inputpattern(1:lx,)

disp("Don't forget cutoff outside window")
inputpattern=inputpattern(1:nquad1,1:nquad2)
inputpat=inputpattern*2-1;



