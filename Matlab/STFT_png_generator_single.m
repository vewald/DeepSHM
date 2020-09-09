clear all;close all;clc
load scene4.mat

%% 
ylimit=600e3;   % To reduce the unwanted y limit in the data. Currently uning the limit 0KHz to 600KHz
num_noisy=10.*[10,20,70];    % Number of noisy files for each sensor, 70 for training, 20 validation, 10 test
%% 

n = 3; combination = 1; % No of sensors n & combination c
dataset = {'test','validation','training'};
%start = 2; step = 2; final = 6; % Sensor 2, 4, and 6
s = [1,2,3;1,2,4;1,3,4;2,3,4];
%s = [1,2,3;1,5,7;2,4,6;2,6,8;3,6,8;3,5,7;4,5,6;4,6,8];

for C = 1:combination
    for d = 1:length(dataset)
        for crack_cond=1:size(signal,1)
            for noisy_files=1:num_noisy(d)
                
                for Sensor=s(C,1:n)
                    
            SNR = ((15-5).*rand(1,1)+5)./1e2;        % SNR Ratio
            Data = awgn(signal{crack_cond,2}(:,Sensor),SNR, 'measured');   % Adding gaussian noise
            filename = ['Crack_',signal{crack_cond,1},'_Sensor_',num2str(Sensor),'_noisyfile_',num2str(noisy_files),'_',num2str(SNR)]; % Filename to tbe exported
            Addy_transform_STFT_png_gen(Data,time,fs,ylimit,filename);          % Calling the function for calculation and exporting image
            M{Sensor} = imread(filename,'png');
            movefile('*.png',['F:/Simulation/single_scene4/',char(dataset{d}),'/',num2str(crack_cond-1)])
                
                end
            
            filename2 = (['Cr_',signal{crack_cond,1},'_',num2str(noisy_files)]);
            %imwrite(cat(3,M{start:step:final}),[filename2,'.png']);
            imwrite(cat(3,M{s(C,1:n)}),[filename2,'.png']);
            movefile('*.png',['F:/Simulation/single_scene4/combi_',num2str(C),'/rgb/',char(dataset{d}),'/',num2str(crack_cond-1)])

            end
            
        end
    end
end