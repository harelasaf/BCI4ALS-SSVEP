%% SSVEP Offline Main Script
% This script runs all the 5 steps in order. 


%% Run stimulation and record EEG data
% recordingFolder = SSVEP1_Training_Scaffolding();
% disp('Finished stimulation and EEG recording. Stop the LabRecorder and press any key to continue...');
% pause;

%% Run pre-processing pipeline on recorded data
SSVEP2_Preprocess_Scaffolding(recordingFolder);
disp('Finished pre-processing pipeline. Press any key to continue...');
pause;

%% Segment data by trials
SSVEP3_SegmentData_Scaffolding(recordingFolder);
disp('Finished segmenting the data. Press any key to continue...');
pause;

%% Extract features and labels
SSVEP4_ExtractFeatures_Scaffolding(recordingFolder);
disp('Finished extracting features and labels. Press any key to continue...');
pause;

%% Train a model using features and labels
SSVEP5_LearnModel_Scaffolding(recordingFolder);
disp('Finished training the model. The offline process is done!');


