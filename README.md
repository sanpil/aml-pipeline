>## Note   
>The official repo for Azure Machine Learning Notebooks for Pipelines is this: [aka.ms/aml-pipeline-notebooks](https://aka.ms/aml-pipeline-notebooks). This repro introduces concepts in the alpha stage of development. As soon as the Notebooks become official versions, they will be moved from here to the official repo.

# Azure Machine Learning Pipeline

## Overview

The [Azure Machine Learning Pipelines](https://docs.microsoft.com/en-us/azure/machine-learning/service/concept-ml-pipelines) enables data scientists to create and manage multiple simple and complex workflows concurrently. A typical pipeline would have multiple tasks to prepare data, train, deploy and evaluate models. Individual steps in the pipeline can make use of diverse compute options (for example: CPU for data preparation and GPU for training) and languages. 

The Python-based Azure Machine Learning Pipeline SDK provides interfaces to work with Azure Machine Learning Pipelines. To get started quickly, the SDK includes imperative constructs for sequencing and parallelization of steps. With the use of declarative data dependencies, optimized execution of the tasks can be achieved. The SDK can be easily used from Jupyter Notebook or any other preferred IDE. The SDK includes a framework of pre-built modules for common tasks such as data transfer and compute provisioning.

Data management and reuse across pipelines and pipeline runs is simplified using named and strictly versioned data sources and named inputs and outputs for processing tasks. Pipelines enable collaboration across teams of data scientists by recording all intermediate tasks and data.

### Notebooks 

In the official repo at [aka.ms/aml-pipeline-notebooks](https://aka.ms/aml-pipeline-notebooks), there are two types of notebooks: 

* The first type of notebooks will introduce you to core Azure Machine Learning Pipelines features. These notebooks below belong in this category, and are designed to go in sequence; they're all located in the "intro-to-pipelines" folder:

1. [aml-pipelines-getting-started.ipynb](https://aka.ms/pl-get-started)
2. [aml-pipelines-with-data-dependency-steps.ipynb](https://aka.ms/pl-data-dep)
3. [aml-pipelines-publish-and-run-using-rest-endpoint.ipynb](https://aka.ms/pl-pub-rep)
4. [aml-pipelines-data-transfer.ipynb](https://aka.ms/pl-data-trans)
5. [aml-pipelines-use-databricks-as-compute-target.ipynb](https://aka.ms/pl-databricks)
6. [aml-pipelines-use-adla-as-compute-target.ipynb](https://aka.ms/pl-adla)

* The second type of notebooks illustrate more sophisticated scenarios, and are independent of each other. These notebooks include:

1. [pipeline-batch-scoring.ipynb](https://aka.ms/pl-batch-score)
2. [pipeline-style-transfer.ipynb](https://aka.ms/pl-style-trans)
