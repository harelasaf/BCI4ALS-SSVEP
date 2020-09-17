function [binarySteady] = binaryStimInit(refreshRate,dynRange,stimTime,figureFlag)
%% This function creats 3 vectors containing a binary sequence of sine waves 
% dynRange - which frequencies to create 
% refreshRate - refresh rate for the monitor
% stimTime - overall time of binary sequence
% figureFlag - would you like to show the output waves?


%% Default visualization to zero
if nargin<4
    figureFlag = 0;
elseif nargin<3
    disp('Missing time variable (or function input order is messed up...)');
    return
end

% Initialize variables
dt = 1/refreshRate;
time  = 0:dt:stimTime;                 % overall stim time
binarySteady = [];

%% Create sine wave
for freq = 1:length(dynRange) 
    binarySteady(freq,:) = real(exp( 1i*2*pi*dynRange(freq).*time ));  
end

%% Change to binary signal (0 & 1) for total dark and total white
binarySteady(binarySteady>0) = 1;
binarySteady(binarySteady<0) = 0;

%% Visualization for debugging
if figureFlag
    figure;
    fftPSD(binarySteady(1,:),refreshRate,1) 
    figure;
    plot(1:length(binarySteady),binarySteady);
end
