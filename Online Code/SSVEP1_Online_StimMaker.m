function [] = SSVEP1_Online_StimMaker()
%% SSVEP Stimulation Maker for Online BCI
% This code creates a visual SSVEP stimulation with (#) numTargets on screen for
% (#) numTrials. Make sure the frequencies are identical to the training paradigm. 
% This code assumes EEG is recorded and streamed through LSL.

%% For debugging:
recordingFolder = 'C:\Dropbox (BGU)\BCI resources\SSVEP\Recordings\Sub38653655\';

%% Make sure you have Psychtoolbox & Lab Streaming Layer installed.

%% Set parameters:
addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Offline Training');
addpath('C:\Dropbox (BGU)\BCI resources\SSVEP\Generic Code\Online Code');
addpath('C:\Toolboxes\labstreaminglayer-master\LSL\liblsl-Matlab\liblsl-Matlab');
addpath('C:\Toolboxes\labstreaminglayer-master\LSL\liblsl-Matlab\liblsl-Matlab\bin');
load(strcat(recordingFolder,'conditionFreq.mat'));
compName = getComputerName;                         % get the local computer name
if compName == 'desktop-6d533n5'
    rootFolder = 'D:\Dropbox (BGU)';                % define Dropbox folder location
else
    rootFolder = 'C:\Dropbox (BGU)';                % define Dropbox folder location
end

trialLength = 5;                        % each trial length in seconds
numTrials = 30;                         % set number of training trials
numTargets = 4;                         % set number of possible targets 
lowEnd = 7;                             % lower bound of target frequency
highEnd = 24;                           % higher bound of target frequency
freqStep = 1;                           % difference between each neighboring frequency

%% Lab Streaming Layer Init
disp('Loading the Lab Streaming Layer library...');
% Init LSL parameters
lib = lsl_loadlib();                    % load the LSL library
disp('Opening Marker Stream...');
% Define stream parameters
info = lsl_streaminfo(lib,'MarkerStream','Markers',1,0,'cf_string','myuniquesourceid23443');
outletStream = lsl_outlet(info);        % create an outlet stream using the parameters above
disp('Open Lab Recorder & check for MarkerStream and EEG stream, start recording, return here and hit any key to continue.');
pause;                                  % Wait for experimenter to press a key

%% Psychtoolbox, Stim, Screen Params Init:
disp('Setting up Psychtoolbox parameters...');
disp('This will open a black screen - good luck!');
% This function will make the Psychtoolbox window semi-transparent:
PsychDebugWindowConfiguration(0,0.5);     % Use this to debug the psychtoolbox screen

[window,white,black,screenXpixels,screenYpixels,xCenter,yCenter,ifi] = PsychInit();
topPriorityLevel = MaxPriority(window);
Priority(topPriorityLevel);                     % set highest priority for screen processes 
vbl = Screen('Flip', window);                   % get the vertical beam line 
refreshRate = 1/ifi;                            % refresh rate as given from the screen
numFrames = floor(trialLength/ifi);             % how many frames needed for trialTime display with current framerate
waitFrames = 1;                                 % how many frames to wait for between screen refresh

%% Prepare Green Square Cues & White Square Stims
baseRect = [0 0 200 200];                       % Make a base Rect of 200 by 200 pixels
whiteBaseRects = [0 0 180 180];                 % White stims will be slightly smaller
squareXposRatio = 1/(numTargets+1);             % Screen X positions of rectangles
for i = 1:numTargets
    squareXpos(i) = [screenXpixels * squareXposRatio*i];
end
whiteRects = nan(4, numTargets);                % Init white rectangle coordinates
for i = 1:numTargets                            % set rectangle center points:
    whiteRects(:, i) = CenterRectOnPointd(whiteBaseRects, squareXpos(i), yCenter);
end
penWidthPixels = 6;                             % Pen width for the green frames

%% Prepare frequencies and binary sequences
[conditionBinary] = binaryStimInit(refreshRate,conditionFreq,trialLength);

% Define the keyboard keys that are listened for:
KbName('UnifyKeyNames');
escapeKey = KbName('Escape');                   % let psychtoolbox know what the escape key is

HideCursor;                                     % hides cursor on screen

%% Record Training Stage
outletStream.push_sample(111);    % start of recordings. Later, reject all EEG data prior to this marker

for trial = 1:numTrials
    % Show "Ready" on screen for 2 seconds, followed by the relevant target    
    Screen('TextSize', window, 70);             % Draw text in the bottom portion of the screen in white
    DrawFormattedText(window, 'Ready', 'center',screenYpixels * 0.75, white);
    Screen('Flip', window); 
    pause(1);                                   % "Ready" stays on screen

    DrawFormattedText(window, strcat('Trial #',num2str(trial),' from:',num2str(numTrials)), 'center',screenYpixels * 0.75, white);
    Screen('Flip', window);
    pause(1);                                   % How long should the green cue wait
    outletStream.push_sample(1111);                % Send LSL marker (trial start)
    outletStream.push_sample(trial);     % Send LSL marker (condition)
%     white = ones(numTargets);
    % Display white squares & green cue & keypress listener
    white = [1;1;1];
    for frame = 1:numFrames   
        % Display stim square, colored according to binary vector
%         colorRects = conditionBinary(frame)
        for targ = 1:numTargets
            Screen('DrawText', window, num2str(targ), squareXpos(targ)-20, yCenter-300, white);
        end
        Screen('FillRect', window, (conditionBinary(:,frame)*white')', whiteRects );
        Screen('DrawingFinished',window);
        % Check Keyboard press
        [keyIsDown,secs, keyCode] = KbCheck;    % check for keyboard press
        if keyCode(escapeKey)                   % pushed escape key - SHUT IT DOWN!!!
            ShowCursor;
            sca;
            return
        end
        % Show on screen all the stimuli - assures correct refresh rate
        vbl = Screen('Flip', window, vbl + (waitFrames - 0.5) * ifi);
    end     
end
%% End of recording session
outletStream.push_sample(99);                   % 99 is end of experiment
ShowCursor;
sca;
Priority(0);
disp('Stop the LabRecorder recording!');

