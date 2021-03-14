## 🧪 Flaky Tests Validty Threats (Assignment 3)

# A) Baseline
The following parts are copied-over from assignment 2:


"
This is a reproduction efforts to re-create the original paper: "What is the Vocabulary of Flaky Tests?" as part of the 
study program "Mining Software Repositories (MSR 2020-21)" provided by SoftLang Team at University of Koblenz-Landau. 
" - Amir Dashti

## MetaData:
This repository describes the recreation of 2020 Paper "What is the Vocabulary of Flaky Tests?" written by: Gustavo Pinto and
               Breno Miranda and
               Supun Dissanayake and
               Marcelo d'Amorim and
               Christoph Treude and
               Antonia Bertolino.


Here, we try to re-create what the original work has achieved to re-confirm and evaluate the challenges involved in
making or verification of an MSR paper. The flaky tests are tests that pass and fail periodically without any code changes. 
There might be different underlying reasons causing such tests to occur. This paper continues investigations of 2 existing papers.
They used the base dataset of manually tracked flaky tests and automated the suggested framework to find vocabulary (simply tokens and keywords) that relate to flakiness using NLP. 


Links to Original Work:

DBLP: https://dblp.org/rec/conf/msr/0001MDdTB20.html?view=bibtex

Conference Link: https://2020.msrconf.org/details/msr-2020-papers/43/What-is-the-Vocabulary-of-Flaky-Tests-

GitHub Link: https://github.com/damorimRG/msr4flakiness

-----------------
Research Questions (*** adopted from the paper):

RQ1. How frequently do flaky tests happen and how prevalent they are?

RQ2. What is the precision of predicting test flakiness using tokens collected from the source code?

RQ3. What is the importance of different features within the model?

RQ4. Find the tokens that are highly connected to flakiness of a tests.

## Requirements:

Minimum Hardware:
- MacOs Catalina or Linux Distributions
  
- Intel Core-i7 x ,2.2 GHZ 6 Cores  

- RAM 8 GB (I recommend at least 16 GB)
  
Software:
  
- Vanilla ZSH bash (or equivalent)

- Python 3.8 or above (use Conda)

- Docker (already running) * ⛴ Docker is only needed if you use the heavy mode

## Process:
The general re-creation work done by us goes through the following steps:

![Alt text](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/doc/diagrams/general-procedure.png?raw=true "General Procedure")

0- Re-organize: the original repository is very poorly organized the data and codes are mixed we will automatically clone and reorganize it in right places.

1- Detection: Depending on your decision can prepare flaky / non-flaky samples:

> e - EASY mode will use already processed initial data.
> 
> h - HEAVY mode will fully re-calculate flaky and non-flaky samples.

2- Identification (tokenization): Uses NLP approaches to find tokens and candidate features.

3- Discovery: Finalizes the classifier model and produces the outputs.

4- Comparison: Open-ended process to check and verify the output.


If you have a compatible extended shell simply running the 'initialization' file will execute 
everything necessary for this project. From there follow the steps console asks (it automatically sets the right environment and installs necessary packages):


```shell
# to initialize and run everything
zsh ./process/initialization.sh

# it will prompt and asks question if needed

# Please choose the mode? [Easy Mode (e or ez) | Heavy Mode (h or hv)]

> h # if you want full process
> e # if you want demo process

# the process might take few minutes
```

👉 Please refer to
[Process iPython](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/process/process.ipynb) file to see the full explanations about the process.


- Important 1: The password is your machine's password (needed for Git Clone).

- Important 2: Refer to the extra section if something did not work.

- Important 3: I have made a code to make env on the fly but it fails sometimes; easisest way is just to use automatic tool
if you have PyCharm or InteliJ products:
  
![Alt text](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/doc/diagrams/env.png?raw=true "  ")

 ✅  How to Validate the works?
--------------------
If everything works properly, the output produced by the code 'features_frequency.csv' will include the
top most related vocabulary to flakiness of the tests. You can quickly verify this by running coe in the easy (e) mode.

Refering to the paper: "we noted that
job, action, and services are commonly associated with flaky tests.".
So, the output here should be also similar.



## Data:
Following is the general description of data types along with the schema overview:

---
- Basics:

> Positive === Flaky Test
> 
> Negative === Estimated Flaky Test (a test that is not proven to be flaky so far)

- Initial Dataset:

#### The main dataset that has been used for this work is called "DeFlaker".


