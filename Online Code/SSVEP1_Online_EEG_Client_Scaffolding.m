%% SSVEP Online Scaffolding
% This code creates an online EEG buffer which utilizes the model trained
% offline, and corresponding frequencies, to classify between the possible targets.
% Assuming: 
% 1. EEG is recorded using openBCI and streamed through LSL.
% 2. SSVEP stimulation is handled on another machine (arduino/comp) using training frequencies.
% 3. A different machine is querying through LSL for the commands sent through this code

addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Online Code');
addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Offline Training');
addpath('C:\Toolboxes\labstreaminglayer-master\LSL\liblsl-Matlab\liblsl-Matlab');
addpath('C:\Toolboxes\labstreaminglayer-master\LSL\liblsl-Matlab\liblsl-Matlab\bin');

%% Set params

Fs = 125;                                   % openBCI sample rate
load(strcat(recordingFolder,'features.mat'));

subID = 0; %%%%%%%%%%%%%%% LAHAV %%%%%%%%%%%%%%

% subID = input('Please enter subject ID/Name: ');    % prompt to enter subject ID or name
if getComputerName == 'desktop-6d533n5'
    addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Online Code');
    addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Offline Training');
end

recordingFolder = strcat('C:\Dropbox (BGU)\BCI resources\SSVEP\Recordings\Sub',num2str(subID),'\');
bufferLength = 1;                     % how much data (in seconds) to buffer for each classification
% numVotes = 3;                           % how many votes before classification?
output_rate = 1;                        % desired output decision rate, in Hz
try 
    load(strcat(recordingFolder,'\weightVec.mat'));
    
numTargets = length(conditionFreq);     % set number of possible targets 

%% Lab Streaming Layer Init
disp('Loading the Lab Streaming Layer library...');
lib = lsl_loadlib();

disp('Opening Output Stream...');
info = lsl_streaminfo(lib,'MarkerStream','Markers',1,0,'cf_string','myuniquesourceid23443');
outletStream = lsl_outlet(info);

% resolve a stream...
disp('Resolving an EEG Stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'type','EEG'); 
end
disp('Success resolving!');
% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});

% onl_newstream('mystream', 'srate', 200, 'chanlocs',openBCIchanLocs);
% onl_newpredictor('mypredictor', model);
disp('Now receiving data...');
myBuffer = {};
t = 0;
pause(0.2);
myChunk = inlet.pull_chunk();
myBuffer = [];
time = 0;
while true
    time = time+1;
    % get data from the inlet
    myChunk = inlet.pull_chunk();
    
%     if sum(myChunk(:,1)) ~= 0
    % append it to buffer
    myBuffer = [myBuffer myChunk];
%     else
%         disp('Houston, we have a problem.');
%     end
    
    t = t + 1/Fs;       % perhaps utlize the inner system clock to properly time the input chunks and output estimate?
    
    % If reaches required output rate (t > (1 / output_rate)) || 
    if (size(myBuffer,2)>(bufferLength*Fs))
        block = [myBuffer];
        % Extract features from the buffered block:
        EEG_Features = ExtractPowerBands(block,features,Fs);
%         EEG_Features = bandpower(block',Fs,powerbandFreqs)

        % Predict using previously learned model
        for targ = 1:numTargets
            myPredictions(targ) = weightVec(targ,2:end)*EEG_Features'+weightVec(1); % first weight is the intercept
        end
        [M,myEstimate] = max(myPredictions);
        myEstimate
        myPredictions
        
        % Send estimate to voting machine (apply different approaches)
%         sendVote(myEstimate);
        % Send decision to some feedback mechanism (Car/Drone/Visual) using
        % LSL. If needed, can be interchanged into OSC, UDP, or any other
        % communication scheme.
%         outletStream.push_sample(myEstimate);
        % clear buffer
        myBuffer = [];
        myPredictions = [];
        % clear timer
        t = t - 1/output_rate;
    end
end




