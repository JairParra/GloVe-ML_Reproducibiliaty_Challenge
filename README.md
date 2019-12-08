[![Generic badge](https://img.shields.io/badge/Mini_project_4-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Contributors-3-<COLOR>.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/COMP551-Applied_Machine_Learning-red.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Neat_level-OVER_9000-green.svg)](https://shields.io/)

# COMP551_Mini4: Replication challenge 

- **Track 2:** Reproduce and modify the model. 
"You will first reproduce the results reported in the paper by running the code provided by the authors. Then you will try to modify the model and perform ablation studies to understand the model's robustness and evaluate the importance of the various model components. (In this context, the term "ablation" is used to describe the process of removing different model components to see how it impacts performance.) You can also try to improve the model based on your experiments. You should do a thorough analysis of the model through an
extensive set of experiments. Note that some experiments will be diffcult to replicate due to computational resources. It is fine to reproduce only a subset of the original paper's results or to work on a smaller variant of the data|if necessary. **At a minimum, in this track you should use the authors code to reproduce a non-trivial subset of their results and explore how the model performs after you make minor modiffcations (e.g., changes to hyperparameters). An outstanding project in this track would perform very a detailed ablation study and/or implement significant/meaningful extensions of the model.**. 

## Our paper: 
- https://www.overleaf.com/7741963696nwdpsgxqvvqy

## Objective Replication Paper 

 - **From Group to Invidiual Labels Using Deep Features**
    - Their paper: http://dkotzias.com/papers/GICF.pdf 
    - Their repository: https://github.com/dkloz/GICF 
    - Status **Failed attempt to reproduce**. The complexity of the code, lack of comments and documentation, issues with external code resources, dependency issues. The external library the author uses, ( from Denis et al.) use to produce the word embedding is highly complex, uncommented and undocumented as well. Reproducibility is thus extremely difficult. 
    
 - **GloVe: Global Vectors for Word Representation**
  - Their paper: https://nlp.stanford.edu/pubs/glove.pdf 
  - Their repository: https://github.com/stanfordnlp/GloVe
  - *Comments:* The repository uses code in C, python and bash; however the repository structure is very well organized, the code is fairly clean and well-commented, and they also include a demo.  
  - *What would we like to do?*: Reproduce the paper
 

## Announcements: 
- We are abandoning the previous paper. Focus on the new one 
 
## Tasks: 
- The tasks for each person will be put in here. These tasks will be decided in group. 
If there is something else wants to do additionally, please discuss it and then write it down here as well. 
- If a task is done, don't delete it immediately, instead, put a **done** mark next to it, and wait for two three days to delete it so we can keep track of what's done! 

### All 
- Choose paper, fill the form https://forms.gle/vPiqmT27qM2U5SME7. 
- Read the new paper we're considering 
- Replicate the code on the demo subset locally 
- Come up with experimentation/modification ideas 

### Jair: 
- Start working on the 

### KhorenL:  
- See All 

### Rivka 
- Modify the paper accordingly

### Attribution 

The `Stanford_Glove` subdirectory is cloned from **GloVe: Global Vectors for Word Representation** (https://nlp.stanford.edu/pubs/glove.pdf),and is the object of study of this *Reproducibility Challenge* project.  

The `GICF_code` subdirectory is the cloned repository for the paper **From Group to Individual Labels using Deep Features** (http://mdenil.com/media/papers/2015-deep-multi-instance-learning.pdf) , produced by Dimitrios Kotzias, Misha Denil, Nando De Freitas, and Padhraic Smyth (see http://dkotzias.com/papers/GICF.pdf). The replication, modification and employment of the code is for academic purposes only.  

The `convnet_embeddings_code` is cloned repository for the paper **Extraction of Salient Sentences from Labelled Documents** ("https://arxiv.org/pdf/1412.6815.pdf"), as employed by Denil et al. in their paper *From Group to Individual Labels using Deep Features* (see https://github.com/mdenil/txtnets). 