> The original paper faces the following issues using the dataset:
>
> 1- The dataset does not list the non-flaky tests but since it was needed for their model training; they ran the tests multiple times to find possible candidates.
>
> 2- One of the projects fails in build so they use 24 out of 25 Java projects provided by the dataset.
>
>
>For further on DeFlaker: http://www.deflaker.org/icsecomp/
> 
>  <sup>Note: This part is adopted (in simple words) from the paper. </sup>

The structure of our data: (To see sample parts of data refer to: [Delta iPython](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/process/delta.ipynb))

A) Input:

- historical_projects_copied.csv: A csv file used as an input in original paper. It includes list of github projects that have been monitored.

- histoircal_rerun_flaky_tests.csv: A csv file used as an initial input that includes detailed list of test files and test methods that are known as being flaky.

- list-flaky.csv: A csv file very similar to histoircal_rerun_flaky_tests.csv but it also includes SHA and version of flakiness since they might have change or fixed.

- ez/ : This directory includes a copy of the mentioned files for representation purposes. It is not used in real processes.

B) Temp:

- test_files/ : Includes multiple text files each file including the full text from a specific test file.
  File name represents the test file name and its category.

- test_cases/ : Running methods jar file will separate test files to test cases. This directory includes multiple text files; 
 each file includes text of a specific test known to be flaky.

- sample_flaky/ : Includes multiple text files that are separated line by line; each line has a token grabbed and processed from a respective
test case file.

C) Output:

- features_raw.csv: Includes raw list of all tokens with their frequencies. It is not yet decided how effective they are in flakiness.

- features_frequency.csv: It includes top filtered tokens that associate with flaky tests and make the vocabulary of flaky tests.

- total_process_original.txt: This file includes the whole code strings of original repository. -- Used to calculated Levenshtein distance.
  
- total_process_rework.txt: This file includes the whole code strings of re-production repository. -- Used to calculated Levenshtein distance.

- total_data_original.txt: This file includes the whole data string of rhe original repository. -- Used to calculated Levenshtein distance.
  
- total_data_rework.txt: This file includes the whole data string of rhe re-production repository. -- Used to calculated Levenshtein distance.

- ez/ : This directory includes a copy of the mentioned files for representation purposes. It is not used in real processes.


## 🔥 Delta:

