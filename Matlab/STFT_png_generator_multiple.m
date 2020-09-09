clear all;close all;clc
load scene4.mat
%load All_angle_crack_signals.mat

%% 
ylimit = 600e3;   % To reduce the unwanted y limit in the data. Currently uning the limit 0KHz to 600KHz
num_noisy = 1.*[10,20,70];   % Number of noisy files for each sensor, 70 for training, 20 validation, 10 test
%% 

n = 4; % No of sensors
%dataset = {'validation','training'};
dataset = {'test','validation','training'};
idx = size(dataset); window_size = 3200;%[100,150,200,250,300,400,500,600,800,1000,1200,1600,2000,3200];

%% looping through each sensor for each crack condition
for Sensor = 1:n % Sensor
    for crack_cond=6%1:size(signal,1)  % crack condition
        for d = 1:idx(2)
            for noisy_files=1:num_noisy(d)     % for given number of noisy pictures to be produced for each sensor
                for j = 1:length(window_size)
                    for L = window_size(j)
                
            SNR = ((15-5).*rand(1,1) + 5)./10;      % SNR Ratio
            start = randi([200 4101-L]);
            Data = awgn(signal{crack_cond,2}((start:(start+L)),Sensor),SNR, 'measured');   % Adding gaussian noise
            filename = ['Crack_',signal{crack_cond,1},'_Sensor_',num2str(Sensor),'_noisyfile_',num2str(noisy_files)]; % Filename to tbe exported
            Addy_transform_STFT_png_gen(Data,time,fs,ylimit,filename);          % Calling the function for calculation and exporting image
            movefile('*.png',['F:/Simulation/multiple_scene4/',num2str(L),'/sensor',num2str(Sensor),'/',char(dataset{d}),'/',num2str(crack_cond-1)])

                    end                    
                end
            end
        end
    end
end