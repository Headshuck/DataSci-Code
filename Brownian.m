% Velocity must be function of bordersize. I wasn't able to do that here.
% Particles move eratically at smaller bordersizes as a result. Also,
% couldn't figure out path tracing(for a few particles). To trace all paths
% one must simply add a 'hold on' command. No collision detection either. 

X = 100 % rectangular border 
n = 50 % number of particles 
part = [1 + (9)*(rand(1,n)) ; 1 + (9)*(rand(1,n))]
j = [ones(1,length(part)) ; ones(1,length(part))]

q = (-1 + (2).*rand(size(part)));
x_velo = j(1,:) 
y_velo = j(2,:)

for i = 1:1000
    plot(part(1,:), part(2,:), 'o');
    part = part + j.*q;
    axis([ -X X -X X]);
    pause(1/72000 )
    
    u = abs(abs(part(1,:)) - X) < .5
    k = abs(abs(part(2,:)) - X) < .5
    
    x_velo(u) = x_velo(u)*-1 
    y_velo(k) = y_velo(k)*-1 
    
    j(1,:) = x_velo 
    j(2,:) = y_velo 
    
    
end 