Please refer to my Jupyter
[Delta iPython](https://nbviewer.jupyter.org/github/gocontractdev/flaky-tests-reproduction/blob/main/process/delta.ipynb) file to see the explanations about the project's delta. Here is the summary:
#### A) about Process:
The methodology used in original and recreation work are same however due to issues in the code or un-explained manaul parts; we had to employ remedees or alternatives in the implementation and exection of the proccess.
The alternatives we had to adopt include:

1- Re-organization: The data and code are poorly mixed in the original work. The first part of the 'actuall.py' focuses on moving file to their correct directory.

2- Fixing python codes that do not run: There are parts of the code that need minor changes to work. I have used the original work and deep-linked them using __importy__() method.
In cases that it was not possible, I have made a custom method that includes the fixed version of original code.

3- Unexplained gradle build and java runtimes: Parts that use the java jdk and gradle are un-explained in the original work. It seems like the authors have ran them manually.
Since running manually is difficult for me. I have made a DockerFile that starts and Alpine injected with Java and Gradle to handle the builds and making output results. This change means you need both Python environment and Docker to run this project.


### 📊 Mathematical Distances: 

Hamming Distance [noamlized]: 1.6694457422028464e-06
Jacard dis-similarity 4.42110833769081e-05
Sorensen-Dice:  8.841825768685356e-05

#### B) about Data:
Flow of data and what is being generated are almost identical to each other since same approaches have been adopted.
We can divide the data into 3 sections:

1- Input: Input data is completely identical; we use exact same inputs.

2- Temp: Temporary data created by us resembles the original work. We only missed the re-runs folder since developing a docker
that runs projects multiple times took too much effort and was out of scope of me doing it alone.

3- Output: Uses similar format, naming and outputs. We have extra output that have been used for calculation of distance between original work and recreation.


###  📊 Mathematical Distances:

Hamming Distance [noamlized]: 0.055623301256152224
Jacard dis-similarity 0.12280896383403594
Sorensen-Dice:  0.2187530876395613

## Extra:
#### A) What should I do if installing pyCurl failed?

```shell
# if pycurl failed for you on MAC -- couldn't find any other solution 
xcode-select --install

# if necessart export the path of anaconda
export PATH="/usr/local/anaconda3/bin:$PATH"

# quick login to alpein (it is only used for builds and running java) 
docker container exec -it my_little_alpine bin/bash

# You can activate the environment if you want but the initialization does that Automatically
source ez_env/bin/activate
# to exit env simply type
deactivate
```

#### B) Known Issues:

1- The environment which comes along with the project is broken.
It fails in installation of 'pyCurl' depending on you O.S. and your SSL settings it may happen or not happen.

2- Some python files do not actually work. I have modified them to achieve the goals; further on this is explained in 
[Process iPython](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/process/process.ipynb).

3- For me, without anaconda path it does not work; Make it somehow that zsh and anaconda work fine:

![Alt text](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/doc/diagrams/anaconda.png?raw=true "  ")

4- If you stop process after making folder and before cloning it just skips it becasue it only checks the folder; generally do not stop script it fails completely.

![Alt text](https://github.com/gocontractdev/flaky-tests-reproduction/blob/main/doc/diagrams/whenempty-cloning-ignored.png?raw=true "   ")


---------------------

# B) Experiment
In this assignment, we would investigate one of the threats to internal validity found in "What is the Vocabulary of Flaky Tests?“ paper.
The threat and the rationale behind it are as follows:

## Threat:


![threat](https://github.com/gocontractdev/flaky-test-threat/blob/main/doc/threatcall.png?raw=true "What is the threat")


This paper discusses a semi-automated procedure to generate a model for detecting flaky tests.
The model, relies on the tokens (or simply keywords) extracted and learned from the flaky and non-flaky test cases.
Although the flaky tests have been confirmed both by human readers and through running them multiple times, not enough confidence for tests labeled as non-flaky is established.
In other words, the paper only relies on estimations for the tests labeled as non-flaky without proving nor justifying the choice of 100 re-runs to assure a single test is non-flaky.
 
Hence, a massive threat to internal validity of this work exists in the initial labelling section.
If one or more tests that attribute to flaky behaviour are labeled incorrectly, the final model may struggle in detecting true patterns and tokens attributing to each class.

## Traces:
Finding the traces for the threats to validity of the present paper is rather easy, since they are all thoroughly mentioned in the section „6.1 Threats to Validity“. The authors also mentioned it back in the section  „4 Objective of Analysis“:
 
„Indeed, the diagnosis of non-flakiness is an estimate—there is no guarantee a test is non-flaky with a given number of runs“ *1 (4 Objective of Analysis)
 
This sentence openly states that we do not have a guarantee for non-flakiness and this is in-fact a probability.
 
„When performing our first experiment (running the test cases of 24 Java projects 100 times to find flaky tests), we noticed that 55% of the test cases passed 99 times, and failed just once. This result suggests that the strategy of rerunning tests several times to detect flakiness could miss cases of flakiness as tests could have been insufficiently executed“ *1 (6.1 Threats to Validity)
 
The statistics mentioned over here is rather alarming. Claiming that running tests 99 times could result in missing almost half of their flaky tests suggests that maybe the chosen threshold is far from optimal.

## Theory:
As mentioned above, it seems like the initial non-flaky test cases used in training the model might be labeled incorrectly. I have quoted parts of the paper that confirm this threat potentially exists. My hypothesis is : „Executing test cases more than 100 times can result in finding previously undetected flaky tests“. I will try to falsify this hypothesis. To do so, I will run a set of tests exhaustively to find a new more optimal threshold for reruns. Then show more executions do not result in a significant deviations from our confidence interval (or the hypothesis can not be falsified).

## Feasibility:
It is obviosuly a heavy task to run unit tests for many times. As a result, I will first try to statistically calculate a new threshold as maximum execution efforts based on the present data we already have access to. Next, I run tests until noticing the first occurrence of a switch in output (true test resulting false or vice versa) or reaching the max threshold for small chosen set of test cases. Lastly, I will compare the original distribution and the new distribution of flaky/ non-flaky tests and find out whether the difference is significant enough.
 
In small scale, this task seems to be feasible, I will try to justify the statistical calculations and avoid introduction of new biases in selection of samples. It is worth mentioning that I might fail in proving the new threshold performs better but still show the threat exists. As for our course, it would be enoguh to only show the re-execution threshold chosen on this paper is not optimal and as a result the trained model of this MSR paper is incomplete and there is a room for study (futher investigations are more time consuming).

## Implementation:

## Results:

## Requirements:

## Process:

## Data:
