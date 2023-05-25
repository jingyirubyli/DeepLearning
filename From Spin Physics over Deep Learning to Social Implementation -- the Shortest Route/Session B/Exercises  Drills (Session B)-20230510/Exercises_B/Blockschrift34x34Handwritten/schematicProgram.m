


posx % Position array of the gridpoints
posy %

to_remove=zeros(size(posx)); % 1: remove, 0: don't remove

nadd=0
minimaldistance=0.????
for igridpoints=1:length(posx)
  for jgridpoints=igridpoints+1:length(posx)
     dist=norm([posx(igridpoints)-posx(jgridpoints) ...
                posy(igridpoints)-posy(jgridpoints)]) 
     if dist<=minimaldistance   % relative distance???
        to_remove(igridpoints)=1;
        to_remove(jgridpoints)=1;
        nadd=nadd+1
        posxadd(nadd)=0.5*(posx(igridpoints)+posx(jgridpoints))
        posyadd(nadd)=0.5*(posy(igridpoints)+posy(jgridpoints))
     end
  end
end
    
posx=posx(~to_remove);
posy=posy(~to_remove);
posx=[posx psxadd];
posy=[posy psyadd];


