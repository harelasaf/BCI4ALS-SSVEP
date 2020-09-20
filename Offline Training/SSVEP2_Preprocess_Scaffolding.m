function [] = SSVEP2_Preprocess_Scaffolding(recordingFolder)
%% Offline Preprocessing
% dataFolder - where the EEG (data & meta-data) are stored.
% Assumes openBCI 
% EEGLAB installed with ERPLAB & loadXDF plugins istalled

% Preprocessing using EEGLAB function. Assumes Wearable Sensing DSI-24 EEG
% 1. load XDF file (Lab Recorder LSL output)
% 2. look up channel names - each group on their own
% 3. remove redundant channels - not necessary for openBCI
% 4. re-reference to mastoid (or other) reference channel - done ANALOG by openBCI hardware
% 5. filter data above 0.5 & below 40 Hz
% 6. notch filter @ 50 Hz
% 7. advanced artifact removal (ICA/ASR/Cleanline...) - EEGLAB functionality
clc
addpath 'C:\Toolboxes\eeglab2019_1'
eeglab;
% Parameters
subjects = 1;
sessions = 1;
% fileName = input('Please enter XDF filename (case sensitive): ');    % prompt to enter XDF filename
recordingFile = strcat(recordingFolder,'EEG.XDF');
% load subject data (assume XDF)
EEG = pop_loadxdf(recordingFile, 'streamtype', 'EEG', 'exclude_markerstreams', {});
EEG.setname = 'SSVEP_sub';
% update channel names - each group should update this according to
% their own openBCI setup.
EEG = pop_select( EEG, 'nochannel',1);  % remove time stamp

EEG_chans(1,:) = 'Fp1';
EEG_chans(2,:) = 'Fp2';
EEG_chans(3,:) = 'C03';
EEG_chans(4,:) = 'C04';
EEG_chans(5,:) = 'P07';
EEG_chans(6,:) = 'P08';
EEG_chans(7,:) = 'O01';
EEG_chans(8,:) = 'O02';
EEG_chans(9,:) = 'F07';
EEG_chans(10,:) = 'F08';
EEG_chans(11,:) = 'F03';
EEG_chans(12,:) = 'F04';
EEG_chans(13,:) = 'T07';
EEG_chans(14,:) = 'T08';
EEG_chans(15,:) = 'P03';
EEG_chans(16,:) = 'P04';
% ...

% low-pass filter
EEG = pop_eegfiltnew(EEG, 'hicutoff',40,'plotfreqz',1);
EEG = eeg_checkset( EEG );
% high-pass filter
EEG = pop_eegfiltnew(EEG, 'locutoff',0.5,'plotfreqz',1);
EEG = eeg_checkset( EEG );
% notch filter - this uses the ERPLAB filter
EEG  = pop_basicfilter( EEG,  1:16 , 'Boundary', 'boundary', 'Cutoff',  50, 'Design', 'notch', 'Filter', 'PMnotch', 'Order',  180 );
EEG = eeg_checkset( EEG );

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Add advanced artifact removal %%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Save the data into .mat variables on the computer
EEG_data = EEG.data;
EEG_event = EEG.event;
save(strcat(recordingFolder,'cleaned_sub.mat'),'EEG_data');
save(strcat(recordingFolder,'EEG_events.mat'),'EEG_event');
save(strcat(recordingFolder,'EEG_chans.mat'),'EEG_chans');
                
end
