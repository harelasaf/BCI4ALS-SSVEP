function SSVEP3_SegmentData_Scaffolding(recordingFolder)
%% Segment data using markers
% This function creates a matrix ready for classifier training.


Fs = 125;               % openBCI sample rate
trialLength = 5;        % needs to be equal to offline trainig parameters
load(strcat(recordingFolder,'cleaned_sub.mat'));                % load the filtered EEG data in .mat format
load(strcat(recordingFolder,'trainingVec.mat'));                % load the training vector (which target at which trial)
load(strcat(recordingFolder,'conditionFreq.mat'));              % load the conditio frequency vector (which frequencies are used)
load(strcat(recordingFolder,'sessionFreqs.mat'));               % load the session frequency vector (which frequency is looked at in each trial)
load(strcat(recordingFolder,'EEG_chans.mat'));                  % load the EEG channel locations
numChans = length(EEG_chans);                                   % how many chans do we have?
load(strcat(recordingFolder,'EEG_events.mat'));                  % load the EEG event markers
numConditions = max(conditionFreq);                             % compute how many different conditions in the trials
trials1 = length(trainingVec);                                  % derive number of trials from training label vector
events = struct('type', {EEG_event(1:end).type});
for i = 1:length(events)
    if strcmp('1111.000000000000',events(i).type)   % find trial start marker
        marker1Index(i) = 1;                        % index markers
    else
        marker1Index(i) = 0;
    end
end
mark1Index = find(marker1Index);                    % index of each trial start
trials = length(mark1Index);                           % derive number of trials from start markers

% Check for consistancy across events & trials
if trials ~= trials1
    disp('!!!! Some form of mis-match between number of recorded and planned trials.')
    return
end
SSVEPData = [];                                     % initialize main matrix
% segment data using markers to conditions (1/2/3/4/...) into trialLength segments
for trial = 1:trials
    [SSVEPData] = sortElectrodes(SSVEPData,EEG_data,EEG_event,Fs,trialLength,mark1Index(trial),numChans,trial);
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Segment trials into smaller epochs %%%%%
%%%%%%%   for efficient model training.    %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

save(strcat(recordingFolder,'SSVEPData.mat'),'SSVEPData');
end
