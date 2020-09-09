clear all; close all; clc
load('scene4.mat')

a = 1;
b = -1;

for i = 1:6
    x = (b-a).*rand(4101,4) + a;
    signal{i,2} = x; 
end

save('scene4.mat')