# falcon-train

## Launch instance from template

-   From template **LLMtrainingtest**
-   Make sure OS is **"Deep Learning AMI GPU PyTorch 2.0.1 (Ubuntu 20.04)"**
-   Select Instance type is **g5.<something xlarge>**
-   Make sure Security group **falcon** is selected
-   Set Storage volume size to (at least) **250GiB**
-   Click **Launch instance**

## Log into instance

-   triplecore aws login (`awslogintriplecore <MFA>` for me)
-   `aws ssm start-session --target <InstanceID>`

## get repo

-   `git clone https://github.com/triplecore-consulting/falcon-train.git`
-   `cd falcon-train`

## run setup

-   `bash ./setup.sh`
-   `LD_LIBRARY_PATH` is added to `.bashrc` Restart bash `exec bash` or
    logout/login

## run stuff manually

-   log into instance
-   `cd falcon-train`
-   `bash run.sh`

## run stuff automatically

-   TBD

## TODO

-   fix `LD_LIBRARY_PATH`
