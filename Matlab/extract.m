clear all;close all;clc
load scene1.mat
%load All_angle_crack_signals.mat

sensor = 2; crack_cond = 6; noisy = 64; L = 3901;

for j = 1:noisy
    SNR = (15-5).*rand(1,1) + 45;
    
    for i = 1:crack_cond
        start = randi([200 4101-L]);
        data(j+(i-1).*noisy,:) = awgn(signal{i,2}(start:(start+L-1),sensor),SNR);
    end
    
end

for j = 1:noisy
    for i = 1:crack_cond
        label(j+(i-1).*noisy,:) = i-1;
    end
end

[idx,C] = kmeans(data,6);
L = [idx label];
plot(L)
%csvwrite('data.csv',data)

%for j = 1:noisy
%    for i = 1:crack_cond
%        label(j+(i-1).*noisy,:) = i-1;
%    end
%end

%csvwrite('label.csv',label)
