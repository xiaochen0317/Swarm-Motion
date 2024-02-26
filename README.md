# Swarm Motion Dataset

A swarm motion simulation dataset is established based on the Boids mathematical model and here is the whole dataset. 

### Data Preparation

------

Download the whole dataset consisting of 300 frames in each sample [Here](https://drive.google.com/file/d/18uS25E2uvhO3vA6aw9-o4ZGQ9oyVkLZq/view) (about 10GB) and put them in the `./Dataset` directory. The overall number of samples is 5,000.

Directory structure:

```shell script
Dataset
|-- data_0.txt
|-- data_1.txt
|-- data_2.txt
|-- ...
|-- data_4999.txt
```

### Data Form

------

The dataset is a `.txt` file consisting of $T$ rows and $2N$ columns which correspond to frames and all $2D$ positions of agents, respectively.  In this dataset, $T$ is set to 300 and $N$ is randomly ranging from 200 to 800. In the phase of motion prediction, we select 151\~160 frames as input and 161\~170 frames as output to avoid initial instability. 

Additionally, another two `.txt` files are given as the index selection of the dataset partition. In `filenames.txt`, the overall 5,000 samples are divided into training, validation, and testing subsets in a ratio of $85\%:5\%:15\%$. To achieve a small-batched pretesting,  a smaller partitioning containing 100 samples is also achieved, namely `filenames_small.txt`. 

In these two `.txt` files, three rows are included, which correspond to the indexes of the training, validation, and testing subsets.

### Self-Made Dataset

------

The simulation code is also provided in `datasetGeneration.py`. You can obtain your own swarm dataset according to different parameter settings. It is worth noting that this code is for generating one sample, you'd better editing another code to generate data sequence according to your requirements.

### Contact

------

Feel free to contact [Me](jiyuchen@tongji.edu.cn) or open a new issue if you have any questions.
